---
title: "PCG Framework Overview"
sidebar_position: 2
---

In this tutorial, we'll have a look at the PCG framework and how it's used in the [Electric Dreams](https://www.unrealengine.com/en-US/electric-dreams-environment) sample

![](../images/unreal/tutorial/PCG/01/PCG-01-c476df127f68bad541d87afc4f459bd4612f4ad5.jpeg)

## Install

Download and Install the [Electric Dreams](https://unrealengine.com/marketplace/en-US/product/electric-dreams-env) sample from the marketplace

### Boost your framerate with DLSS plugin [Optional]
This is a resource intensive sample.  If you have an RTX card, you can boost your framerate by 2x or even 4x using DLSS and FrameGen.   The NVIDIA DLSS plugin is currently unavailable for 5.3, however, I have instructions on setting this up for 5.3.

If the DLSS plugin is still unavialable for 5.3 while you're reading this, follow [these instructions](https://forums.dungeonarchitect.dev/t/compile-nvidia-dlss-plugin-for-5-3/42) to install DLSS in 5.3

## Setup

Load up the editor and create a new open world scene

![image|536x450](../images/unreal/tutorial/PCG/01/PCG-01-16b7144edbea7f876acf5ff908a1686b0b7a5ebe.png)

## Forest PCG Graph

Navigate to `Content/PCG/Graphs/Forest`.   There's you'll find a PCG Graph asset `PCGDemo_Forest`.  Drag-Drop that on to the scene

![image|469x500](../images/unreal/tutorial/PCG/01/PCG-01-808e3f68de566ccd4eef133a1069588a1c86f2df.jpeg)

When you drag-drop a PCG graph asset on to the scene ,the editor would spawn a PCG Volume and set this asset in that volume.  Then it run this graph inside the volume and we get a nice forest

![image|690x374](../images/unreal/tutorial/PCG/01/PCG-01-2f2d5875d79fa174176eb4658a684dc44e4b657f.jpeg)

Select the PCG volume and increase the bounds of the volume to create a larger forest

![image|522x380](../images/unreal/tutorial/PCG/01/PCG-01-5a94f74a579d411c8a0be24e480c64b658004b72.png)

![image|690x274, 100%](../images/unreal/tutorial/PCG/01/PCG-01-79a653ff6a843f3ca8277e9284c2772158c7d687.jpeg)

![image|690x291](../images/unreal/tutorial/PCG/01/PCG-01-9066cc34f97b40f19abbe5bdca321d681b261d82.jpeg)

Select the PCG volume actor and click `Cleanup` to remove all spawned meshes.   This is important if you are iterating and need to a clean rebuild.  Click `Generate` to rerun the PCG graph and recreate the forest

![image|690x402](../images/unreal/tutorial/PCG/01/PCG-01-53c33fe371c16149c2f371f629ac12eb24b254b7.png)

## Ditch PCG Blueprint

Cleanup the Forest PCG volume so the scene is empty.

Drag-drop the ditch blueprint `PCGDemo_DitchBP` on to the scene.    You don't see much

![image|458x500](../images/unreal/tutorial/PCG/01/PCG-01-d6a91255ccebaf44755aee0dd54a20de0cf79c9a.jpeg)

This is a blueprint with a spline component.   The ditch assets are spawned along the spline and this logic is invoked from within the blueprint.    Select the dropped-in actor and hit `Clean Regen`

![image|690x387](../images/unreal/tutorial/PCG/01/PCG-01-e6abfd6f7e229ff83d747fa6230c04d433340706.jpeg)

![image|690x451](../images/unreal/tutorial/PCG/01/PCG-01-e3a23c890f4a1fb09e43fbe3d3ca5260e6866885.jpeg)

#### Regen / Cleanup

Notice that we don't have any buttons to destroy this from the scene,  only the `Clean Reg` button (i.e. clean+build).

Lets add a cleanup button.  Open up the blueprint `PCGDemo_DitchBP `

You'll notice that these 3 buttons are just blueprint functions with their `Call In Editor` flag checked

![image|690x454](../images/unreal/tutorial/PCG/01/PCG-01-24982a5e330a3dfa3f8ccceea7c9190a81eb5d5e.png)

Duplicate the `CleanReg` function and name it `Cleanup`

![image|441x380](../images/unreal/tutorial/PCG/01/PCG-01-4bceaed5d75354e999e63b9666839fa0f379cdd3.png)

Open up the newly created `Cleanup` function. We just want Cleanup here and no Generate.    So get rid of Generate. Also make sure `Call In Editor` is checked.   It should look like this.

![image|690x295](../images/unreal/tutorial/PCG/01/PCG-01-9074d89cb3780b3d6ddb4d7655da2bd6e2b19245.png)

Compile and save, switch back to the level editor, select the ditch blueprint actor and you should see a button to cleanup

![image|276x111](../images/unreal/tutorial/PCG/01/PCG-01-cf40f171cc1f7955173bf0d91db499c3d3db4b71.png)

#### Ditch Spline

The ditch blueprint has a spline.  Select the actor in the level editor and select the Spline component

![image|690x367](../images/unreal/tutorial/PCG/01/PCG-01-4bf0f43c40166bbe83c9a2e9be40a3eb81db59fa.jpeg)


If you don't see the spline after selecting the spline component,  make sure you're not in Game Mode (press the `G` key in the viewport to toggle game mode)

You can add / remove points and perform a clean regen

![image|690x440](../images/unreal/tutorial/PCG/01/PCG-01-445d1a5e3662a88257b5c79586d457b76f95d50d.jpeg)

You might want to `Cleanup` before working on the spline

Once done, click `Clean Reg`

![image|420x463](../images/unreal/tutorial/PCG/01/PCG-01-a2e27ae291495bbe6c4de50a12b3f2190f26adee.png)

![image|690x439](../images/unreal/tutorial/PCG/01/PCG-01-66ddba27a48935363520e4461951e3482b356831.jpeg)

Select the Forest PCG volume and click `Generate`.  You'll notice the forest doesn't generate inside the ditch spline

![image|690x394](../images/unreal/tutorial/PCG/01/PCG-01-03641820e96bc984b07c39d8ab30523c56199758.jpeg)

## Ground Material

Select your Landscape and assign the landscape auto material that comes along with the sample

![image|379x134](../images/unreal/tutorial/PCG/01/PCG-01-a3b907f6eb53f1e02c1644b3396887f51e15467d.png)

![image|690x317](../images/unreal/tutorial/PCG/01/PCG-01-4776db31f41be24a3b8c9b3eca8fcbc17b4c3d2e.png)


![image|690x337](../images/unreal/tutorial/PCG/01/PCG-01-ec7316d7d6c59d1612ebe57b3e4150264fed16c3.jpeg)

![image|690x374](../images/unreal/tutorial/PCG/01/PCG-01-c0bbe4d954c0d2c5ea9f361ca24b8ecc681648f9.jpeg)


## Ground PCG Graph

The sample comes with a PCG graph for decorating open spaces.

Drag drop `PCGDemo_GroundBP` anywhere on the scene

![image|690x378](../images/unreal/tutorial/PCG/01/PCG-01-9b53dba36afc6931227149ee40964b54c0135765.jpeg)

![image|690x374](../images/unreal/tutorial/PCG/01/PCG-01-c609d2a8cec1c840017d090bc0581f6f5a690931.jpeg)

![image|690x374](../images/unreal/tutorial/PCG/01/PCG-01-c44a1cfb2c3eebf7cb0949ecc17384d43aaafd11.jpeg)

![image|690x417](../images/unreal/tutorial/PCG/01/PCG-01-45eb479b60a7f653084a4fc0d27ee3a77d0d97be.jpeg)


## Extending the PCG Graphs

### Fix Ground PCG Graph

Select the Forest volume and perform a Cleanup

![image|506x500](../images/unreal/tutorial/PCG/01/PCG-01-e7eb3a37ab0802c12a425f136169936abe4221ec.png)

Select the Ground bluerpint and perform a Cleanup

![image|690x463](../images/unreal/tutorial/PCG/01/PCG-01-b5655fde71b3d4631acb15540aaab68c6d58d55f.png)


Then drop in another `PCGDemo_DitchBP` blueprint and hit `Clean Regen`

Your scene should look something like this:

![image|690x432](../images/unreal/tutorial/PCG/01/PCG-01-ebe3db7775fb82478500138f5bb14cf25c38eb70.jpeg)


Now select the `PCGDemo_GroundBP` blueprint and hit `Generate`

![image|690x461](../images/unreal/tutorial/PCG/01/PCG-01-b030d414df4cdffe575631c31cf5ff8e48c7c4ff.jpeg)

You'll notice that the ground was built only on the first spline.    Epic has designed the Ground PCG graph this way to pick the first spline in the scene and build it there.   Lets change that so it picks up all the ditch splines in the scene

Open the Ground PCG graph asset (not the blueprint)

![image|650x333](../images/unreal/tutorial/PCG/01/PCG-01-d1915c12a157b5ae58058ca766144f707cf7302d.png)

![image|690x239](../images/unreal/tutorial/PCG/01/PCG-01-84251dae2fc3d46afc5ed9f8b1e2b82f0c86e1ed.png)

![image|690x193](../images/unreal/tutorial/PCG/01/PCG-01-e1a4ec7b4cf91b1dff6d26338378c47ecbe1073f.png)

Select the node that searches for the ditch blueprint and enable the flag `Select Multiple`

Save the blueprint, come back to the level editor, select the Ground PCG blueprint and regenerate

![image|690x426](../images/unreal/tutorial/PCG/01/PCG-01-c16e7aff8a530905544eba135149e02700800a70.jpeg)

### Fix Forest PCG Graph

The forest PCG graph has a similar issue.  Select the forest volume and hit `Generate`

![image|690x387](../images/unreal/tutorial/PCG/01/PCG-01-f2044923273f3d4dae4e32b8b7c137b894b05d1e.jpeg)

The forest doesn't generate over the first ditch spline, however it ignores the other splines

Open up the forest PCG graph: `Content/PCG/Graphs/Forest/PCGDemo_Forest`

![image|690x340](../images/unreal/tutorial/PCG/01/PCG-01-d3b85e341d546f3831c240dca1cb8129e534d9a7.png)

![image|690x341](../images/unreal/tutorial/PCG/01/PCG-01-7f4e89c85aaee672b66dc1def2ab49b02a87d5f7.png)

Select the node that searches for the ditch blueprint and enable the `Select Multiple` flag

![image|690x217](../images/unreal/tutorial/PCG/01/PCG-01-add2f958ff1089a5b2a92149576d90663c552202.png)

![image|690x400](../images/unreal/tutorial/PCG/01/PCG-01-c36258a7abf725093f3bec7b20ebf799791c00d9.jpeg)

The forest should grow inside every ditch spline placed in the scene


## Landscape Modifications

Modify the landscape and the PCG should automatically regnerate around it

![image|690x358](../images/unreal/tutorial/PCG/01/PCG-01-86e15b837dbc2fca3e48c913ddcbee222f35280f.jpeg)

![image|690x458](../images/unreal/tutorial/PCG/01/PCG-01-b3ef22657d5c0e58f12a1ab1b09eb6589abecfc5.jpeg)

![image|690x458](../images/unreal/tutorial/PCG/01/PCG-01-e7de7884dfe73adcd2f19aa209df7d27133f9f15.jpeg)

Drop in `PCGDemo_ForestCliffs` and reset the location and set the scale to (200, 200, 10) so it covers a large area.   This should add trees around the cliff area

![image|690x334](../images/unreal/tutorial/PCG/01/PCG-01-6d2dd27390f8c3156dc1b232347cf5c345fe06d9.png)

![image|690x379](../images/unreal/tutorial/PCG/01/PCG-01-7cb4d4a30ab69bdadc0eb9615ff680838cbf7f61.jpeg)

![image|690x331](../images/unreal/tutorial/PCG/01/PCG-01-fb349eb5b6bd1de74dc4f0eb6978e9ab5ecd7001.jpeg)

## Exclude PCG Generation around certain areas
Avoid PCG generation around certain objects.  I've placed an asset here and I don't want the foliage, rocks and trees generated by the forest PCG graph

![image|690x389](../images/unreal/tutorial/PCG/01/PCG-01-7f5ad88f02925604d1febbc180498b00779833b6.jpeg)


We'll update the forest PCG graph so it removes points within a volume (that we place around the house) so the forest doesn't grow there

![image|690x369](../images/unreal/tutorial/PCG/01/PCG-01-9263fef0866df03def037a9f6898205991822b43.jpeg)

![image|690x322](../images/unreal/tutorial/PCG/01/PCG-01-f23c2e81ebbd224a0ee9f5b6e88b4d01815220a5.jpeg)


The developers from Epic have created a provision for excluding the generation around a certain volume in the ditch blueprint (`Content/PCG/Graphs/Ditch/PCGDemo_Ditch`)

Lets open that up and copy that node over to the forest blueprint

**PCGDemo_Ditch.uasset**

![image|690x355](../images/unreal/tutorial/PCG/01/PCG-01-c8c95507869290321d1fa99c978f52b4bf266bc2.png)


Open up the forest pcg graph (`Content/PCG/Graphs/Forest/PCGDemo_Forest`)

![image|690x332](../images/unreal/tutorial/PCG/01/PCG-01-358b06c3a40c967140e4a1334783a8e96580db08.png)


![image|690x278](../images/unreal/tutorial/PCG/01/PCG-01-225d1c68131f2c5d5f7e393ca7df321e8356d021.png)

Paste the node (that you copied from the ditch pcg graph) over here and link it to the Merge node as shown below:

![image|690x367](../images/unreal/tutorial/PCG/01/PCG-01-2b81743174eb263e215de11f4e00eb8d446a97da.png)

This will remove all PCG points from the scene that are contained with PCG Volumes tagged with `PCG_EXCLUDE`.  Save the graph

Now all you have to do is drop in a PCGVolume, navigate to the Tags section and add `PCG_EXCLUDE`

![image|295x213](../images/unreal/tutorial/PCG/01/PCG-01-95f2e36f67b9d2ea5ac1a063fe4530da2caaf6f8.png)

Select the volume you just created, and search for Tag in the details panel.  Add a tag named `PCG_EXCLUDE`

![image|510x500](../images/unreal/tutorial/PCG/01/PCG-01-1ea8a0e0cd3a5fe220a939bad1c5dc8cf02104a2.png)

> IMPORTANT: Do not add this to the Components Tag or the PCG tag.  This should be added to the actor tag

Now move / rotate / scale your volume and the forest would not be generated inside this volume.    I've wrapped the volume around the building.  Feel free to make copies of this volume and reuse it elsewhere

![image|690x427](../images/unreal/tutorial/PCG/01/PCG-01-85765f61b2a0289d587c666a2a7a0c8350d777fd.jpeg)

Select the forest blueprint:
* Click Cleanup to remove the forest
* Click Generate

![image|690x367](../images/unreal/tutorial/PCG/01/PCG-01-375099fd2ae9139bcb474c0521cd28342a99719f.jpeg)
