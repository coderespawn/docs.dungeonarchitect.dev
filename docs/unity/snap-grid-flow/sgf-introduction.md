# Snap Grid Flow Builder 

## Features

The **Snap Grid Flow Builder** allows you to stitch snap modules using a flow graph.  You can create many types of 
levels with this builder. Some examples include:
* FPS/TPS with multiple floors
* Side Scrollers
* Top-Down dungeon crawlers (like diablo)
* Cities (with custom road paths, subways etc)
* Race Tracks

Since this builder uses parts of the Snap builder and the Flow framework, you can do the following:
* As an artist, have complete control over the design of the individual snap rooms. 
  Use vertex painting, foliage, landscapes, custom gameplay elements etc. on your snap room modules
* Use the flow framework to design procedural layouts, leveraging all the existing features 
  like cyclic-paths, key-locks, one-ways doors, item spawners etc
* Use Level streaming to keep the framerate high, even with lots of dynamic lights


## 3D Flow Graph

You'll design the flow graph in a 3D Layout Grid 

![](../../../images/unity/tutorial/08/ut-08-01.png)

The snap rooms are required to be of a fixed size (that is chosen by you), so they all can fit nicely and
can be stitched inside the 3D grid. 

However, you may also design your snap rooms to span multiple nodes in the flow graph. The flow framework is smart enough to identify these rooms 
and use them appropriately in the flow graph:

![](../../../images/unity/tutorial/08/ut-08-02.png)



In this example, the goal room was designed to be 2x2x2 the size of the chunk.    The flow framework identified it and
created a larger node appropriately while building the flow graph 

![](../../../images/unity/tutorial/08/ut-08-03.png)



The flow framework will also read the available doors you've setup in your snap modules and use that configuration
to grow the graph. So you are free to leave out the doors that you don't want while designing your snap module

This means, you don't need to leave space for doors on each side of the room. You can safely 
wall them off with your art assets, and it won't grow from there

