#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
import re
import sys
from collections import defaultdict
from urllib.parse import unquote

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".tif", ".tiff", ".avif", ".ico"}
MD_EXTS = {".md", ".mdx"}

INLINE_IMG_RE = re.compile(
    r'!\[(?P<alt>[^\]]*)\]\s*\(\s*(?P<url><[^>]+>|[^)\s]+)'
    r'(?P<title>\s+(?:"[^"]*"|\'[^\']*\'|\([^()]*\)))?\s*\)',
    re.IGNORECASE
)

REF_DEF_RE = re.compile(
    r'^(?P<indent>\s*)\[(?P<id>[^\]]+)\]:\s*(?P<url><[^>]+>|\S+)'
    r'(?P<title>\s+(?:"[^"]*"|\'[^\']*\'|\([^()]*\)))?\s*$',
    re.IGNORECASE | re.MULTILINE
)

HTML_IMG_RE = re.compile(r'(<img\b[^>]*\bsrc=["\'])(?P<src>[^"\']+)(["\'][^>]*>)', re.IGNORECASE)
ABS_URI_RE = re.compile(r'^(?:[a-zA-Z][a-zA-Z0-9+.\-]*:|#)')
ANGLE_BRACKETS_RE = re.compile(r'^[<](.*)[>]$')

def is_image_file(filename: str) -> bool:
    return os.path.splitext(filename)[1].lower() in IMAGE_EXTS

def is_markdown_file(filename: str) -> bool:
    return os.path.splitext(filename)[1].lower() in MD_EXTS

def posixify(path: str) -> str:
    return path.replace(os.sep, '/')

def collect_images(base_dir: str, images_roots=None, exclude_dirs=None):
    mapping = defaultdict(list)
    roots = []
    if images_roots:
        for r in images_roots:
            root = os.path.join(base_dir, r)
            if os.path.isdir(root):
                roots.append(root)
    if not roots:
        roots = [base_dir]

    exclude_set = set(exclude_dirs or [])

    def should_exclude_dir(abs_dir: str) -> bool:
        rel = os.path.relpath(abs_dir, base_dir)
        return any(rel == ed or rel.startswith(ed + os.sep) for ed in exclude_set)

    for root in roots:
        for cur, dirs, files in os.walk(root):
            dirs[:] = [d for d in dirs if not should_exclude_dir(os.path.join(cur, d))]
            for f in files:
                if is_image_file(f):
                    rel = os.path.relpath(os.path.join(cur, f), base_dir)
                    mapping[f.lower()].append(posixify(rel))
    return mapping

def existing_path_ok(markdown_dir: str, url: str) -> bool:
    m = ANGLE_BRACKETS_RE.match(url)
    if m:
        url = m.group(1)
    candidate = unquote(url)
    if ABS_URI_RE.match(candidate):
        return True
    abs_path = os.path.normpath(os.path.join(markdown_dir, candidate))
    return os.path.isfile(abs_path)

def raw_basename_from_url(url: str) -> str:
    m = ANGLE_BRACKETS_RE.match(url)
    if m:
        url = m.group(1)
    url = url.split('#', 1)[0].split('?', 1)[0]
    url = unquote(url)
    return os.path.basename(url).lower()

def alt_variants_for_basename(basename_lower: str):
    """
    Generate fallback variants for Writerside-style prefixes.
    First yield the exact name (to prefer exact matches),
    then variants with X- / X_ / X␠ stripped.
    """
    yield basename_lower
    if basename_lower.startswith("x-"):
        yield basename_lower[2:]
    if basename_lower.startswith("x_"):
        yield basename_lower[2:]
    if basename_lower.startswith("x "):
        yield basename_lower[2:]

def best_match_for_candidates(image_map, candidate_names, markdown_dir, base_dir):
    """
    For a sequence of candidate base names, try exact filename matches in order.
    If multiple paths exist for a given name, pick the one 'closest' to the md file.
    """
    for name in candidate_names:
        candidates = image_map.get(name)
        if not candidates:
            continue
        if len(candidates) == 1:
            return candidates[0]
        # choose closest path to markdown_dir
        best = None
        best_score = None
        for rel_img in candidates:
            img_abs = os.path.join(base_dir, rel_img)
            rel_from_md = os.path.relpath(img_abs, markdown_dir)
            score = (rel_from_md.count(os.sep), len(rel_from_md))
            if best_score is None or score < best_score:
                best = rel_img
                best_score = score
        return best
    return None

def replace_inline_images(text, markdown_dir, base_dir, image_map, stats):
    def repl(m):
        alt = m.group('alt')
        url = m.group('url')
        title = m.group('title') or ""

        if existing_path_ok(markdown_dir, url) or ABS_URI_RE.match(url):
            return m.group(0)

        base = raw_basename_from_url(url)
        new_rel = best_match_for_candidates(image_map, alt_variants_for_basename(base), markdown_dir, base_dir)
        if not new_rel:
            stats['unresolved'].add(url)
            return m.group(0)

        new_url = posixify(os.path.relpath(os.path.join(base_dir, new_rel), markdown_dir))
        stats['replacements'].append((url, new_url))
        return f"![{alt}]({new_url}{title})"
    return INLINE_IMG_RE.sub(repl, text)

