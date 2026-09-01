---
title: "Design your first Theme"
sidebar_position: 3
---

A theme file lets you map the different assets (meshes, blueprints, lights etc) used to populate your dungeon.

<iframe
    width="100%"
    height="540"
    src="https://www.youtube.com/embed/rzY768vzmz8"
    frameBorder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowFullScreen
/>

![](../images/unreal/tutorial/B/B-01.jpg)

When a dungeon is built, it does not spawn any meshes.  Instead, it scatters invisible points called `Markers` all around the
map (e.g. `Wall`, `Ground`, `Door` etc.) where ever they are expected.

![](../images/unreal/tutorial/B/B-02.jpg)

The theme engine then runs and spawns any meshes/blueprints you specify under these markers
   
In the previous section, we created a dungeon with an existing theme file.  In this section, we'll create one ourselves

## Create a Theme File

Right click on the `Content Browser` and choose ``Dungeon Theme``

![](../images/unreal/tutorial/B/B-03.png)

This will create the Dungeon Theme asset.  Double click it to open the Theme Editor

![](../images/unreal/tutorial/B/B-03A.png)
   
![](../images/unreal/tutorial/B/B-04.jpg)



## Assign Grid Size

We'll use modular assets to populate our dungeon. As with any modular assets, they need to have a consistent size, so 
they all fit together nicely.    You'll specify the grid size in the dungeon properties.

With the theme editor open,  click on an empty area of the graph and inspect the details panel

The default grid size is `(400, 400, 200)`.  Leave this to the default for now, but you'll need to set this to the size
of the modular art asset being used in the theme

![](../images/unreal/tutorial/B/B-04B.png)

:::note
If you change this, you'll need to set this in the level editor's dungeon actor properties as well while building the dungeon
:::



## Use Sample Assets

