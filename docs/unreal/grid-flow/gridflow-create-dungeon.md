# Create a Grid Flow Dungeon

The Grid Flow Builder offers a rich set of tools to control the flow of your dungeons and item placement


## Setup Dungeon Actor

Create a new Level and drop in a dungeon actor

![](A-02.jpg)


Inspect the properties of the dungeon actor you just dropped.   Set the `Builder Class` to ``GridFlowBuilder``

![](E-01.png)


## Setup Theme

Click the ``+`` icon next to the Themes array to create a new theme entry.

![](E-02A.png)

Here we'll assign an existing theme from the samples folder.  For this, we'll need to enable `Show Engine Content` and `Show Plugin Content` from the view options

![](E-02B.png)

![](E-02C.png)


We'll assign the theme ``T_DefaultGridFlow``.

![](E-03.png)


> The above theme file is under `Dungeon Architect Content > Builders > GridFlowContent > Theme` folder 
> 
> ![](E-04.png)


## Setup GridFlow Graph


This builder requires another asset called the `Grid Flow Graph`.   This is a graph that helps you  control the flow of your dungeon. In this section, we'll use an existing graph from the samples folder

Select the Dungeon actor and in the `Grid Flow` setting assign the following asset ``DefaultGridFlow``.  This is in the folder `Dungeon Architect Content > Builders > GridFlowContent > FlowGraph`

![](E-05.png)

![](E-06.png)

![](E-07.png)

## Build Dungeon

Select the Dungeon actor and click `Build Dungeon` button from the Details panel

![GridFlow dungeon built using the sample theme](E-09.jpg)

![GridFlow dungeons support key-locks](E-08.jpg)
   
