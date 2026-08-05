---
title: "Cell Flow Builder"
sidebar_position: 1
---

The Cell Flow builder generates organic, non-grid layouts.   Instead of laying rooms out on a tile grid, it
partitions the play area into cells, merges them into chunks and grows the flow graph's paths through them.
The result is a layout with irregular room shapes and dynamic height, which is hard to get out of a grid based
builder

Cell Flow uses the same flow graph framework as Grid Flow and Snap Grid Flow, so paths, key-locks, items and
the Finalize node all work the way you already know them

## Video

This walkthrough builds a Cell Flow graph from scratch

<iframe width="100%" height="540" loading="lazy" src="https://www.youtube.com/embed/Q7c4UwVqlPs" frameborder="0" allowfullscreen></iframe>

## Grid or Voronoi

The layout starts with one of the two Create Cells nodes, and this is the main decision you make up front

| Node | Use it for |
|------|------------|
| `Create Cells (Grid)` | Rectangular rooms of varying sizes.   Rooms still merge into irregular chunks, but every edge stays axis aligned, so it works well with modular art built for right angles |
| `Create Cells (Voronoi)` | Fully organic cells with angled walls.   Best paired with the voxel workflow, where the geometry is generated rather than assembled from modular meshes |

Both nodes share the same chunk merging settings, so you can swap one for the other without rebuilding the rest
of the graph

## Node Reference

The layout graph nodes execute in this order

| Node | What it does |
|------|--------------|
| `Create Cells (Grid)` / `Create Cells (Voronoi)` | Creates the initial cell graph to work on |
| `Create Main Path` | Creates the main path with the spawn and goal rooms |
| `Create Path` | Grows a branch path on the existing network |
| `Spawn Items` | Spawns items in the layout nodes |
| `Create Key/Lock` | Creates a key and lock pair along a path |
| `Finalize Graph` | Finalizes the layout graph |
| `Scatter Props (Grid)` | Scatters props in the free space around the scene |

## Voxel Worlds

Cell Flow is the builder most often paired with the voxel workflow, which carves caves and islands out of a
voxel volume instead of spawning modular meshes.   Voxel carving is configured on the Dungeon actor and is not
exclusive to this builder - see [Voxel Worlds](../advanced-dungeons/advdungeon-voxel-worlds.md)

## Next Steps

* [Cell Flow Settings](cellflow-settings.md) - the dungeon config and the layout node properties
