---
title: "Mini-Map"
sidebar_position: 6
---

Grid Flow dungeons draw their minimap through the Dungeon Canvas framework, like every other builder

:::note
The old minimap framework this page used to describe - the `Grid Flow Mini Map` actor and the
`DungeonMiniMapTrackedObject` component - was removed in version `2.32.0` and replaced by Dungeon Canvas.
Existing assets are redirected automatically, so `DungeonMiniMapTrackedObject` becomes a
`Dungeon Canvas Item` component when you open an older level
:::

## Setup

Add a `Dungeon Canvas` component to your Dungeon actor, then follow the Canvas documentation

* [Canvas Overview](../canvas/canvas-overview.md) - what the framework does and how the pieces fit together
* [Player Setup](../canvas/canvas-player-setup.md) - getting the map on screen and revealing fog of war
* [UI Widget](../canvas/canvas-ui-widget.md) - the interactive widget with pan and zoom
* [Canvas Theme](../canvas/canvas-theme.md) - designing how the map looks

## Tracked Objects

To show an object on the map, add a `Dungeon Canvas Item` component to it.   This is also what lets an actor
reveal the fog of war around itself
