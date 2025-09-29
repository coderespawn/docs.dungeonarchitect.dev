# Build Dungeon

It's time to use everything we've created to build a dungeon

## Create Theme file

Create an empty theme file somewhere in the content browser.  We'll visit this later to spawn items in our modules
(like NPCs, Spawners, Pickups, PlayerStart etc.)

![](J-94.jpg)

![](J-95.png)

## Setup Dungeon Actor

Create a new Level

![](J-96.png)

![](J-97.jpg)

Drop in a `Dungeon` actor

![](J-98.jpg)

Select the actor and reset the transform

Change the Builder type to `SnapGridFlowBuilder`

![](J-99.png)

Assign the `Module Database`, `Flow Graph` and `Theme` assets

![](J-100.png)

Click the `Build Dungeon` button

![](J-101.jpg)

![](J-102.jpg)

## Debug Draw

Select the `Dungeon` actor and enable `Debug Draw` to see the flow graph overlay on the world

![](J-103.png)

![](J-104.jpg)

![](J-105.jpg)

![](J-106.jpg)

## Save Map

We've set up our dungeon actor in this map. Save this map, we'll revisit this later
