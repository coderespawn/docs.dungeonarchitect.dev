---
title: "Voxel Settings"
sidebar_position: 2
---

These live on the Dungeon actor, under the `Voxel` category, once `Carve Voxels` is enabled

## Voxel Mesh Settings

| Property | Default | Description |
|----------|---------|-------------|
| Voxel Size | `50` | The size of a single voxel in world units.   Smaller values give finer detail and cost more to generate |
| Voxel Chunk Size | `32` | How many voxels make up one chunk along each axis |
| Voxel Shape Theme | *none* | The theme asset used to dress the carved world |
| Enable Collision | `true` | Generates collision for the meshed chunks |
| Wall Thickness | `200` | Thickness of the walls generated from the layout outline |
| Use GPU | `true` | Generates the voxel density on the GPU using compute shaders.   Faster, but requires a renderer |
| Bake Collection Asset | *none* | Optional.   Assign a collection asset to bake the voxel chunks into static meshes in the editor |

:::note
The `Material` property is deprecated.   Use the `Voxel Shape Theme` and the material settings instead
:::

`Voxel Mesh Settings` is accessible from Blueprints, so you can change the voxel setup at runtime before
triggering a build

## Voxel Materials

| Property | Default | Description |
|----------|---------|-------------|
| UV Scale | `100` | UV scale for texture mapping.   Smaller values make the texture larger |

## Voxel Noise Settings

Noise is what makes the carved surfaces look eroded rather than perfectly smooth

| Property | Default | Description |
|----------|---------|-------------|
| Noise Scale | `1.0` | Scale of the noise pattern |
| Noise Amplitude | `350` | Maximum displacement the noise can apply |
| Noise Octaves | `4` | Number of octaves for the fractal noise.   More octaves add finer detail |
| Noise Offset | `(0, 0, 0)` | Base offset for noise sampling.   Change it to get a different pattern from the same settings |
| Noise Floor Scale | `0.3` | How much vertical noise is applied to floors.   `0` gives flat floors, `1` matches the walls |
| Noise Ceiling Scale | `1.0` | How much vertical noise is applied to ceilings.   `0` gives flat ceilings, `1` matches the walls |
| Noise Scale Vector | `(1, 1, 1)` | Per-axis scaling of the noise pattern.   Use it to stretch features along an axis |

Under Advanced you will also find `Floor Ceiling Transition Height` (the height at which noise switches from
the floor scaling to the ceiling scaling), `Noise Channel Separation` and `Use Per Axis Seeds`.   The defaults
are fine for most worlds
