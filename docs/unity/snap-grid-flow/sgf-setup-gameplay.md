---
title: Setup Gameplay
---

We want to be able to open locked doors after we've picked up the keys.   For this to happen, we need to implement 
a few things: 
* Pick up the keys when we touch them and place it in our inventory
* When we get close to a locked door blueprint, check the keys in our inventory and find out if any one of them 
  can open it
* A UI to show the keys in our inventory
  
## Player Inventory

You may create your inventory in any way you like.  A simple inventory is implemented for the sample character

Check the `Inventory` class in this path: `Assets\CodeRespawn\DungeonArchitect_Samples\DemoBuilder_GridFlow\Scripts\DemoGame\Inventory\Inventory.cs`

It contains four inventory slots. Each inventory slot contains an item id and a preview texture to show the item in the UI

There's also a `PickableItem` class in this path: `Assets\CodeRespawn\DungeonArchitect_Samples\DemoBuilder_GridFlow\Scripts\DemoGame\Inventory\PickableItem.cs`

## Pickable Item

If there's an object that you'd the player to pick (e.g. keys), add a `PickableItem` component to it.    Whenever a gameobject with an inventory touches this object (e.g. a player), it would add the item id to the next free slot of the inventory and destroy the pickable object

This is how the keys get added to the inventory and disappear when you touch them

Pickable items have an icon texture that you specify in your prefabs.  This texture is added to the inventory slot so it can be shown in the inventory UI

## Locked Doors

You are free to implement this in any way you like.  A sample is provided in `LockedDoor.cs` file here: 
`Assets\CodeRespawn\DungeonArchitect_Samples\DemoBuilder_GridFlow\Scripts\DemoGame\Door\LockedDoor.cs`

When Dungeon Architect spawns the Key and Locked Door prefabs, it will automatically insert a `FlowItemMetadataComponent` to it with the item id. This component will also contain referenced item ids.    A key item will reference the lock item and vice versa.    So if you are reading a locked door item metadata, the reference item ids will contain a list of key ids that can open this lock

Key Metadata:

![](../../../images/unity/tutorial/12/ut-12-01.jpg)
  
Lock Metadata:

![](../../../images/unity/tutorial/12/ut-12-02.jpg)

Notice how the key references the lock id and the lock references the key id

This component was added automatically by the flow framework when the dungeon was built


When ever we pick a key, the key item ids are added to our inventory.   When a player enters the trigger volume of a locked door, we simply check if the inventory contiains any of the key ids that this lock can open

```c#
bool CanOpenDoor(Collider other)
{
    var inventory = other.gameObject.GetComponentInChildren<Inventory>();
    if (inventory != null)
    {
        // Check if any of the valid keys are present in the inventory of the collided object
        foreach (var validKey in validKeys)
        {
            if (inventory.ContainsItem(validKey))
            {
                return true;
            }
        }
    }
    return false;
}
```




