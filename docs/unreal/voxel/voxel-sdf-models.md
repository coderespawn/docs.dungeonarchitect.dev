---
title: "SDF Models"
sidebar_position: 3
---

The SDF model decides what kind of world the dungeon is carved out of.   Assign one to `Voxel SDF Model` on the
Dungeon actor

## Cave

An underground cave system.   Rooms get extra headroom above the layout, and holes can be punched through the
ceiling to let light down into them

| Property | Default | Description |
|----------|---------|-------------|
| Ceiling Extra Height | `800` | Extra headroom added above the room height |
| Enable Ceiling Holes | `true` | Punches holes through the cave ceiling, letting light down into the rooms |
| Ceiling Hole Radius | `600` | The radius of a ceiling hole |
| Ceiling Hole Height Offset | `400` | How far above the ceiling the hole is centred |
| Max Ceiling Holes Per Room | `2` | The most holes a single room may get |
| Ceiling Hole Spawn Probability | `0.5` | The chance a room gets a ceiling hole at all |

## Island

An island sitting in water.   The platform extends below ground level and the surrounding water slopes away
from the shoreline

| Property | Default | Description |
|----------|---------|-------------|
| Platform Depth | `200` | How deep the island platform extends below the ground level |
| Edge Taper Depth | `0` | Additional depth variation at the platform edges, for a more natural island edge |
| Water Level | `0` | The Z height of the water |
| Shore Slope | `0.2` | How much the water slopes down away from the island.   `0` is flat |
| Shoreline Extent | `4000` | The maximum horizontal distance the shoreline reaches out from the island edge |
| Shoreline Falloff Distance | `0` | Falloff applied to the shoreline effect, to avoid discontinuities at chunk boundaries |
| Max Shore Depth | `1000` | The maximum depth below the water level where the shoreline effect is applied |
| Shore Depth Cutoff | `1000` | Hard cutoff.   No shore effect is applied beyond this depth below the water level |

## Floating Island

An island floating in the air, tapering to a tip below it

| Property | Default | Description |
|----------|---------|-------------|
| Platform Depth | `5000` | How far the island extends down below the surface |
| Surface Z | `0` | The Z height of the island surface |
| Exp Strength | `2.0` | How sharply the underside tapers towards the tip |
| Tip Location Actor | *none* | Optional actor marking where the tip points.   Leave it empty to use the default |
| Curl Angle Per Meter | `1.5` | How much the island curls as it descends |
| Shape Search Expansion Amount | `2000` | How far the chunk search bounds are expanded to catch the curled shape |