In the `Content Browser`, [enable plugin contents](create-first-dungeon.md#show-plugin-content), so we can use sample meshes that come with the plugin to design our theme

:::note
You can use any asset you like, but for this tutorial, lets stick with the sample assets
:::
	

   

Navigate to ``Dungeon Architect Content > Showcase > Samples > Themes > Candy > Meshes``.  This folder contains a set of meshes we can use for our dungeon


![](../images/unreal/tutorial/B/B-07.jpg)

   
## Add Ground Mesh

Drag-drop the ground mesh on to the Theme Editor

![](../images/unreal/tutorial/B/B-08.jpg)

   
Link up the mesh node with the ``Ground`` marker node.  When you do, you should see a live preview on theme editor's Preview Viewport window

![](../images/unreal/tutorial/B/B-09.jpg)

![](../images/unreal/tutorial/B/B-10.jpg)


## Add More Meshes

Go ahead and add more meshes under the following markers: **Wall**, **Fence** and **Door**

![](../images/unreal/tutorial/B/B-11.jpg)

![](../images/unreal/tutorial/B/B-12.jpg)


## Add Wall Pillars

Drag drop the ``Pillar2`` mesh to the theme editor and link it to the ``WallSeparator`` marker node

![](../images/unreal/tutorial/B/B-13.jpg)

![](../images/unreal/tutorial/B/B-14.jpg)


We'll need to make this pillar a bit bigger. Select the node you just dropped and modify the Scale parameter under Offset category

![](../images/unreal/tutorial/B/B-15.jpg)
   

The live preview should update automatically to show the new scaled pillars

![](../images/unreal/tutorial/B/B-16.jpg)


## Add Windows

We have two wall meshes in the samples folder

![](../images/unreal/tutorial/B/B-17.jpg)


The other one (``Wall2``) has a window. Lets configure the theme to sometimes use this second mesh, so we can have some windows

Drag drop ``Wall2`` mesh on to the theme editor and place it **before** (left of) the existing wall mesh node

![](../images/unreal/tutorial/B/B-18A.jpg)

Link them up. The execution index should get updated, indicating their execution order

![](../images/unreal/tutorial/B/B-19.jpg)


Notice that the first node has been picked up and all the walls have been replaced with the windowed version

![](../images/unreal/tutorial/B/B-20.jpg)


This is because Dungeon Architect starts executing the nodes from left to right. When the condition was satisfied to pick the first node, it stopped execution and never came to the second node. 

There are multiple ways you can control this condition, the simplest being adjusting the probablity of selection.

Select the node you just dropped and change the probability to ``0.5`` (this would mean it gets selected 50% of the time).  The other 50% of the time, it would not be selected and the execution would then move to the next node, and hence selecting the non-windowed wall node


![](../images/unreal/tutorial/B/B-21.jpg)
   
![Half the walls now have windows](../images/unreal/tutorial/B/B-22.jpg)


## Add Wall Decorations

There's a photo frame mesh we'd like to attach to every wall.  Drag drop this mesh to the theme editor **before** the two existing wall nodes and link it to the ``Wall`` marker node

![](../images/unreal/tutorial/B/B-23.jpg)
   

This will cause all the walls to disappear and be replaced with this photo frame

![](../images/unreal/tutorial/B/B-24.jpg)
   
This is because once the photo frame node was selected, the execution stopped there and the wall nodes further down the line were not executed.    

Selected the photo frame and uncheck the flag "Consume on Attach".  This will cause the execution to continue further even though this node was selected by the theming engine


![](../images/unreal/tutorial/B/B-25.png)
   
![](../images/unreal/tutorial/B/B-26.jpg)
   

Lets adjust the offset of the photo frame (position and rotation) to make it properly align with the inner walls

Select the photo frame node and change the Offset's **Position** to ``(0, -22, 200)`` and **Rotation** to ``(0, 0, 180)``

![](../images/unreal/tutorial/B/B-27.png)
   

The photo frame is aligned now with the walls correctly

![](../images/unreal/tutorial/B/B-28.jpg)
   

## Marker Emitters

We have an issue with the photo frames. They also spawn near windows

![](../images/unreal/tutorial/B/B-29.jpg)
   


``Marker Emitters`` allow you to emit marker names from any of your dropped mesh nodes.  This means, we can define a new marker node (e.g. ``MyWallDeco``) and then emit that marker from the wall node that doesn't have a window (``Wall1`` mesh).  All our wall decorations can now go under this ``MyWallDeco`` marker and it will show up only near solid walls


Right click on an empty area in the theme editor and select ``Add Marker Node``

![](../images/unreal/tutorial/B/B-30.png)
   

Select the newly created marker node and change its name to ``MyWallDeco``

![](../images/unreal/tutorial/B/B-31.png)
   

Break the link to the photo frame

![](../images/unreal/tutorial/B/B-32.png)
   

Connect this under ``MyWallDeco`` marker node.  All the future wall decorations can also go under this marker

![](../images/unreal/tutorial/B/B-33.jpg)
   
   
Now emit this marker from the wall node that doesn't contain a window

Drag a link out of the bottom of the solid wall mesh node and release the mouse in an empty area

![](../images/unreal/tutorial/B/B-34.jpg)
   
Expand the category ``Marker Emitter``  in the context menu and select ``MyWallDeco``

![](../images/unreal/tutorial/B/B-35.jpg)


![](../images/unreal/tutorial/B/B-36.jpg)


This will cause the marker named ``MyWallDeco`` to be emitted in the scene whenever the solid wall node is selected, in which case it would then process the nodes defined under it.    Now our decorations don't show up near windows

![](../images/unreal/tutorial/B/B-37.jpg)


You can follow the same method to create another type of decoration (e.g. MyWindowDeco) and emit it from under the windowed wall node. In this example, I've added a flower pot in the windows

![](../images/unreal/tutorial/B/B-38.jpg)
   
![](../images/unreal/tutorial/B/B-39.jpg)

## Recap
In this section we learnt the following:

* *Probablity* - Controls the percentage chance of a node being selected.  A value of 1 means 100% selection chance. A value of 0.25 means 25% selection chance
* *Execution Order* - The theme engine executes all the nodes under a marker node from left to right. If it selects a certain node, it stops executing, unless the ``Consume on Attach`` flag is unchecked
* *Marker Emitters* - You can create complex hierarchies with your own marker nodes, giving you more freedom to decorate your dungeons
