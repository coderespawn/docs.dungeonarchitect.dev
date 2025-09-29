---
title: Create Flow Graph
---

Design the layout of your procedural dungeons using the flow editor.   Then create an infinite number of 
procedural dungeons that follow this layout rule.

Create cyclic-paths, key-locks, teleporters, shops, treasure rooms, boss rooms and much more

## Create a Snap Grid Flow Asset

Move to an appropriate folder and create a new `Snap Grid Flow Graph` asset from the Create Menu

`Create > Dungeon Architect > Snap Grid Flow Builder > Snap Grid Flow Graph`

![](../images/unity/tutorial/09/ut-09-05.png)
   
![](../images/unity/tutorial/09/ut-09-06.png)

Double click the asset to open up the flow graph editor

![](../images/unity/tutorial/09/ut-09-07.jpg)

The top panel is the Exection Flow Graph where you would be designing your dungeon flow.    The resulting layout graph is shown in the 3D viewport below

### 3D Viewport Navigation

The navigation is similar to what you'd expect from Unity's scene view

* Hold right mouse button and move to look around.
* Hold right mouse button and WASD to move
* Hold right mouse button and Q to move up, E to move down

## Create Grid

Right click on the execution graph and add a `Create Grid` node from the context menu

`Layout Graph > Create Grid`

![](../images/unity/tutorial/09/ut-09-08.png)

![](../images/unity/tutorial/09/ut-09-09.png)

Link the `Create Grid` node to the `Result` node

![](../images/unity/tutorial/09/ut-09-10.png)

> To create a link, hover the mouse pointer over the border of the `Create Grid` node until it turns yellow. Then drag a link out of it and attach it to the border of the `Result` node

Hit the `Build` button in the Execution Graph Panel

![](../images/unity/tutorial/09/ut-09-11.png)

Move around in the 3D viewport and should should see a faint set of dots that represent the initial grid that this node has created.    This is our work area and our dungeon layout will grow in it

![](../images/unity/tutorial/09/ut-09-12.png)


Select the `Create Grid` node and inspect the properties

![](../images/unity/tutorial/09/ut-09-13.png)

You may adjust the size of your initial work area here.  

There are a few things to consider when choosing the size of your grid
* Larger initial grids will require more processing power.  
* Sometimes, it's better to have a smaller grid so it creates a nice tightly packed layout.  
* However if the grid is too small, the paths will not have any room to grow

You should come back to this node and adjust it as needed.  For now, we'll leave it to default

## Create Main Path

Add a `Create Main Path` node

`Layout Graph > Create Main Path`

![](../images/unity/tutorial/09/ut-09-14.png)

![](../images/unity/tutorial/09/ut-09-15.png)

Break the previous connection we made to the result node and link it like this

![](../images/unity/tutorial/09/ut-09-16.png)

> To break the link, hover the mouse over the `Create Grid` node's border till it turns yellow. Then right click

Hit build

![](../images/unity/tutorial/09/ut-09-17.png)

Keep hitting build for different results

### More Viewport Controls

* Hold Alt + Hold Left Mouse button + Move mouse to orbit around the selected nodes
* Press `F` key to focus on the active nodes and reset the orbit pivot

![](../images/unity/tutorial/09/ut-09-18.gif)

### Main Path Properties

Select the `Create Main Path` node and inspect the properties

![](../images/unity/tutorial/09/ut-09-19.png)


Parameter                | Description
------------------------ | -------------------------
Path Size                | Control the size of the path with the variable
Path Name                | Each path in the flow system can be later referenced using its path name.   The name of this path is set to `main`
Snap Module Categories   | When you registered a room in the module database, you specified a category (which defaulted to `Room`).   This allows you to control the module prefabs that would be used from that list to stitch the path
Node Color               | Adjust the preview color of the nodes created in this path
Start/End Marker Names   | These values allow you to insert your prefabs into the start / end rooms using the theme engine. More on this later
Start/End Node Path Name | Override the path name of the first and the last node in the path.  This allows you to give a unique path name to your spawn room and goal room
Position Constraints     | Control the position of the nodes in the path with your own scripts and rules. More on this in the later sections
Snap Module Constraints  | Override the snap modules for any of the nodes in the path with your own scripts and rules. More on this in the later sections


We'll leave all the properties unchanged for now

## Create Alternate Path

Add a node `Create Path` and connect it as below


