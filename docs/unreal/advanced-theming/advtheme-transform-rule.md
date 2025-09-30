---
title: "Transform Rule"
sidebar_position: 4
---

Dungeon Architect lets you specify offsets to your visual nodes to move/scale/rotate them from their relative marker locations.


![Static node Offset](../images/unreal/tutorial/G/G-offset.png)


However, if you want a more dynamic way of applying offsets (based on blueprint or C++ logic), you can do so with a *Transform Rule*.  This can be very useful to add variations to your levels for certain props


## Using Transform Rules
To assing an existing rule into the node, Check the **Use Transform Logic** property and select the rule you would like to attach to the node from the dropdown list


![Assign an existing Transform Rule](../images/unreal/tutorial/G/G-transform_rule_01b.png)

Create a new Transform rule by creating a new blueprint class derived from the appropriate DungeonTransformLogic.  It should match the builder you are targeting


![Create a new Selection Rule](../images/unreal/tutorial/G/G-transform_rule_01a.png)

Open up the blueprint and override the **Get Node Offset** function. This function will be called by the engine and the logic you put here will let you decide on the offset that needs to be applied on this node


![Override function to define logic](../images/unreal/tutorial/G/G-transform_rule_04.png)


## Example #1

In this example, a single rock mesh is randomly rotated, and slightly scaled and translated to give a nice cave like look


![Rocks randomly rotated, translated and scaled](../images/unreal/tutorial/G/G-transform_rule_eg1_1.jpg)

A different transformation rule is applied to ceiling stone meshes for more variations


![Transform rule applied to rock nodes](../images/unreal/tutorial/G/G-transform_rule_eg1_2.jpg)


![Cliff Random rotation rule](../images/unreal/tutorial/G/G-transform_rule_eg1_3.png)

## Example #2

Here is an example where alternate pipes are rotated by 180 degrees to give a visually appealing look


![Alternate meshes are rotated by 180 degrees](../images/unreal/tutorial/G/G-transform_rule_eg2_1.jpg)

This was done by rotating the mesh node by 180 degrees for every alternate cell (similar to the checker rule logic seen previously)


![Rule assignment](../images/unreal/tutorial/G/G-transform_rule_eg2_2.jpg)


## Example #3

In this example a small random rotation is applied to orange ground tiles.  Useful while creating ruins when laying down broken tile meshes


![Transform rule applied to orange ground meshes](../images/unreal/tutorial/G/G-vol_platform_04c.jpg)


![Transformation Rule Blueprint](../images/unreal/tutorial/G/G-transform_rule_eg3_1.png)
