---
title: "Grid Flow Editor"
sidebar_position: 3
---

Let's open the GridFlow asset in the editor:

Navigate to ``Dungeon Architect Content > Core > Runtime > Builders > GridFlowContent > FlowGraph`` and double click on ``DefaultGridFlow``

This will open the `Grid Flow Editor`

![Grid Flow Editor](../images/unreal/tutorial/E/E-10.jpg)

Click the Build button toolbar to build the graph

![](../images/unreal/tutorial/E/E-11.png)

![](../images/unreal/tutorial/E/E-12.jpg)


Keep hitting build to get a new dungeon

![](../images/unreal/tutorial/E/E-13.gif)

> Click the image to play


### Explore Grid Flow Graph

After you've built a dungeon in the editor (by hitting the `Build` button on the toolbar), you can select each node in the execution graph and see how the dungeon layout was built, as shown in the lower preview panels

![Select an execution graph node to preview the build process](../images/unreal/tutorial/E/E-15.gif)

> Click the image to play

## Editor Panels

The Grid Flow Editor has the following panels

### Execution Graph Panel

This is where you design the flow of your dungeon. All other panels are for previewing the result of this panel

![](../images/unreal/tutorial/E/E-14A.jpg)


### Layout Graph Panel

The initial level is designed in a higher level layout graph

![](../images/unreal/tutorial/E/E-14B.jpg)


### Tilemap Panel

The result of the layout graph is eventually transferred over to a tilemap. The resulting tilemap is previewed here

![](../images/unreal/tutorial/E/E-14C.jpg)

### Preview Viewport Panel

The 3D representation of the final Dungeon

![](../images/unreal/tutorial/E/E-14D.jpg)
