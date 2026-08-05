---
title: "Cell Flow Settings"
sidebar_position: 2
---

This page lists the settings on the Cell Flow dungeon config and on the layout graph nodes that are specific to
this builder.   The path, item and key-lock properties that every flow builder shares are covered in the flow
graph documentation

## Dungeon Config

Select your dungeon actor and look at the config

| Property | Default | Description |
|----------|---------|-------------|
| Cell Flow | *none* | The Cell Flow asset that holds the layout graph |
| Grid Size | `(400, 400, 200)` | The size of a single layout cell in world units.   The Z value is the height of one floor level |
| Max Retries | `50` | How many times the builder retries the layout before giving up |
| Parameter Overrides | *empty* | Overrides node parameters by name at build time, so a single graph can drive several dungeons |
| Marker Config | *none* | The marker settings asset that maps paths to the markers they emit |

## Create Cells

These are shared by both the `Create Cells (Grid)` and `Create Cells (Voronoi)` nodes

| Property | Default | Description |
|----------|---------|-------------|
| World Size | `(30, 30)` | The size of the play area in layout cells |
| Min Group Area | `20` | The smallest area a merged chunk is allowed to have |
| Cluster Blobbiness | `0.5` | Controls the shape of the merged chunks.   `0.5` keeps the classic behaviour, higher values create rounder more compact chunks, lower values create longer stringier chunks.   Ranges from `0` to `1` |

### Create Cells (Grid)

| Property | Default | Description |
|----------|---------|-------------|
| Min Cell Size | `1` | The smallest cell the grid partition may produce |
| Max Cell Size | `6` | The largest cell the grid partition may produce |
| Fit Iterations | `20` | How many attempts are made to fit cells into the play area.   Raise it for a denser packing |
| Min Aspect Ratio | `0.4` | Cells narrower than this ratio are rejected |
| Max Aspect Ratio | `1.5` | Cells wider than this ratio are rejected |

### Create Cells (Voronoi)

| Property | Default | Description |
|----------|---------|-------------|
| Num Points | `100` | The number of Voronoi sites scattered across the play area.   More points means smaller cells |
| Num Relax Iterations | `5` | Lloyd relaxation passes.   Higher values even out the cell sizes and make them more regular |
| Disable Boundary Cells | `true` | Drops the cells touching the outer boundary, which are unbounded and stretch off to the edges |
| Edge Connection Threshold | `0.2` | Two adjacent cells are only connected if their shared edge is at least this ratio in length.   This avoids connections through a sliver of an edge.   This is an advanced setting |

## Create Main Path / Create Path

Both path nodes carry these Cell Flow specific properties, on top of the path settings shared by all flow builders

| Property | Default | Description |
|----------|---------|-------------|
| Ceiling Height Min | `1` | The smallest ceiling height a node on this path may use, in floor levels |
| Ceiling Height Max | `4` | The largest ceiling height a node on this path may use, in floor levels |
| Room Size Min | `1` | The smallest number of layout cells a node on this path may merge into a single larger room |
| Room Size Max | `1` | The largest number of layout cells a node on this path may merge into a single larger room.   Each node rolls a size between the min and max and absorbs that many adjacent free cells |

## Common Setups

* **Bigger halls on the main path**:  Set `Room Size Min` / `Room Size Max` to something like `2` and `4` on the
  `Create Main Path` node and leave the branch paths at `1`.   The main route then reads as a series of large
  halls linked by narrow side passages
* **Compact chunks**:  Raise `Cluster Blobbiness` above `0.5`.   Lower it for long stringy chunks that feel more
  like winding tunnels
* **Tighter cave cells**:  On the Voronoi node, raise `Num Points` and `Num Relax Iterations` together.   More
  points shrink the cells and more relaxation keeps them evenly sized instead of a mix of slivers and blobs

:::note
Keeping both `Room Size` values at `1` gives one layout cell per node, which is how graphs behaved before this
setting existed.   Existing graphs are unaffected
:::