def replace_ref_defs(text, markdown_dir, base_dir, image_map, stats):
    def repl(m):
        indent = m.group('indent')
        id_ = m.group('id')
        url = m.group('url')
        title = m.group('title') or ""

        if existing_path_ok(markdown_dir, url) or ABS_URI_RE.match(url):
            return m.group(0)

        base = raw_basename_from_url(url)
        new_rel = best_match_for_candidates(image_map, alt_variants_for_basename(base), markdown_dir, base_dir)
        if not new_rel:
            stats['unresolved'].add(url)
            return m.group(0)

        new_url = posixify(os.path.relpath(os.path.join(base_dir, new_rel), markdown_dir))
        stats['replacements'].append((url, new_url))
        return f"{indent}[{id_}]: {new_url}{title}"
    return REF_DEF_RE.sub(repl, text)

def replace_html_imgs(text, markdown_dir, base_dir, image_map, stats):
    def repl(m):
        pre = m.group(1)
        src = m.group('src')
        post = m.group(3)

        if existing_path_ok(markdown_dir, src) or ABS_URI_RE.match(src):
            return m.group(0)

        base = raw_basename_from_url(src)
        new_rel = best_match_for_candidates(image_map, alt_variants_for_basename(base), markdown_dir, base_dir)
        if not new_rel:
            stats['unresolved'].add(src)
            return m.group(0)

        new_url = posixify(os.path.relpath(os.path.join(base_dir, new_rel), markdown_dir))
        stats['replacements'].append((src, new_url))
        return f"{pre}{new_url}{post}"
    return HTML_IMG_RE.sub(repl, text)

def process_markdown_file(path, base_dir, image_map, apply_changes, backup_ext):
    stats = {'file': path, 'replacements': [], 'unresolved': set()}
    md_dir = os.path.dirname(path)
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    updated = original
    updated = replace_inline_images(updated, md_dir, base_dir, image_map, stats)
    updated = replace_ref_defs(updated, md_dir, base_dir, image_map, stats)
    updated = replace_html_imgs(updated, md_dir, base_dir, image_map, stats)

    changed = updated != original
    if changed and apply_changes:
        if backup_ext:
            with open(path + backup_ext, 'w', encoding='utf-8') as bf:
                bf.write(original)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(updated)

    return changed, stats

def find_markdown_files(base_dir, exclude_dirs=None):
    files = []
    exclude_set = set(exclude_dirs or [])

    def should_exclude_dir(abs_dir: str) -> bool:
        rel = os.path.relpath(abs_dir, base_dir)
        return any(rel == ed or rel.startswith(ed + os.sep) for ed in exclude_set)

    for root, dirs, fnames in os.walk(base_dir):
        dirs[:] = [d for d in dirs if not should_exclude_dir(os.path.join(root, d))]
        for f in fnames:
            if is_markdown_file(f):
                files.append(os.path.join(root, f))
    return files

def main():
    ap = argparse.ArgumentParser(description="Fix Markdown image links by mapping filenames to discovered image paths.")
    ap.add_argument("--base", default=".", help="Base directory (project root). Default: .")
    ap.add_argument("--images-root", nargs="*", help="Optional image roots (relative to base). If omitted, search entire base.")
    ap.add_argument("--exclude", nargs="*", default=[".git", "node_modules", ".docusaurus", "build"],
                    help="Directories to exclude (relative to base).")
    ap.add_argument("--apply", action="store_true", help="Write changes in-place (creates backups unless --no-backup).")
    ap.add_argument("--no-backup", action="store_true", help="Do not create .bak backups when applying changes.")
    ap.add_argument("--verbose", action="store_true", help="Print extra diagnostics.")
    args = ap.parse_args()

    base_dir = os.path.abspath(args.base)
    if not os.path.isdir(base_dir):
        print(f"Base directory not found: {base_dir}", file=sys.stderr)
        sys.exit(1)

    image_map = collect_images(base_dir, args.images_root, args.exclude)
    total_images = sum(len(v) for v in image_map.values())
    unique_names = len(image_map)
    print(f"Discovered {total_images} images ({unique_names} unique filenames).")

    md_files = find_markdown_files(base_dir, args.exclude)
    print(f"Found {len(md_files)} markdown files.")

    apply_changes = args.apply
    backup_ext = "" if args.no_backup else ".bak"

    total_changed = 0
    total_replacements = 0
    unresolved_all = set()

    for md in md_files:
        changed, stats = process_markdown_file(md, base_dir, image_map, apply_changes, backup_ext)
        if args.verbose:
            print(f"Processed {os.path.relpath(md, base_dir)}: "
                  f"{len(stats['replacements'])} changes, {len(stats['unresolved'])} unresolved")
        if stats['replacements']:
            print(f"- {os.path.relpath(md, base_dir)}:")
            for old, new in stats['replacements']:
                print(f"    {old}  ->  {new}")
            total_replacements += len(stats['replacements'])
        if stats['unresolved']:
            print(f"! Unresolved in {os.path.relpath(md, base_dir)}:")
            for u in sorted(stats['unresolved']):
                print(f"    {u}")
            unresolved_all.update(stats['unresolved'])
        if changed:
            total_changed += 1

    print("\nSummary:")
    print(f"  Files changed     : {total_changed}")
    print(f"  Links replaced    : {total_replacements}")
    print(f"  Unresolved links  : {len(unresolved_all)}")
    if not apply_changes:
        print("\n(Dry-run) No files were modified. Re-run with --apply to write changes.")

if __name__ == "__main__":
    main()
