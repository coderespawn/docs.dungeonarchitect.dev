---
title: "Dedicated Servers"
sidebar_position: 4
---

Voxel density is generated on the GPU by default, which needs a renderer.   Dedicated servers, `-nullrhi` runs
and commandlets do not have one, so they automatically fall back to a CPU path that runs the same density
math.   The server therefore builds the same world as its clients, and no configuration is needed for this to
work

## Console Variables

Two console variables let you override the path selection when you are debugging

| Console Variable | Default | Description |
|------------------|---------|-------------|
| `da.Voxel.UseGPU` | `-1` | Overrides the voxel density generation path.   `-1` uses the dungeon's setting, `0` forces CPU, `1` forces GPU.   Render-incapable targets always use the CPU path |
| `da.Voxel.CPUExactDensity` | `-1` | Chooses the CPU density evaluator.   `-1` is exact on render-incapable targets and coarse otherwise, `0` forces coarse, `1` forces exact, which matches the GPU shader math |

:::note
`da.Voxel.UseGPU 1` cannot force the GPU path on a target that has no renderer.   The fallback always wins
there, otherwise the build would fail outright
:::
