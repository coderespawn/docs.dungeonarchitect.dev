---
title: "Pattern Matcher - Getting Started"
sidebar_position: 2
---

Capture patterns in your dungeon layout and add or remove markers around this pattern.    This is a powerful system for 
decorating your themes, as you are no longer restricted to a single tile level decoration and can decorate across 
multiple tiles using your own patterns


![Pattern Matcher](../images/unreal/tutorial/P/P-01.jpg)


## Switch to Pattern Matcher Mode

Open an existing theme file. On the top right, you'll find two tabs for the different app modes in the theme editor
* Theme Graph
* Pattern Matcher

![](../images/unreal/tutorial/P/P-02.jpg)


Click the `Pattern Matcher` button to switch to the Pattern Matcher App Mode

![](../images/unreal/tutorial/P/P-03.png)


This will change the layout of the theme editor. You can switch between the two modes at any time without losing data

![](../images/unreal/tutorial/P/P-04.jpg)


## Create your first Pattern

### Create a new Pattern

Start by adding a new pattern by clicking the `Add` button in the *Patterns* panel

![](../images/unreal/tutorial/P/P-05.png)

You can have multiple patterns, and they run in sequence one after the other


![](../images/unreal/tutorial/P/P-06.jpg)


### Pattern Rules

A pattern is formed by assembling various pattern rules together (think of them as blocks arranged in a certain way)

![](../images/unreal/tutorial/P/P-08.jpg)


Right click on an emtpy space and select `Add new Rule`

![](../images/unreal/tutorial/P/P-07.jpg)

This will create a new rule

![](../images/unreal/tutorial/P/P-09.jpg)

You can click and drag the rule to another location

![](../images/unreal/tutorial/P/P-10.jpg)

![](../images/unreal/tutorial/P/P-11.jpg)


Move the rule to an tile position like shown below and select it

![](../images/unreal/tutorial/P/P-12.jpg)

### Pattern Rule Graph

Each Pattern rule block has a rule graph.  Here you define what needs to be present (or not present) at this location 
for the pattern to match

The `Selection Condition` node takes in the result of your condition (boolean).  

Create a graph like this:

![](../images/unreal/tutorial/P/P-13.jpg)

The text in the rule block will update to reflect the rule graph condition

If the pattern is matched (i.e. the condition of every rule block succeeds), then the `On Pattern Selected` node
will fire on all the rule blocks. Use this node to either emit or remove markers at this block's location (more on this shortly)

Create a new rule node next to it as shown below. Place a similar constraint to make sure a ground marker exists in this location

![](../images/unreal/tutorial/P/P-14.jpg)

Our pattern will now match two adjacent ground blocks, and we can place a `1x2` Ground tile here

Whenever this pattern matches, it would fire off the `On Pattern Selected` node

Select any one of the two rule block and add a *Emit Marker* node with the name `Ground1x2` *(later, you'll need to adjust the mesh's offset transform accordingly depending on which block you chose)*

It should look like this:

![](../images/unreal/tutorial/P/P-15.jpg)

So, when the dungeon is created in the scene, this would create a marker named `Ground1x2` on all the 
places where the pattern matched.   We'll need to switch back to the *Theme Graph* app mode, so we can add our art asset 
under the `Ground1x2` marker

## Add Marker Node

In the top right corner of the editor, click the `Theme Graph` tab

![](../images/unreal/tutorial/P/P-17.png)

Create a new marker node and rename it to `Ground1x2`

![](../images/unreal/tutorial/P/P-18.png)

![](../images/unreal/tutorial/P/P-19.png)


Add this mesh under the `Ground1x2` marker node: `/Game/Geometry/Meshes/1M_Cube_Chamfer` (available when you add starter content)

![](../images/unreal/tutorial/P/P-20.jpg)

We want to scale the cube along X axis by 2 units nudge it to the right (since this is a wide tile and is spawned on one of the tile)

![](../images/unreal/tutorial/P/P-21.jpg)

![](../images/unreal/tutorial/P/P-22.png)

![](../images/unreal/tutorial/P/P-23.png)

![](../images/unreal/tutorial/P/P-24.png)

Select the Cube mesh node in the theme graph and set the following transform:

![](../images/unreal/tutorial/P/P-26.png)

The result looks like this:

![](../images/unreal/tutorial/P/P-25.jpg)

It has inserted our wide tiles, however there are overlaps.

## Avoid Overlaps

Since we are emitting a marker in the left rule block (orange),  the system already knows that there might be something
spawned at that location, and it will try not to overlap it when searching for this pattern through the scene.

![](../images/unreal/tutorial/P/P-27.jpg)

However, it does now know that the art asset you plan to insert here would take up 2 tiles and the block on the right (green)
would also be occupied.    To let the system know this, select the block on the right (green) and check 
`Hint Will Insert Asset Here`

![](../images/unreal/tutorial/P/P-28.jpg)


The tiles no longer overlap

![](../images/unreal/tutorial/P/P-29.jpg)

## Remove Markers

Since we are inserting a 2-wide ground tile, we don't need the `Ground` marker in its place as it's redundant. 

Select each of the two rule blocks and add a `Remove Marker` node with the value `Ground` like shown below

![](../images/unreal/tutorial/P/P-31.jpg)

![](../images/unreal/tutorial/P/P-32.jpg)

## Cleanup

Just for consistency, let's update the Candy theme's ground tile to have the same art asset.  We've removed
the default ground mesh node and replaced it with a new mesh node that has the same chamfered gray cube (scaled to 4x4x1 since it takes up a single tile)

Before:

![](../images/unreal/tutorial/P/P-33.jpg)

![](../images/unreal/tutorial/P/P-34.jpg)

## Same Height Constraint

We have a problem in some locations. We don't want ground tiles in adjacent locations to be merged if they are in different heights

![](../images/unreal/tutorial/P/P-35.jpg)

To fix this, select the pattern and have a look at the details panel

![](../images/unreal/tutorial/P/P-36.png)

Add an entry to the `Same Height Markers` list named `Ground`.  This will match the pattern where all the entries in this list are in the same height

![](../images/unreal/tutorial/P/P-37.png)

![](../images/unreal/tutorial/P/P-38.jpg)
