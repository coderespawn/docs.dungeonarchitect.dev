---
title: "Module Selection & Repetition"
sidebar_position: 15
---

When multiple registered modules fit a layout node, the builder has to pick one.  This page describes how that
choice is made and how you can control it to avoid repeating rooms and create unique landmark rooms

You don't need a huge module library for this to work well.  A small set of modules can go a long way with the
right settings

## Module Database Settings

These are set on each module entry in the Module Database

| Property         | Default | Description                                                                                                                                     |
|------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Selection Weight | 1.0     | How often this module shows up compared to the other fitting modules.  A module with weight `2.0` shows up twice as often as one with weight `1.0` |
| Max Instances    | 0       | The maximum number of times this module can appear in a single dungeon.  `0` means unlimited.  Set this to `1` to create unique landmark rooms that show up at most once |

## Dungeon Settings

Select your dungeon actor and look for `Module Selection` in the config.  Every penalty here ranges
from `0` to `1`

* `0` disables the penalty
* `1` means avoid this module unless it is the only option that fits

| Property             | Default | Description                                                                                                                    |
|----------------------|---------|--------------------------------------------------------------------------------------------------------------------------|
| Repeat Nearby Penalty | 1.0     | Applied when the same module already appears nearby, either within `Repetition Radius` grid cells or within `Repetition Depth` rooms along the path |
| Repetition Radius     | 2       | A module counts as nearby if another instance of it lies within this many grid cells, in any direction.  `0` disables the distance check |
| Repetition Depth      | 3       | A module counts as nearby if it was used within this many rooms along the path leading to this room.  `0` disables the path check |
| Reuse Penalty         | 0.5     | Applied once for every existing instance of the module anywhere in the dungeon.  This spreads the selection across your whole module set |
| Extra Door Penalty    | 0.3     | Applied once for every module door that would be left unused and walled off.  Higher values prefer modules whose doors match the layout snugly |

## Selection Score

For every module that fits a layout node, the builder computes a score:

```
score = Selection Weight
      x (1 - Reuse Penalty) ^ (times already used)
      x (1 - Repeat Nearby Penalty)   if an instance is nearby
      x (1 - Extra Door Penalty) ^ (unused doors)
```

The module is then picked with a weighted random selection.  A module with double the score of another is
twice as likely to be chosen.  Modules whose score reaches `0` are only used when nothing else fits, so the
dungeon will still resolve even with very strict settings

## Common Setups

* **Unique boss / shop room**:  Set `Max Instances` to `1` on the module.  If you have several variations
  registered, each capped at `1`, a dungeon that needs two of them is guaranteed to pick two different ones
* **Small module set, more variety**:  Raise the `Reuse Penalty` (e.g. `0.75`).  The builder will use every
  fitting module before it starts repeating any of them
* **No side-by-side repeats**:  Keep `Repeat Nearby Penalty` at `1` and raise the `Repetition Radius` if you
  still spot the same room from an adjacent corridor
* **Snug corridors**:  Raise the `Extra Door Penalty` so corridor cells prefer 2-door modules over 4-door
  rooms with walled-off doorways

:::note
The older `Non Repeating Rooms` and `Prefer Modules with Minimum Doors` settings were removed and replaced by
this system.  `Repetition Radius` / `Repetition Depth` cover what `Non Repeating Rooms` did, and also catch
repeats across nearby branches, which the old setting missed.  Use the `Extra Door Penalty` instead of
`Prefer Modules with Minimum Doors`

`Selection Weight` now controls how often a module shows up.  Previously a module with a slightly higher
weight would always win over the lower weighted ones and they would never get picked.  Now a weight of `2.0`
means twice as often, not always first
:::
