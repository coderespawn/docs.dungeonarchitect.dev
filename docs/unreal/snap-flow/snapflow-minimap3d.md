---
title: "Snap Minimap 3D"
sidebar_position: 11
---

![image|690x454](../images/unreal/tutorial/D/1/D-1-8f0278d9a088df6a58af8ae227e906b4b2a04776.jpeg)

This post shows you how to create a 3D snap dungeon minimap.   You can create this preview dungeon in the same world (like a hologram sitting in some room), or in a separate world to render out in a render texture

To spawn a 3D minimap on the world, just call this function after your dungeon has been fully built:

![image|690x483](../images/unreal/tutorial/D/1/D-1-86244629e94a61dc3be0de8866d34a2956aa7cb4.png)

The parent actor node controls where you'd like to spawn this.    Update the scale, rotation and location accordingly

You can spawn this in an other world, and then render it out in a render texture for your HUD, if you specify the World input parameter (more on this later below).    Rendering it in another world means you don't have to worry about it getting in the way of your existing world geometry, and you can use a different lighting model in that world.

## Minimap Modules
You can render out your modules in a different theme.   Think of this as a simplified verison of each  module, as you wouldn't want detailed world geometry rendered here.     Here's I've specified `minimap` and in the module database, for each module entry, I've created a simplified module to be used with the minimap and registered it there

![image|348x500](../images/unreal/tutorial/D/1/D-1-b31aabde640ca4ca30f6be2e2369806d1c39fc8d.png)

This is how a minimap module looks like:

![image|690x366](../images/unreal/tutorial/D/1/D-1-ea06796b59b5d70a3ab13ed18c0ae4eefa0444b4.jpeg)

Notice it doesn't have connections defined.  Connections are not needed here, the minimap will be built based on the existing dungeon layout, so it should just match the base module's layout


## Minimap Connections

![image|520x473](../images/unreal/tutorial/D/1/D-1-9072850b897d2b2205a4e910c35dae65c1443630.png)

![image|382x500](../images/unreal/tutorial/D/1/D-1-7979e21d0c47c7a5d740534ab61746177aafba5d.jpeg)

![image|386x372](../images/unreal/tutorial/D/1/D-1-c0108c1199f22a33ecd29b19330b4dd34b26bd8a.jpeg)


The `Connection Marker Prefix` input in the `Build Snap Themed Dungeon` node lets you have a different door and wall meshes on your minimaps.   Specify a prefix here and it would look for this door in the Snap Connection's theme graph

So if you specify `Minimap`,   it would look for `MinimapDoor` instead of a `Door`.  It would do the same with `Wall`
