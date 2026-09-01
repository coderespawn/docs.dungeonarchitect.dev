---
title: "Voxel Worlds"
sidebar_position: 1
---

The voxel workflow carves your dungeon out of a solid voxel world instead of assembling it from modular meshes.
The layout your builder generates is used to cut caves, islands and tunnels out of a density field, which is
then meshed into geometry with full Nanite and Lumen support

This is configured on the Dungeon actor, not on the builder, so it works alongside whichever builder you are
using.   It is most often paired with the [Cell Flow builder](../cell-flow/cellflow-overview.md), whose organic
cell shapes suit carved geometry better than a tile grid

<iframe
    width="100%"
    height="540"
    src="https://www.youtube.com/embed/KVH-zzC8TV4"
    frameBorder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowFullScreen
/>

## Enable It

Select your dungeon actor and check `Carve Voxels` in the `Voxel` category.   The mesh, noise and SDF model
settings below it become editable once it is on

Then assign a `Voxel SDF Model`.   This decides what kind of world you are carving out of

| Model | World |
|-------|-------|
| Cave | An underground cave system, with optional holes punched through the ceiling |
| Island | An island sitting in water, with a shoreline that slopes away from the land |
| Floating Island | An island floating in the air, tapering to a tip below it |

Each model has its own settings - see [SDF Models](voxel-sdf-models.md)

## Next Steps

* [Voxel Settings](voxel-settings.md) - mesh, material and noise settings
* [SDF Models](voxel-sdf-models.md) - the per-world settings for caves and islands
* [Dedicated Servers](voxel-dedicated-servers.md) - how headless targets build the same world
