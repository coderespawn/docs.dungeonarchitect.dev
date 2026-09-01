---
title: "Multiplayer Sample"
sidebar_position: 2
---

A complete networked sample built on the build system - server browser, lobby, synced minimap preview and
late-join support

Open it from `Dungeon Architect Content > Showcase > Samples > Games > Multiplayer` and start with
`1_MainMenuMap_StartHere`

<iframe
    width="100%"
    height="540"
    src="https://www.youtube.com/embed/_lh0cydS-cI"
    frameBorder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowFullScreen
/>

## What it demonstrates

The hard part of a networked dungeon is that every client has to end up with the same level, without shipping
the geometry over the wire.   The build system solves this by replicating the seed and having each client build
locally from it, then holding the match until everyone is done

The sample shows that whole sequence end to end

* A server browser and lobby, with the host able to randomize the seed and every client seeing the new layout
  preview in real time
* The dungeon built on the server and on each client from the same seed
* Players held in spectator mode while their local build runs, then spawned in once it completes
* Clients joining late, catching up to the dungeon that is already running

The session management and lobby code is provided as a reference implementation - it is there to be read and
copied from, not to be shipped as is

## Seed Control

The sample deliberately leaves `Randomize Seed On Build` off and sets the seed itself from Blueprints, because
the host needs to choose the seed in the lobby and share it before anyone builds.   This is the case the
[build system settings](build-system-overview.md) refers to when it suggests keeping that flag off if you want
to control the seed yourself

## Related

The lobby's map preview uses the Canvas widget - see [Canvas Minimaps](../canvas/canvas-overview.md).   Building
only up to the layout phase, so a preview can be shown without spawning any meshes, is done with the
`BuildDungeonWithSettings` node

In the match itself, who sees whose fog of war exploration on the minimap is controlled by the canvas
share mode - see [Fog of War & Multiplayer](../canvas/canvas-fog-of-war.md)
