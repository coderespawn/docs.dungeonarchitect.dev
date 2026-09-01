---
title: "Canvas Player Setup"
sidebar_position: 3
---

<show-structure />

You'll need a custom player controller to do two things:
* Show your UI with the minimap widget
* Add a component to this class, so it automatically takes care of setting everything up for you

> Note: Check the canvas samples for reference: `Dungeon Architect Content > Showcase > Samples > Features > Canvas > CanvasExamples`

## Add Components

### Dungeon Actor

Select the Dungeon Actor in the scene and add the `DungeonCanvas` component to it

![C002B.png](../images/unreal/tutorial/Canvas/C002B.png)

### Player Pawn

Open your player pawn and add the `Dungeon Canvas Item` component to it.  This gives the pawn an icon on the
map, and reveals the fog of war around it as it moves

Set `Item Type` to `Player` and check `Explore Fog Of War`

| Property | Default | Description |
|----------|---------|-------------|
| Icon Name | *empty* | The icon drawn for this item.  Maps to the icon list registered in the canvas theme asset |
| Item Type | `World Object` | `Player` entries follow the fog of war share mode set on the canvas component.  `World Object` entries ignore it - visible to everyone when no team is set, or only to their team otherwise |
| Explore Fog Of War | `false` | Reveals the fog of war around this item.  Enable it on player pawns, and on world objects that light up the map like a shrine or a watch tower |
| Fog Of War Explorer Enabled | `true` | Turns the exploration on and off at runtime, e.g. keep a shrine's explorer disabled until the shrine is activated.  Mark the component as replicated if you toggle it on the server |
| Fog Of War Settings | | How far the item reveals the map and how soft the shadow edges are.  See [Fog of War & Multiplayer](canvas-fog-of-war.md) |
| Team Id | `-1` | The team this item belongs to.  `-1` means no team |
| Orient To Rotation | `false` | Rotates the icon to match the actor's rotation |
| Occludes Fog Of War | `false` | Blocks fog of war reveal, so this item casts a shadow on the map |
| Hide When Out Of Sight | `false` | Hides the icon when the item is not currently visible |
| Z Order | `0` | Higher numbers draw on top when icons overlap.  Bump the player icon up (e.g. `1000`) to keep it above everything else |

![C002.png](../images/unreal/tutorial/Canvas/C002.png)

The same component works on any actor, not just the player pawn - see
[Fog of War & Multiplayer](canvas-fog-of-war.md) for world object explorers, teams and how exploration is
shared between players

:::note
Older projects added a `DungeonCanvasPlayerController` component to the player controller instead.  That
component still works but is deprecated, and shows up in the editor as
`Dungeon Canvas Player Controller Component (Deprecated)`.  The Canvas Item component replaces it, works on any
actor rather than just the possessed pawn, and supports multiplayer
:::

## Show UI

Open your player controller and create your UI widget and add to viewport

![image|690x289](../images/unreal/tutorial/Canvas/583839d36fe04688000534c8bbaaa9baba664ee0.png)

This will make the UI show up when your game starts. The Dungeon Canvas widget you placed in your UI will auto register itself when it constructs. So there's no more setup required here on the UI side

