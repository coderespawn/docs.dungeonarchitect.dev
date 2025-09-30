---
title: Finalize Graph
sidebar_position: 10
---

The final node of your flow graph design should always be the `Finalize Graph` node.  This node does the following:
* Strategically promote some doors to `one-way` doors.  This is done to keep the player from bypassing locked doors
  by entering from another nearby door. This may also be done to keep the player from entering another 
  path from the opposite direction. It will always create a playable level
* Remove unused links from the layout graph 

## Add Finalize Node

Open the flow graph we designed earlier and add a `Finalize Graph` node


![](../images/unity/tutorial/11/ut-11-79.png)


Link it before the `Result` node as shown below

![](../images/unity/tutorial/11/ut-11-78.png)

Build the graph and have a look at the layout graph

![](../images/unity/tutorial/11/ut-11-80.png)

The orange double head arrows indicate one-way doors

We have already specified a one-way door asset in the snap connection prefab [previously](sgf-connections.md#setup-one-way-door-asset)

![](../images/unity/tutorial/08/ut-08-45.png)

This one-way door prefab will be used in those locations

## Build the dungeon

Open the scene where we previously [set up](sgf-build-dungeon.md) our dungeon.  Rebuild the dungeon

You should see one-way doors spawn where needed

![](../images/unity/tutorial/11/ut-11-81.jpg)

![](../images/unity/tutorial/11/ut-11-82.jpg)

---

We have now created a fully playable level and this wraps up our dungeon flow design.  Feel free to add more path or play around
with your own design

In the next section, we'll look at how to set up gameplay where we will build a random dungeon at runtime, 
move the player to the spawn room and have the player character (first person, third person etc) move around the map,
pick up keys, open locked doors and more
