---
title: Create a Grid Flow Dungeon
slug: /unity/grid-flow
sidebar_position: 2
---


The Grid Flow Builder offers a rich set of tools to control the flow of your dungeons and item placement

## Setup Dungeon Prefab

Create a new scene.  Navigate to ``Assets/DungeonArchitect/Prefabs`` and drop in the DungeonGridFlow prefab on to the scene

![](../images/unity/tutorial/04/ut-04-01.png)


Select the DungeonGridFlow game object you just dropped and reset the transform

![](../images/unity/tutorial/04/ut-04-02.png)


## Setup Parent Object

Create a new Parent object where all the spawned dungeon items will go in.

![](../images/unity/tutorial/04/ut-04-03.png)

Reset the parent object's transform and set it to static

![](../images/unity/tutorial/04/ut-04-04.png)


Assign the parent object

![](../images/unity/tutorial/04/ut-04-05.png)


This makes sure all the spawned dungeon objects are placed under this parent object


## Setup Theme

There's a theme available in the samples folder which we'll use for this tutorial section

Navigate to ``Assets\DungeonArchitect_Samples\DemoBuilder_GridFlow\Theme`` and assign the theme ``ThemePrehistoric`` to the DungeonGridFlow game object

![](../images/unity/tutorial/04/ut-04-06.png)


## Setup GridFlow Graph

This builder requires another asset called the `Grid Flow Graph`.   This is a graph that helps you  control the flow of your dungeon. In this section, we'll use an existing graph from the samples folder

Navigate to ``Assets\DungeonArchitect_Samples\DemoBuilder_GridFlow\FlowGraph`` and assign the graph ``DemoGridFlow`` to the `DungeonGridFlow` game object's ``Flow Asset`` property

![](../images/unity/tutorial/04/ut-04-07.png)



## Build Dungeon

Select the ``DungeonGridFlow`` game object and click ``Build Dungeon`` button from the inspector window

![GridFlow dungeon built using the Prehistoric theme](../images/unity/tutorial/04/ut-04-08.jpg)


![GridFlow dungeons support key-locks](../images/unity/tutorial/04/ut-04-09.jpg)


## Open Grid Flow Editor

Let's open the GridFlow asset in the editor:

Navigate to ``Assets\DungeonArchitect_Samples\DemoBuilder_GridFlow\FlowGraph`` and double click on ``DemoGridFlow``.

Dock the editor window so you see both the scene view and the grid flow editor

![](../images/unity/tutorial/04/ut-04-10.jpg)

Click the `Build` button on the top left of the flow editor to build a new dungeon in the Grid Flow Editor

![](../images/unity/tutorial/04/ut-04-11.png)

![](../images/unity/tutorial/04/ut-04-flow_editor_anim.gif)



## Link Editor with Dungeon

We are going to link up the dungeon we have on the scene (`DungeonGridFlow` game object) with the Grid Flow Editor so when we generate a new dungeon in the editor, it syncs up the dungeon on the scene


Click an empty space (grey area) in the Execution Graph

![Click anywhere in the empty area](../images/unity/tutorial/04/ut-04-12.png)


This will show up the execution graph properties in the Inspector window


![Execution Graph properties](../images/unity/tutorial/04/ut-04-13.png)


Assign the dungeon game object by dragging the DungeonGridFlow over

![](../images/unity/tutorial/04/ut-04-14.jpg)

Now build the dungeon again by clicking the `Build` button in the Execution Graph Window

![](../images/unity/tutorial/04/ut-04-11.png)


This will recreate the dungeon in the scene view.  The dungeon in the editor window is now synchronized with the dungeon in the scene view

If you double click on any of the tiles in the Tilemap window,  the scene view should focus on that tile/item


Double click on the Bonus Item (``B``) in the tilemap.


![](../images/unity/tutorial/04/ut-04-15.png)

The scene view should zoom in on the treasure chest

![](../images/unity/tutorial/04/ut-04-16.jpg)


## Explore Grid Flow Graph

After you've built a dungeon in the editor (by hitting the build button on the top left), you can select each node and see how the dungeon layout was built, as shown in the lower preview panels

![Select a node to preview the build process](../images/unity/tutorial/04/ut-04-flow_editor_node_preview.gif)
