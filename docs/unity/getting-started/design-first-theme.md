---
title: Design your first Theme
---

A theme file is a mapping between **marker** names (like Walls, Ground, Door etc) and the meshes that you provide.    The prefabs you map here will be used to build your dungeon

![](../images/unity/tutorial/02/ut-02-theme_editor_preview.jpg)

In the previous section, we created a dungeon with an existing theme file (CandyDungeonTheme).  In this section, we'll create one ourselves

## Create a Theme File

Create a new theme file from either the Main menu or the Create menu

![Create from Main menu](../images/unity/tutorial/02/ut-02-create_theme_01.png)

![Create from Create menu](../images/unity/tutorial/02/ut-02-create_theme_02.png)


This will create a theme file in the current open directory in the Projects window

![](../images/unity/tutorial/02/ut-02-03.png)


## Open the Theme File

Double-click the theme file to open the **Theme Editor**.  Dock the theme editor so you can see both the Scene view and the Theme Editor at the same time

![](../images/unity/tutorial/02/ut-02-04.jpg)
## Assign the Theme File

Destroy the existing dungeon by selecting ``DungeonGrid`` game object and click ``Destroy Dungeon`` button


Assign the theme file that you just created, on to the DungeonGrid game object

![](../images/unity/tutorial/02/ut-02-05.png)


Click ``Build Dungeon`` and nothing should appear.   That's because we haven't added prefab mappings on the theme yet



## Design the Theme

Navigate to ``Assets\DungeonArchitect_Samples\Demo_Theme_Candy\Prefabs``.  This folder contains a set of mesh prefabs we can use for our dungeon

![](../images/unity/tutorial/02/ut-02-06.jpg)

### Add Ground

Drag-drop the ground prefab mesh on to the Theme Editor

![](../images/unity/tutorial/02/ut-02-07.jpg)


Link up the mesh node with the ``Ground`` marker node.  When you do, you should see a live preview on the scene view with the dungeon using this ground mesh

![](../images/unity/tutorial/02/ut-02-08.jpg)

For the live preview to work, make sure the "Realtime Update" button is enabled in the Theme Editor

![](../images/unity/tutorial/02/ut-02-09.png)

Another criteria for the live preview to work is that a dungeon in the scene should reference the theme that is currently being edited in the theme editor

### Adjust Object Transform

Dungeon Architect can adapt to any modular asset.   In our example, the dungeon's grid size is set to `(4, 2, 4)`.  The ground prefab that we used has the same size (`4x4`) and the pivot is in the center.  So it will fit nicely without any change

![](../images/unity/tutorial/02/ut-02-37.png)

![](../images/unity/tutorial/02/ut-02-38.png)


However, this might not always be the case.  Your prefabs might have its pivot in a different position (like in the corner) and the size may be different than the grid size we've defined in the dungeon game object.

Here's an example of a modular ground prefab from one of the Synty asset.  

![](../images/unity/tutorial/02/ut-02-39.png)

The Pivot is in the corner and the size of the tile is `5x5` units

If we were to drop this in the theme editor and link it to the ground marker, we'd see this

![](../images/unity/tutorial/02/ut-02-40.jpg)

The tiles overlap since the asset is bigger than the grid size (we chose the grid size to be 4 and the asset size is 5)

Select the mesh node and set the scale to `0.8` *(since 4/5 = 0.8)*


![](../images/unity/tutorial/02/ut-02-42.png)

![](../images/unity/tutorial/02/ut-02-41.jpg)

Now we need to align the position.    Click `Visualize Markers` from the theme editor's toolbar

![](../images/unity/tutorial/02/ut-02-43.png)

Select the ground prefab node or the `Ground` marker node to visualize the correct position of where your meshes should be

![](../images/unity/tutorial/02/ut-02-44.jpg)

Use a corner as a reference for alignment, like in the image above

We'll move it along `X` by `-2` and see where it goes


![](../images/unity/tutorial/02/ut-02-46.png)

![](../images/unity/tutorial/02/ut-02-45.jpg)


That doesn't seem right. Move the `X` along `2` instead and it fits correctly along the x-axis

![](../images/unity/tutorial/02/ut-02-47.png)

![](../images/unity/tutorial/02/ut-02-48.jpg)

Move along `Z` by `2` units to bring it to the correct position

![](../images/unity/tutorial/02/ut-02-50.png)

![](../images/unity/tutorial/02/ut-02-49.jpg)


### Marker Visualizer

As we've seen in the previous section,  the theme editor's *Marker Visualizer* is a useful feature while designing your dungeons.   It will show the alignment guides whenever you select a built-in marker node (like Ground, Wall etc) or any node connected underneath it

Turn it on from the Theme Editor's toolbar and select a built-in marker node or any node underneath it to visualize that marker's expected alignment

![](../images/unity/tutorial/02/ut-02-43.png)

![](../images/unity/tutorial/02/ut-02-51.jpg)

![](../images/unity/tutorial/02/ut-02-52.jpg)

