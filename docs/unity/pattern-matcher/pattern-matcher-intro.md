# Pattern Matcher - Basics

## Introduction

Capture patterns in your dungeon layout and add or remove markers around this pattern.    This is a powerful system for
decorating your themes, as you are no longer restricted to a single tile level decoration and can decorate across
multiple tiles using your own patterns


![Pattern Matcher](../images/unity/tutorial/16/ut-16-01.png)


## Create a Pattern Matcher asset

Create a new asset by right-clicking on the project window: `Create > Dungeon Architect > Theme Engine > Pattern Matcher`

![Pattern Matcher](../images/unity/tutorial/16/ut-16-02.png)


Double-click the asset to open up the Pattern Matcher editor

![Pattern Matcher](../images/unity/tutorial/16/ut-16-03.png)

![Pattern Matcher](../images/unity/tutorial/16/ut-16-04.png)

## Create your first Pattern

### Create a new Pattern

Start by adding a new pattern by clicking the `Add` button in the *Patterns* panel

![Pattern Matcher](../images/unity/tutorial/16/ut-16-05.png)

You can have multiple patterns, and they run in sequence one after the other

![Pattern Matcher](../images/unity/tutorial/16/ut-16-06.png)


### Pattern Rules

A pattern is formed by assembling various pattern rules together (think of them as blocks arranged in a certain way)

![Pattern Matcher](../images/unity/tutorial/16/ut-16-07.png)


Right click on an emtpy space and select `Add new Rule`

![Pattern Matcher](../images/unity/tutorial/16/ut-16-08.png)

This will create a new rule

![Pattern Matcher](../images/unity/tutorial/16/ut-16-09.png)


You can click and drag the rule to another location

![Pattern Matcher](../images/unity/tutorial/16/ut-16-10.png)

![Pattern Matcher](../images/unity/tutorial/16/ut-16-11.png)

![Pattern Matcher](../images/unity/tutorial/16/ut-16-12.png)


Move the rule to an tile position like shown below and select it

![Pattern Matcher](../images/unity/tutorial/16/ut-16-13.png)

### Pattern Rule Graph

Each Pattern rule block has a rule graph.  Here you define what needs to be present (or not present) at this location
for the pattern to match

The `Should Select?` node takes in the result of your condition (boolean).

Create a graph like this:

![](../images/unity/tutorial/16/ut-16-14.png)

The text in the rule block will update to reflect the rule graph condition

If the pattern is matched (i.e. the condition of every rule block succeeds), then the `On Selected` node
will fire on all the rule blocks. Use this node to either emit or remove markers at this block's location (more on this shortly)

Create a new rule node next to it as shown below. Place a similar constraint to make sure a ground marker exists in this location

![](../images/unity/tutorial/16/ut-16-15.png)

Our pattern will now match two adjacent ground blocks, and we can place a `1x2` Ground tile here

Whenever this pattern matches, it would fire off the `On Pattern Selected` node

Select any one of the two rule block and add a *Emit Marker* node with the name `Ground1x2` *(later, you'll need to adjust the mesh's offset transform accordingly depending on which block you chose)*

It should look like this:

![](../images/unity/tutorial/16/ut-16-16.png)

So, when the dungeon is created in the scene, this would create a marker named `Ground1x2` on all the
places where the pattern matched.   We'll need to switch back to the *Theme Graph* app mode, so we can add our art asset
under the `Ground1x2` marker

### Setup Theme

Let's clone a scene from the launchpad and set up our pattern matcher asset in it

Navigate to Main Menu: `Dungeon Architect > Launch Pad`

![](../images/unity/tutorial/16/ut-16-17.png)

Clone a Candy Grid builder theme.   Navigate to the `Samples`, scroll down to the *Grid* category and clone the `Demo`
scene as shown below

![](../images/unity/tutorial/16/ut-16-18.jpg)

![](../images/unity/tutorial/16/ut-16-19.jpg)


Select the dungeon game object and assign our pattern matcher asset to it

