---
title: "Voxel Worlds"
sidebar_position: 8
---

The voxel workflow carves your dungeon out of a solid voxel world instead of assembling it from modular meshes.
The layout your builder generates is used to cut caves, islands and tunnels out of a density field, which is
then meshed into geometry with full Nanite and Lumen support

This is configured on the Dungeon actor, not on the builder, so it works alongside whichever builder you are
using.   It is most often paired with the [Cell Flow builder](../cell-flow/cellflow-overview.md), whose organic
cell shapes suit carved geometry better than a tile grid

<iframe width="100%" height="540" loading="lazy" src="https://www.youtube.com/embed/KVH-zzC8TV4" frameborder="0" allowfullscreen></iframe>

## Enable It

Select your dungeon actor and check `Carve Voxels` in the `Voxel` category.   The mesh, noise and SDF model
settings below it become editable once it is on

Then assign a `Voxel SDF Model`.   This decides what kind of world you are carving out of

| Model | World |
|-------|-------|
| Cave | An underground cave system, with optional holes punched through the ceiling |
| Island | An island sitting in water, with a shoreline that slopes away from the land |
| Floating Island | An island floating in the air, tapering to a tip below it |

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

## Voxel Materials

| Property | Default | Description |
|----------|---------|-------------|
| UV Scale | `100` | UV scale for texture mapping.   Smaller values make the texture larger |

`Voxel Mesh Settings` is accessible from Blueprints, so you can change the voxel setup at runtime before
triggering a build

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

## Model Settings

### Cave

| Property | Default | Description |
|----------|---------|-------------|
| Ceiling Extra Height | `800` | Extra headroom added above the room height |
| Enable Ceiling Holes | `true` | Punches holes through the cave ceiling, letting light down into the rooms |
| Ceiling Hole Radius | `600` | The radius of a ceiling hole |
| Ceiling Hole Height Offset | `400` | How far above the ceiling the hole is centred |
| Max Ceiling Holes Per Room | `2` | The most holes a single room may get |
| Ceiling Hole Spawn Probability | `0.5` | The chance a room gets a ceiling hole at all |

### Island

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

### Floating Island

| Property | Default | Description |
|----------|---------|-------------|
| Platform Depth | `5000` | How far the island extends down below the surface |
| Surface Z | `0` | The Z height of the island surface |
| Exp Strength | `2.0` | How sharply the underside tapers towards the tip |
| Tip Location Actor | *none* | Optional actor marking where the tip points.   Leave it empty to use the default |
| Curl Angle Per Meter | `1.5` | How much the island curls as it descends |
| Shape Search Expansion Amount | `2000` | How far the chunk search bounds are expanded to catch the curled shape |

## Dedicated Servers and Headless Builds

Voxel density is generated on the GPU by default, which needs a renderer.   Dedicated servers, `-nullrhi` runs
and commandlets do not have one, so they automatically fall back to a CPU path that runs the same density
math.   The server therefore builds the same world as its clients, and no configuration is needed for this to
work

Two console variables let you override the path selection when you are debugging

| Console Variable | Default | Description |
|------------------|---------|-------------|
| `da.Voxel.UseGPU` | `-1` | Overrides the voxel density generation path.   `-1` uses the dungeon's setting, `0` forces CPU, `1` forces GPU.   Render-incapable targets always use the CPU path |
| `da.Voxel.CPUExactDensity` | `-1` | Chooses the CPU density evaluator.   `-1` is exact on render-incapable targets and coarse otherwise, `0` forces coarse, `1` forces exact, which matches the GPU shader math |

:::note
`da.Voxel.UseGPU 1` cannot force the GPU path on a target that has no renderer.   The fallback always wins
there, otherwise the build would fail outright
:::