![](../images/unity/tutorial/09/ut-09-20.png)

![](../images/unity/tutorial/09/ut-09-22.png)


Select the node and inspect the properties

![](../images/unity/tutorial/09/ut-09-23.png)

Build the graph, and you'll see a new branch (orange) emitting out of the main branch (green) 

![](../images/unity/tutorial/09/ut-09-21.png)


This new orange path branched out of the main (green) path because we have configured it to do so by setting the 
`Start from Path` parameter to `main`

We would like to have this new path merge back into the main path.   Set the `End on Path` parameter to `main`.   We also want to reference this new path as `alt`

![](../images/unity/tutorial/09/ut-09-24.png)


Control the size of the path with the `Min/Max Path Size` parameter

Add a description to this node

![](../images/unity/tutorial/09/ut-09-25.png)

![](../images/unity/tutorial/09/ut-09-26.png)

> It's a good practice to add description to your nodes, as it becomes easier to manage them when you graph grows bigger

## Create Another Path

We'll create another path originating from the 'alt' path and merging back into the 'main' path

![](../images/unity/tutorial/09/ut-09-28.png)

![](../images/unity/tutorial/09/ut-09-29.png)

The path originates out of the `alt` path (orange) and merges beack into the `main` path (green)

![](../images/unity/tutorial/09/ut-09-27.png)

## Assign Module Database

The flow editor doesn't have a module database assigned, so it doesn't really know how our modules look like

Let's assign the module database in the editor settings, so it creates a layout graph compatible with how we've set up
the modules

Click an empty area in the Execution Flow Graph to view the editor properties

![](../images/unity/tutorial/09/ut-09-30.png)


Property                 | Description
------------------------ | -------------------------
Randomize Seed           | Randomize the layout everytime you build
Seed                     | The current seed that was used to build the dungeon
Module Database          | Specify a module database asset to build the flow graph compatible with the regsitered module prefabs
Auto Focus Viewport      | Whenever you select a node in the execution graph, the camera auto-focuses on all the active nodes.  Uncheck to disable this


Assign the module database we created earlier

![](../images/unity/tutorial/09/ut-09-31.png)


Rebuild and have a look at the layout graph now  

![](../images/unity/tutorial/09/ut-09-32.png)


You'll notice that the flow graph is built on a single floor, which is consistent with the way we've designed our
registered modules.   We have designed a room which, although it goes out in the four horizontal directions, there's 
no way of moving up or down.   

> If your build fails, make sure you've compiled your module database and saved the asset

## Create a Lift Module

Let's create a module that lets us move to another floor

### Design Lift Module

Create a new module as we've done in the previous [Modules](sgf-modules.md) section 

1. Switch to a new scene and create a new game object and name it `Module_Lift`

   ![](../images/unity/tutorial/09/ut-09-34.png)

2. Reset the transform

   ![](../images/unity/tutorial/09/ut-09-33.png)

3. Add a `Snap Grid Flow Module` component and assign the module bounds asset

   ![](../images/unity/tutorial/09/ut-09-35.png)

   You should see the bounds of the module
   
   ![](../images/unity/tutorial/09/ut-09-36.jpg)

4. We want the module to span two node vertically

   Set the Num Chunks parameter to `(1, 2, 1)`

   ![](../images/unity/tutorial/09/ut-09-38.png)

   ![](../images/unity/tutorial/09/ut-09-37.jpg)

5. Go ahead and design your lift module in any way you like.  Leave two openings on the same side of the room, one below and another on top

   ![](../images/unity/tutorial/09/ut-09-39.jpg)

6. Drop in two snap connection prefabs and make sure they are facing outwards.   Align them correctly using the `Grid and Snap` window

   ![](../images/unity/tutorial/09/ut-09-40.jpg)

   ![](../images/unity/tutorial/09/ut-09-41.jpg)


7. Make sure all the objects that make up this room are inside the module game object

   ![](../images/unity/tutorial/09/ut-09-42.png)

8. Save this module lift as a prefab

   ![](../images/unity/tutorial/09/ut-09-43.png)

9. Delete the Module_Lift game object from the scene as we no longer need it

   ![](../images/unity/tutorial/09/ut-09-44.png)

### Register Lift Module

Register this module in the Module database.   Select the module database asset and in the properties, register our new lift module

![](../images/unity/tutorial/09/ut-09-45.png)
   
