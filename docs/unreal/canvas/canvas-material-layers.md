---
title: "Canvas Material Layers"
sidebar_position: 5
---

<show-structure />

## Edit Material layers

![image|635x396](../images/unreal/tutorial/Canvas/6ce468f51f7c20f1e823864df932c4f4a87fc81b.png)

Use effect layers to design the look and feel of your dungeon.  Select a layer,  and modify any of its properties to see it change in real time in the preview viewport

![image|553x500](../images/unreal/tutorial/Canvas/f2a7166ef4b9d9a8a360eadee2a3d508db7e6b7d.jpeg)

![image|343x500](../images/unreal/tutorial/Canvas/1b3cc67b16f7f524919b818390189d6caf1ad11c.png)

![image|485x500](../images/unreal/tutorial/Canvas/aa505420e93d7b80f9f3b598843f140c11404bff.jpeg)

## Custom Material Layer

The final material is composed by stacking the different material layers together

You can define your own material layers and use them with the system

Any parameters you've created inside these functions show up in the details panel, allowing you to adjust their values

Create a new material layer, these are standard unreal engine's material layer assets. Right click on the content browser and create a material layer

![C016.png](../images/unreal/tutorial/Canvas/C016.png)

For reference examples on creating your own material layer effects, navigate to:  `DungeonArchitect Content > Core/Features/DungeonCanvas/Materials/Layers/Functions/ML_IconOverlay.ML_IconOverlay`

![C017.png](../images/unreal/tutorial/Canvas/C017.png)

Use this material layer in the theme using a `Custom Material Layer`

![C015](../images/unreal/tutorial/Canvas/C015.jpg)

Assign your material layer in the details panel. Any parameters you've exposed on the material will show up in the details panel
