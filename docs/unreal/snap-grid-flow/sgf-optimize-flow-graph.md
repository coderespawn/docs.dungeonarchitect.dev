---
title: Optimize Flow Graph
---

In this section, we'll use the Performance Analyzer to identify and improve the performance of our graph

## Performance Analyzer

![](J-149.png)

Find bottlenecks in your dungeon graph designs and optimize them using the Performance Analyzer. It shows how many attempts were made to build the dungeon.

It is normal for a dungeon to make multiple attempts before converging to a solution. However, if your dungeon design doesn't provide good opportunities for it to converge, they would show up here and you can fix them


## Run Performance Analyzer

Open up our flow graph editor and reassign the Module database in the Editor Settings, as we've done previously

![](J-73.jpg)


Please the Play button on the `Performance Stats` window

![](J-148.png)

![](J-150.png)

We are running 300 test cases, where we generate random dungeons with current graph setup.    Each test case will 
take a certain number of retries before converging to a solution

The number of retries is represented in the X-axis.  The number of test cases is represented in Y-axis

We want to reduce the number of retries our graph takes (so it generates them faster).  We have quite a few test cases
taking more than 10 retries (orange), and some taking more than 30 retries (red)

## Optimize Graph

### Lift Modules
Looking at the generated graph, one possible reason is the graph doesn't have much opportunity to grow to other floors
(and hence utilize the free nodes) because the lift module design is very constrained.  It has to enter and exit 
from the same side. 

![](J-83.jpg)

We'll fix that by adding 3 more lift modules where the top exit is from the other 3 directions

#### Existing Lift Module:

The existing lift module we created in the previous section enters and exits from the same side

![](J-151.jpg)


#### New Lift Modules:

Create 3 new Lift Modules which exit from the other 3 directions like shown below:

![](J-152.jpg)

![](J-153.jpg)

![](J-154.jpg)

This gives the layout graph more opportunities to grow

#### Register the new Modules

Open up the Module database editor and add the three entries 

![](J-88.png)

![](J-155.png)

Rebuild the Module cache and save the module database

![](J-45.png)


#### Test Performance

Run the performance analyzer again