![](../images/unity/tutorial/09/ut-09-46.png)


Since we've modified the module database, hit `Compile Module Database` and save the asset

![](../images/unity/tutorial/09/ut-09-47.png)


Open up our flow graph editor and reassign the Module database in the Editor Settings, as we've done previously

![](../images/unity/tutorial/09/ut-09-48.png)


Click build and now, the flow graph uses the new lift module to move to other floors

![](../images/unity/tutorial/09/ut-09-49.png)

![](../images/unity/tutorial/09/ut-09-50.gif)

Notice how the links enter and exit out of the same side, since this is how we've set it up in our module design

![](../images/unity/tutorial/09/ut-09-51.png)


### Adjust Selection Probability

We don't want the lift to show up too often. Open up the Module database and set the selection weight to `0.1` 
on the lift module entry

![](../images/unity/tutorial/09/ut-09-54.png)

Before `(with selection weight 1.0)`:

![](../images/unity/tutorial/09/ut-09-52.png)


After `(with selection weight 0.1)`:

![](../images/unity/tutorial/09/ut-09-53.png)



## Create a Goal Room

We'll create a large `2x2x2` room for the boss fight and register it under the category `Boss`.

### Design the Goal Room Prefab

1. Open a new empty scene, create an empty game object and name it `Room_BossFight`
 
  ![](../images/unity/tutorial/09/ut-09-55.png)

2. Reset the transform

  ![](../images/unity/tutorial/09/ut-09-56.png)

3. Add a `Snap Grid Flow Module` component and set the num chunks to `(2, 2, 2)`

  ![](../images/unity/tutorial/09/ut-09-57.png)

4. Assign the module bounds

  ![](../images/unity/tutorial/09/ut-09-58.png)

  You should now see a the bounds visuals in the scene view.    You have a large area to design your boss fight arena

  ![](../images/unity/tutorial/09/ut-09-59.jpg)

5. Design the module in any way you like.

  ![](../images/unity/tutorial/09/ut-09-60.jpg)

  In our example, we'll keep only one opening on the top floor, and the player falls down to the arena to fight the boss

6. Add the snap module near the opening and snap it to the correct position

  ![](../images/unity/tutorial/09/ut-09-61.jpg)


7. Make sure all your objects are inside the module prefab

  ![](../images/unity/tutorial/09/ut-09-62.png)

8. Turn this into a prefab

  ![](../images/unity/tutorial/09/ut-09-63.png)

9. Delete the module game object from the scene

  ![](../images/unity/tutorial/09/ut-09-64.png)

### Register the Module

Register this module in the `Module Database` with the category `Boss`

  ![](../images/unity/tutorial/09/ut-09-65.png)

Make sure the following parameters are set

Parameter        | Value
---------------- | ----------
Module Prefab    | Room_BossFight
Category         | Boss
Selection Weight | 1


Since we've modified the module database, hit `Compile Module Database` and save the asset

![](../images/unity/tutorial/09/ut-09-47.png)


Open up our flow graph editor and reassign the Module database in the Editor Settings, as we've done previously

![](../images/unity/tutorial/09/ut-09-48.png)

Select the `Create Main Path` node and inspect the properties in the Details panel

![](../images/unity/tutorial/09/ut-09-67.png)

![](../images/unity/tutorial/09/ut-09-66.png)


Change the `Category Constraint Mode` to `Start End Node`

This allows you to override the category of the start and the end nodes.   

![](../images/unity/tutorial/09/ut-09-68.png)

This will force the flow system to pick up modules that are registered under the `Boss` category.   We previously registered our boss room with this category

> You can have more than one module registered under the same category.   For example, you may have 3 boss rooms registered in the module database under the category `Boss` and it would randomly pick one while building it

Build the flow graph and have a look at the layout graph

![](../images/unity/tutorial/09/ut-09-69.png)


The last node in the main path has a size of `2x2x2` to accommodate our goal module. It also enters from the correct position


## Create More Room Modules

Add a few more `Room` modules of size `2x1x1` and `2x1x2`

![](../images/unity/tutorial/09/ut-09-92.jpg)

![](../images/unity/tutorial/09/ut-09-93.jpg)

Register them with the module database under the category `Room` and click `Compile Module Database`.  Adjust their weights to control how often they appear

Rebuild the flow graph

![](../images/unity/tutorial/09/ut-09-94.png)

