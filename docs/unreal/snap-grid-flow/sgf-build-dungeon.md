# Build Dungeon

It's time to use everything we've created to build a dungeon

## Create Theme file

Create an empty theme file somewhere in the content browser.  We'll visit this later to spawn items in our modules
(like NPCs, Spawners, Pickups, PlayerStart etc.)

![](../images/unreal/tutorial/J/J-94.jpg)

![](../images/unreal/tutorial/J/J-95.png)

## Setup Dungeon Actor

Create a new Level

![](../images/unreal/tutorial/J/J-96.png)

![](../images/unreal/tutorial/J/J-97.jpg)

Drop in a `Dungeon` actor

![](../images/unreal/tutorial/J/J-98.jpg)

Select the actor and reset the transform

Change the Builder type to `SnapGridFlowBuilder`

![](../images/unreal/tutorial/J/J-99.png)

Assign the `Module Database`, `Flow Graph` and `Theme` assets

![](../images/unreal/tutorial/J/J-100.png)

Click the `Build Dungeon` button

![](../images/unreal/tutorial/J/J-101.jpg)

![](../images/unreal/tutorial/J/J-102.jpg)

## Debug Draw

Select the `Dungeon` actor and enable `Debug Draw` to see the flow graph overlay on the world

![](../images/unreal/tutorial/J/J-103.png)

![](../images/unreal/tutorial/J/J-104.jpg)

![](../images/unreal/tutorial/J/J-105.jpg)

![](../images/unreal/tutorial/J/J-106.jpg)

## Save Map

We've set up our dungeon actor in this map. Save this map, we'll revisit this later
