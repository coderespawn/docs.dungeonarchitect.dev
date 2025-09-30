---
title: "Custom Snap Bound Shapes"
sidebar_position: 10
---

Define snap module bounds using custom shapes. This opens up lots of possibilities for snap map based dungeons. 
In the previous examples, the doors were aligned at the edges of the axis-aligned bounding box. Now you can place the
doors at any orientation, at the edge of your custom polygon shape and create a more tightly packed and organic looking level

We'll look at setting up custom bounds shapes (like boxes, cylinders or polygon) in your module level file

![sb_01|637x500](../images/unreal/tutorial/D/0/D-0-f01d6112f05c5eaa55bd2163f63e8e437a13ed50.jpeg)

![sb02|690x447](../images/unreal/tutorial/D/0/D-0-d5afa159571018d4f4b84a7b812f4717b9515ce0.jpeg)

![sb03|690x340](../images/unreal/tutorial/D/0/D-0-4634760cc37d668c40ca04b2da85236b7c81aa37.jpeg)



---

Open up a snap module that you designed

![image|690x465](../images/unreal/tutorial/D/0/D-0-f7dafc5d03b787a11e9017b58e4c69fd10d61eeb.jpeg)

Drop in a `Snap Map Module Bounds` actor on to the scene. You can have as many of these actors as you like in the module to cover the bounds

![image|508x259](../images/unreal/tutorial/D/0/D-0-9d093fd8c79db03467b66101c0b21b1a153c133b.png)

![image|689x490](../images/unreal/tutorial/D/0/D-0-5580c1e139bad07ed4128e9c8f14047a0030d96e.jpeg)

## Circle Shape
By default, it's set to a polygon.   Lets change it to a circle

![image|564x500](../images/unreal/tutorial/D/0/D-0-052aed1dd74eedee989c948bd63977b842e80884.png)

![image|601x499](../images/unreal/tutorial/D/0/D-0-58cdac8d6fde680f7004f8025a6f9807bfca8559.jpeg)

Move the bounds accordingly.

![image|657x500](../images/unreal/tutorial/D/0/D-0-653edf4582b8ff25450cf1c019db44187cc756c3.jpeg)

Grab the radius handle and adjust the radius

![image|639x500](../images/unreal/tutorial/D/0/D-0-c1a0bc6a03dc41784b61803b53459558c9f3fd75.jpeg)

Adjust the height with the height handle

![image|690x397](../images/unreal/tutorial/D/0/D-0-de296da6c63cefc1d4d2a8a16aa5b7b709d7939c.jpeg)

## Box Shape

Add another bounds and set the shape to Box this time.   Adjust it so it aligns on one of the door opening

![image|565x500](../images/unreal/tutorial/D/0/D-0-1b24f621c12edb3f5cbefa01ddf6ab580541b9c6.jpeg)

Do the same of the other 2 doors

![image|634x500](../images/unreal/tutorial/D/0/D-0-b00f0ddaf59f34cf3d376ef1af0516795151a55c.jpeg)


> IMPORTANT: After you modify the bounds, it's important that you rebuild the [Module database cache](https://docs.dungeonarchitect.dev/unreal/snap-flow/register-modules)


## Polygon Shape

![image|690x478](../images/unreal/tutorial/D/0/D-0-6c79843a8dded09a8682f510028ab5d354e886ad.jpeg)

Use the polygon shape to wrap your dungeon bounds using a polygon.   The polygon should not self intersect. If it does, the system will ignore the bounds, since the shape is invalid and the bounds would not be shown

![](../images/unreal/tutorial/D/0/D-0-650b2238aba617257acdf21852ce4f40acf7e976.gif)

> Click the image to play

It would show a dashed border like this:

![image|560x500](../images/unreal/tutorial/D/0/D-0-9357aa4aff9eda7474e6d13dafbbd32f69da5007.jpeg)


You can provide a concave polygon and DA will automateically split it into several convex shapes (so collision check is faster)

## Final Notes
You don't have to go very agressive with this, just have a general bounds that cover everything and it might be ok to leave out some small stuff.   The goal of these bounds is to make sure other modules do not overlap with whatever is inside this.   Try to not have too many of these shapes as it would increase the time required to check for collision

## Sample Scene

Download: [SnapMap_Bounds_Demo.zip](https://forums.dungeonarchitect.dev/uploads/short-url/sf8NJecgYZEbK6XS9Lt6e6hMCfo.zip) (101.2 KB)


Extract and copy the folder to your Content folder. It should look like this:

![image|690x265](../images/unreal/tutorial/D/0/D-0-eab0368195af8794da5d58410d672dd5210e380a.png)
