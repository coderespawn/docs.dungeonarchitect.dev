---
title: "Interactive Theme Editor Mode"
sidebar_position: 8
---

The Theme Editor window is not the only way to build a theme.   The `Dungeon Theme` editor mode lets you design
a theme directly in the level viewport - drag a mesh onto a wall in the actual dungeon and it is attached to
that marker across the whole level straight away, instead of dropping it into a graph and rebuilding to see
where it landed

<iframe
    width="100%"
    height="540"
    src="https://www.youtube.com/embed/99YniYNoT1E"
    frameBorder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowFullScreen
/>

## Entering the Mode

Build a dungeon in your level, then pick `Dungeon Theme` from the editor mode ribbon in the level editor

The mode works on the dungeon that is already in the level, so the theme you edit is the one assigned to that
dungeon actor

## The Tools

| Tool | What it does |
|------|--------------|
| Select | The default tool.   Picks marker nodes and spawned actors in the viewport |
| Marker Node | Drag and drop assets from the content browser into the viewport to attach them to the selected marker nodes |
| Visual Node | Modifies the actors associated with the visual theme node |

## Why use it

The graph view in the Theme Editor window shows you the structure of a theme.   The viewport shows you the
result.   This mode collapses the gap between the two, which matters most when you are placing art that has to
line up with the grid - trim, corner pieces, ceiling props - where the graph tells you nothing about whether
the mesh actually fits

You are editing the same theme asset either way, so you can move between the window and this mode freely, and
whichever one you use, the changes land in the same file

:::note
Changes propagate to every matching marker in the level as you make them.   If you only want a mesh in one
spot, that is a job for a hand placed actor, not a theme node
:::
