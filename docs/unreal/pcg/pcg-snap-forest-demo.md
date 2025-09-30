---
title: "Snap Forest PCG Demo"
sidebar_position: 3
---

In this tutorial, we'll be creating this:

<video src="https://www.youtube.com/watch?v=iplZmwlaSq0" />

This tutorial build on these two existing tutorials:


* [PCG Framework Overview](pcg-framework-overview.md)
* [Custom Snap Bound Shapes](../snap-flow/snapflow-custom-module-bounds.md)

Please go through those first, if you haven't done so already

Download and load up the [Electric Dreams](https://www.unrealengine.com/en-US/electric-dreams-environment) project

Create a new Open World level

![image|534x454](../images/unreal/tutorial/PCG/02/PCG-02-8ed4a8e559189c6d07770f1d343f471a13c97213.png)


Assign the landscape material

![image|690x336](../images/unreal/tutorial/PCG/02/PCG-02-70b4f7fea37337eb5cdbc6ae039459a338812537.jpeg)


and drop in a Dungeon Actor and reset the location to ground level (e.g. 0,0,0)

![image|607x440](../images/unreal/tutorial/PCG/02/PCG-02-1465c6a79763fa330c695708bc13078284fd5f1b.jpeg)

Set the builder type to SnapMap

![image|548x500](../images/unreal/tutorial/PCG/02/PCG-02-5a70eaba8f2f8cded2e683073ee1d078d10aacf1.png)

## Module Creation

We'll create individual modules, like you see in the video above.  Save this level then create a new empty level for our module

> NOTE: Modules are rooms that are stitched together using the SnapMap builder

![image|534x462](../images/unreal/tutorial/PCG/02/PCG-02-0a1d3fbe9190fb187cf8f046b16e1bab4f29048b.png)

![image|690x432](../images/unreal/tutorial/PCG/02/PCG-02-2bf9b38b86d8e0a5d79fe4e1beba800b46223e18.jpeg)

Select the ditch blueprint and select the Spline component, so you can visualizae and modify the spline shape

![image|690x348](../images/unreal/tutorial/PCG/02/PCG-02-1f82e37f3332cd80ed7cb7c92528a6487464d32c.jpeg)

With the Spline component selected, enabled "Debug Draw" so you can view the spline shape even when the ditch actor is not selected. We'll need this for propertly aligning the connections

![image|568x500](../images/unreal/tutorial/PCG/02/PCG-02-3e88f64d8de6d135d3a41fe73af11e8829a2477c.png)

## Snap Connection

Create an empty snap connection asset.

![image|690x444](../images/unreal/tutorial/PCG/02/PCG-02-2214aa7eeccefbad8883be84035aacf4964080a2.png)

Drop this connection in a few places around the spline.  Don't keep it too close to the spline as the art assets that the ditch blueprint creates around this spline are a bit further away. Place them like this:

![image|690x376](../images/unreal/tutorial/PCG/02/PCG-02-954d02f26c3e0497871fccb9edb34fcefc7ffafc.jpeg)

Make sure the red connection arrows are facing outwards

Next, drop in a `Snap Map Module Bounds` actor

![image|396x195](../images/unreal/tutorial/PCG/02/PCG-02-71c3a98fb04c75fdbd56a395d1ecf151e7881311.png)

Add more points as needed and wrap it around the spline shape.   Keep it a bit further away from the spline, as the ditch spline creates the assets outside the spline shape. Make sure the bounds are near the snap connection actor

![image|690x381](../images/unreal/tutorial/PCG/02/PCG-02-e0b0630e4768d2d224068666661ddbc400cdb8ab.jpeg)


You may switch to the top view to align everything

![image|690x418](../images/unreal/tutorial/PCG/02/PCG-02-83c5ddcefce3b715e95ccec310541e6e0cdef497.png)

Save the module level

![image|253x286](../images/unreal/tutorial/PCG/02/PCG-02-2813fa0045400cd8c0745dddfb6720d8f0fade88.png)

## Module Database

Create a SnapMap module database and register this module.

![image|690x440](../images/unreal/tutorial/PCG/02/PCG-02-cef381aa80412814214d6a1601c8c108ec14c58f.jpeg)

![image|567x499](../images/unreal/tutorial/PCG/02/PCG-02-780374ca089e99edc182e34a10e73704ce38420d.jpeg)


Build module database cache

![image|405x149](../images/unreal/tutorial/PCG/02/PCG-02-0ac3a1129f0d25c82ff53322155ae1a8da41bb24.png)

## Flow Graph

Create a SnapMap flow graph.   These are rules for stitching the levels.   Right now we have only one module, registered under the name "Room" in the module database created above

![image|690x445](../images/unreal/tutorial/PCG/02/PCG-02-f0e83f01702ce6dbda3691db264c9b4ba0cd18a8.jpeg)

Add a new node and name it `Room`.     We name it `Room` because we've registerd our module in the ModuleDB with this name

![image|690x334](../images/unreal/tutorial/PCG/02/PCG-02-0590a0611adc0887f60e79a6ab85b375b2f86e5e.png)


Select the Start Rule and add two `Room` nodes on the RHS graph and connect them up

![image|582x499](../images/unreal/tutorial/PCG/02/PCG-02-ea9462d152364140b434c2f224f5995faba77039.png)

This will connect two rooms together. We start with a small graph to make sure the connection setup works.  Then we'll move to a larger graphs


## Setup Dungeon Actor
Open up the first map we created and select the Dungeon Actor

![image|690x324](../images/unreal/tutorial/PCG/02/PCG-02-c9bd39d79458b6fce5d9b1b32f4b5403ed9a62f7.jpeg)

Change the Builder Class to `Snap Map`

![image|500x500](../images/unreal/tutorial/PCG/02/PCG-02-d84389aead025cb5d90209c5f89399c66aa736de.png)

Then assign the assets we created

![image|690x479](../images/unreal/tutorial/PCG/02/PCG-02-63ba7790d059436e06eb74f7c990f17e818eff4c.jpeg)

Click `Build Dungeon`, it should stitch the two modules together

![image|690x335](../images/unreal/tutorial/PCG/02/PCG-02-7a503c461612bb1d20a2443b9bca45a6ea25510f.jpeg)

![image|690x335](../images/unreal/tutorial/PCG/02/PCG-02-baf6d9236f7e0e8e5246d0405b8aa3540fa31534.jpeg)


## Troubleshoot
If it didn't build, make sure the connection points are not too far inside the module bounds

This is how a successful stitch looks like

![image|616x500](../images/unreal/tutorial/PCG/02/PCG-02-965c2624cb042bd04a01b8c6bf0873f7f3165f38.png)

Either update your connection point positions and rebuild your module database (important!) or increase the collision tollerance to a higher number, this is the amount of overlap the system would tolerate

![image|341x294](../images/unreal/tutorial/PCG/02/PCG-02-760d37a5be5b87cf1c54a071c758e64a043cb8e3.png)

## Improved Flow Graph

Now that we have this working, open up the flow graph and add a more complex rule

![image|513x500](../images/unreal/tutorial/PCG/02/PCG-02-88f8c3642cc2e77a5b07580f297da83982592ee0.png)

Build the dungeon

![image|690x322](../images/unreal/tutorial/PCG/02/PCG-02-fcd35855da5fcbf6e6779b9ade09c01c1bef9d05.jpeg)

Randomize, Click Build

![image|687x500](../images/unreal/tutorial/PCG/02/PCG-02-7d1584c2b2e4699264d42c52e258dfb5c9360806.jpeg)

![image|690x424](../images/unreal/tutorial/PCG/02/PCG-02-9f98755562feb1bf69440c8781e64669743221ad.jpeg)


## Generate Persistent Level

After we generate the dungeon, we want to pass this spline information to the PCG system.  So we don't need level streaming here and everything needs to be generated in the current persistent level

Select the dungeon actor and enable `GenerateSinglePersistentDungeon`

![image|690x198](../images/unreal/tutorial/PCG/02/PCG-02-32a19607c0a146262540f8941bd6f1a751c17f50.png)


## PCG Post Build Setup

After we spawn our rooms into the world (which are ditch splines) We want the PCG system to build everything.  Lets create a post build event for it

![image|232x500](../images/unreal/tutorial/PCG/02/PCG-02-665baf9e259d4f37411ba741c684bc4c2f41e952.png)

![image|406x432](../images/unreal/tutorial/PCG/02/PCG-02-3965f66f3228b4f9dac7c75847273d8be4ad70b9.png)

Open it up and override the  `OnPostDungeonBuilt` function

![image|690x286](../images/unreal/tutorial/PCG/02/PCG-02-3e763f8dd1f241058b8ddfad2dc0eef4f8edb052.png)

In this function, we're going to iterate through all the `PCGDemo_DitchBP` blueprints that were spawned as part of the room module and call the `Clean Regen` function on it.

Dungeon Architect has a `DAGetAllActorsOfClass` helper node for this

![image|690x186](../images/unreal/tutorial/PCG/02/PCG-02-450ec78e9f9f8061ec52943743a04faad0bc3daa.png)

Assign this to the dungeon actor's `Event Listener` list

![image|379x499](../images/unreal/tutorial/PCG/02/PCG-02-4124ab06d0a6af24f69e697b6b6683579ac0f7cb.png)

Rebuild the dungeon and it should build the ditch blueprints

![image|690x416](../images/unreal/tutorial/PCG/02/PCG-02-ca439f431da13036d863a63799f2ae5af369be0d.jpeg)

## Forest PCG Blueprint
Next, drop in a forest PCG bluerpint `PCGDemo_ForestBP` anywhere on the scene

![image|690x364](../images/unreal/tutorial/PCG/02/PCG-02-7fb706f2f4d5eb9679efd9b29027f6334a933ff5.jpeg)

We'll invoke the Forest PCG bluerpint on our dungeon post build event

![image|690x330](../images/unreal/tutorial/PCG/02/PCG-02-7d7b8de5f29042bc7474eaf30346668b0efd5d16.png)

Destroy the current dungeon and rebuild the dungeon

![image|690x253](../images/unreal/tutorial/PCG/02/PCG-02-b44a843e2f4f80b2974a5b0ae14ccfee82528a3d.jpeg)


## Ground PCG Graph

Drop in the `Content/PCG/Graphs/Ground/PCGDemo_GroundBP` blueprint anywhere on to the scene

![image|562x500](../images/unreal/tutorial/PCG/02/PCG-02-77a4777fad59448113cc6ccf49ce53d92e28a45a.jpeg)

![image|690x341](../images/unreal/tutorial/PCG/02/PCG-02-d0a32554e4d93cf6829f589f44d0796d2cd588a0.jpeg)


Lets invoke this PCG as well, after our dungeon builds

![image|690x441](../images/unreal/tutorial/PCG/02/PCG-02-b8a679199e5ee8d42bd2a8d00d6ac617472fe721.png)


## PCG Post Destroy setup

We want to cleanup and rebuild the forest after the dungeon is destroyed

Override the `OnPostDungeonDestroyed` function

![image|690x183](../images/unreal/tutorial/PCG/02/PCG-02-2289ce566126936802b59ad528f6a3b2315073a8.png)

and perform cleanup like this:

![image|690x320](../images/unreal/tutorial/PCG/02/PCG-02-d9d760004ce485e667b1b69e9c531d2fa5a03da9.png)


Destroying the dungeon should remove the forest

![image|690x306](../images/unreal/tutorial/PCG/02/PCG-02-23bb24c1ac074e24d46e737925fc1dd642f0ba68.jpeg)

![image|690x306](../images/unreal/tutorial/PCG/02/PCG-02-dd899f95c2abac7c4178a6d8a0553ba7143f58c6.jpeg)

## Connection

The adjacent room connections look like this. The geometry from the other room is overlaping

![image|690x270](../images/unreal/tutorial/PCG/02/PCG-02-fbba8e12156fe6c893e598b0dff3af1c5c9d700d.jpeg)


Open up the module and increase the bounds.  Also move the connection points outwards (this depends on your art asset placement)

![image|545x500](../images/unreal/tutorial/PCG/02/PCG-02-f2d0d09e1a2541c5409e4520acc45db706543d79.png)

Save and rebuild the module database cache.  Then rebuild the dungeon

![image|690x293](../images/unreal/tutorial/PCG/02/PCG-02-7ffd4538a20c7312216c6f5c549dfb1d175df812.jpeg)


## Opening up connections

Now we need to create a gap so the player can walk through to the other room

The forest and ditch PCG graphs designed by Epic have a logic where generation inside volumes is ignored if that PCGVolume has a `PCG_EXCLUDE` actor tag

To test this out, drop in a PCGVolume on to the scene

![image|361x260](../images/unreal/tutorial/PCG/02/PCG-02-6a2b17142331d6e5e8f4319e5ebebc932d239909.jpeg)

Scale it and place it approximately where the connection is

![image|690x433](../images/unreal/tutorial/PCG/02/PCG-02-6f503b798ee58ef601764a80e4c80f45b0e6bcaa.jpeg)

In the PCGVolume's detail panel, search for Tag and add `PCG_EXCLUDE` to the actor tag

![image|385x500](../images/unreal/tutorial/PCG/02/PCG-02-bced3976ae5d46c373329fc9f7f367c14383d866.png)

> NOTE: Do not add this to the component tag.  It should be added to the Actor tag as shown in the image above

Destroy and rebuild the dungeon

![image|690x336](../images/unreal/tutorial/PCG/02/PCG-02-9407cb7d48de1a01e1377b2a80b353a3bd7b1db9.jpeg)


Open up your connection asset and use a PCG volume as a door

![image|442x217](../images/unreal/tutorial/PCG/02/PCG-02-373e7bf1ed1314b2f58f675b044b5d311cb3da06.png)

![image|690x286](../images/unreal/tutorial/PCG/02/PCG-02-b8e9daf4f769db2ae1a1f75272af20d697b4949a.png)

Set the scale to (20, 10, 10)

![image|690x349](../images/unreal/tutorial/PCG/02/PCG-02-b639adff74de5331e5a84c204d690298138d3a2d.png)

Set the `PCG_EXCLUDE` tag in the node template settings

![image|494x500](../images/unreal/tutorial/PCG/02/PCG-02-13e10f3b0c5d9768bcfcd22c8e1524131183f23a.png)

Add more assign assets around the connection opening, like we've done in the video to cover up the gaps

![image|690x283](../images/unreal/tutorial/PCG/02/PCG-02-244280a28127040e28eac1c0ad1dda11d462b45f.jpeg)
