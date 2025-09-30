---
title: Item Spawn Listener
sidebar_position: 4
---

*Item Spawn Listeners* get notified of every game object that is spawned by the theme engine.    This allows you to modify the spawned objects and perform post processing on them (e.g. set metadata, add / remove extra components etc)


You'll need to inherit from `DungeonItemSpawnListener` and implement the following function

```c#
void SetMetadata(GameObject dungeonItem, DungeonNodeSpawnData spawnData) 
```

Then add this script to the dungeon game object

```c#
using DungeonArchitect;
using UnityEngine;

public class FlowItemMetadataHandler : DungeonItemSpawnListener
{
    public override void SetMetadata(GameObject dungeonItem, DungeonNodeSpawnData spawnData)
    {
        if (dungeonItem != null)
        {
            dungeonItem.AddComponent<...>();
        }
    }
}
```