![](../images/unity/tutorial/02/ut-02-53.jpg)

![](../images/unity/tutorial/02/ut-02-54.jpg)


### Add More Prefabs

Go ahead and add prefabs under the following markers: **Wall**, **Fence** and **Door**

![](../images/unity/tutorial/02/ut-02-10.jpg)


![](../images/unity/tutorial/02/ut-02-11.jpg)


### Add Wall Pillars

Drag drop the ``Pillar2`` prefab to the theme editor and link it to the ``WallSeparator`` marker node

![](../images/unity/tutorial/02/ut-02-12.jpg)

We'll need to make this pillar a bit bigger. Select the node you just dropped and modify the Scale parameter under Offset category

![](../images/unity/tutorial/02/ut-02-13.jpg)

![](../images/unity/tutorial/02/ut-02-14.jpg)


### Add Windows
We have two wall meshes in the samples folder

![](../images/unity/tutorial/02/ut-02-15.jpg)

The other one (``Wall2``) has a window. Lets configure the theme to sometimes use this second mesh so we have windows

Drag drop ``Wall2`` prefab on to the theme editor and place it **before** (left of) the existing wall prefab node

![](../images/unity/tutorial/02/ut-02-16.jpg)


When you connect this to the ``Wall`` marker node, you'll notice it has picked up the window node for all the walls

![](../images/unity/tutorial/02/ut-02-17.jpg)


This is because Dungeon Architect starts executing the nodes from left to right. When the condition was satisfied to pick the first node, it stopped execution and never came to the second node.

There are multiple ways you can control this condition, the simplest being adjusting the probablity of selection.

Select the node you just dropped and change the probability to ``0.5`` (this would mean it gets selected 50% of the time).  The other 50% of the time, it would not be selected and the execution would then move to the next node, and hence selecting the non-windowed wall node

![](../images/unity/tutorial/02/ut-02-18.png)

![Half the walls have windows](../images/unity/tutorial/02/ut-02-19.jpg)


### Add Wall Decorations

There's a photo frame prefab we'd like to attach to every wall

![](../images/unity/tutorial/02/ut-02-20.jpg)

Drag drop this prefab to the theme editor **before** the two existing nodes and link it to the ``Wall`` marker node

![](../images/unity/tutorial/02/ut-02-21.jpg)


This will cause all the walls to disappear and be replaced with this photo frame

![](../images/unity/tutorial/02/ut-02-22.jpg)

This is because once the photo frame was selected, the execution stopped and the the wall nodes further down the line were not executed.

Select the photo frame and uncheck the flag "Consume on Attach".  This will cause the execution to continue further even though this node was selected by the theming engine


![](../images/unity/tutorial/02/ut-02-23.jpg)


Lets adjust the offset of the photo frame (position and rotation) to make it properly align with the inner walls

Select the photo frame node and change the position to ``(0, 2, -0.22)`` and rotation to ``(0, 180, 0)``

![](../images/unity/tutorial/02/ut-02-24.png)


The photo frame is aligned with the walls

![](../images/unity/tutorial/02/ut-02-25.jpg)


### Marker Emitters

We have an issue with the photo frames. They also spawn near windows

![](../images/unity/tutorial/02/ut-02-26.jpg)


``Marker Emitters`` allow you to emit marker names from any of your dropped prefab nodes.  This means, we can define a new marker node (e.g. ``MyWallDeco``) and then emit that marker from the wall node that doesn't have a window (``Wall1`` prefab).  All our wall decorations can now go under this ``MyWallDeco`` marker and it will show up only near solid walls


Right click on an empty area in the theme editor and select ``Add Marker Node``

![](../images/unity/tutorial/02/ut-02-27.png)


Select the node and change its name to ``MyWallDeco``


![](../images/unity/tutorial/02/ut-02-28.png)


Break the link to the photo frame

![](../images/unity/tutorial/02/ut-02-29.png)


Connect this under ``MyWallDeco`` marker node.  All the future wall decorations can also go under this marker

![](../images/unity/tutorial/02/ut-02-30.png)


Now emit this marker from the wall node that doesn't contain a window

Drag a link out of the bottom of the solid wall prefab node and release the mouse in an empty area


![](../images/unity/tutorial/02/ut-02-31.png)


![](../images/unity/tutorial/02/ut-02-32.png)


You can follow the same method to create another type of decoration (e.g. MyWindowDeco) and emit it from under the windowed wall node. In this example, I've added a flower pot in the windows

![](../images/unity/tutorial/02/ut-02-33.jpg)

### Recap
In this section we learnt the following:

* *Probablity* - Controls the percentage chance of a node being selected.  A value of 1 means 100% selection chance. A value of 0.25 means 25% selection chance
* *Execution Order* - The theme engine executes all the nodes under a marker node from left to right. If it selects a certain node, it stops executing, unless the ``Consume on Attach`` flag is unchecked
* *Marker Emitters* - You can create complex hierarchies with your own marker nodes, giving you more freedom to decorate your dungeons
 
 