![](../images/unity/tutorial/16/ut-16-20.png)


## Add Marker Node

Open up the theme file linked to this dungeon and create a new marker node named `Ground1x2`   

![](../images/unity/tutorial/16/ut-16-21.png)

![](../images/unity/tutorial/16/ut-16-22.png)


Add this prefab under the `Ground1x2` marker node: `/Game/Geometry/Meshes/1M_Cube_Chamfer`

![](../images/unity/tutorial/16/ut-16-23.png)

![](../images/unity/tutorial/16/ut-16-24.jpg)


We want to scale the cube along X axis by 2 units nudge it to the right (since this is a wide tile and is spawned on one of the tile)

![](../images/unity/tutorial/16/ut-16-25.png)

![](../images/unity/tutorial/16/ut-16-26.png)

![](../images/unity/tutorial/16/ut-16-27.png)

![](../images/unity/tutorial/16/ut-16-28.png)

![](../images/unity/tutorial/16/ut-16-29.png)

Select the Cube mesh node in the theme graph and set the following transform:

![](../images/unity/tutorial/16/ut-16-30.png)


The result looks like this:

![](../images/unity/tutorial/16/ut-16-31.jpg)


It has inserted our wide tiles, however there are overlaps.

## Avoid Overlaps

Since we are emitting a marker in the left rule block (blue),  the system already knows that there might be something
spawned at that location, and it will try not to overlap it when searching for this pattern through the scene.

![](../images/unity/tutorial/16/ut-16-25.png)

However, it does now know that the art asset you plan to insert here would take up 2 tiles and the block on the right (pink)
would also be occupied.    To let the system know this, select the block on the right (pink) and check
`Hint Will Insert Asset Here`

![](../images/unity/tutorial/16/ut-16-32.png)

The tiles no longer overlap

![](../images/unity/tutorial/16/ut-16-33.jpg)

## Remove Markers

Since we are inserting a 2-wide ground tile, we don't need the `Ground` marker in its place as it's redundant.

Select each of the two rule blocks and add a `Remove Marker` node with the value `Ground` like shown below

![](../images/unity/tutorial/16/ut-16-34.png)

![](../images/unity/tutorial/16/ut-16-35.png)


## Cleanup

Just for consistency, let's update the Candy theme's ground tile to have the same art asset.  We've removed
the default ground mesh node and replaced it with a new mesh node that has the same chamfered gray cube (scaled to `4x1x4` since it takes up a single tile)

Before:

![](../images/unity/tutorial/16/ut-16-36.jpg)

![](../images/unity/tutorial/16/ut-16-37.jpg)

## Same Height Constraint

We have a problem in some locations. We don't want ground tiles in adjacent locations to be merged if they are in different heights

![](../images/unity/tutorial/16/ut-16-38.jpg)

To fix this, select the pattern and have a look at the details panel

Add an entry to the `Same Height Markers` list named `Ground`.  This will match the pattern where all the entries in this list are in the same height

![](../images/unity/tutorial/16/ut-16-39.png)

![](../images/unity/tutorial/16/ut-16-40.jpg)

## Probability

Change the layer's probability field to a value between 0 and 1 (i.e. 0% to 100%).  Setting this to 0.5 would insert our wide tiles 50% of the time

**Before (with 100% probability):**

![](../images/unity/tutorial/16/ut-16-41.png)

![](../images/unity/tutorial/16/ut-16-42.jpg)

**After (with 50% probability):**

![](../images/unity/tutorial/16/ut-16-44.png)

![](../images/unity/tutorial/16/ut-16-43.jpg)


## Extend further

Another pattern was added for 2x2 tiles with a probability of 0.5 (and moved up to the first entry)

![](../images/unity/tutorial/16/ut-16-45.png)

![](../images/unity/tutorial/16/ut-16-47.png)

![](../images/unity/tutorial/16/ut-16-46.jpg)


> You can do a lot more with the system. More examples will be added to this section soon
