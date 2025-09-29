---
title: Runtime Navigation
---

Dungeon Architect can generate dungeons at runtime so you get a new dungeon every time you play

This section shows you how to generate a navigation mesh on these runtime generated dungeons so the NPCs can move around

> This section is releavant for dungeon types that use a theme file (e.g. Grid Builder, Grid Flow builder, City builder etc)


## Setup Dungeon Game Object

Select the Dungeon game object and make sure you have the `Dungeon component in it.  If not add one


![](../../../images/unity/tutorial/13/ut-13-39.png)

![](../../../images/unity/tutorial/13/ut-13-40.png)

![](../../../images/unity/tutorial/13/ut-13-41.png)

Make sure `Enable Runtime Navigation` is checked

![](../../../images/unity/tutorial/13/ut-13-42.png)


## Build Runtime Dungeon

Set up your scene so this dungeon gets built at runtime as discussed in the section [Runtime Dungeons](runtime-dungeons.md) section and hit Play

![](../../../images/unity/tutorial/13/ut-13-38.png)

This will build your dungeon but won't build the navigation mesh, since we haven't specified the meshes that would contribute to the navmesh generation


To confirm this, do the following:
1. Open the navigation panel from the main menu (`Window > AI > Navigation`)

   ![](../../../images/unity/tutorial/13/ut-13-43.png)

2. Play your game and switch to the Scene view. Now focus on the Navigation panel, you won't see a nav mesh generated

   ![](../../../images/unity/tutorial/13/ut-13-44.png)


## Setup Theme File 

When we spawn prefabs from the theme editor, we'll need to set a flag on all the prefabs that would contribute to the navigation mesh generation

Open the theme that your dungeon uses

![](../../../images/unity/tutorial/13/ut-13-45.png)


Select the Ground prefab node and inspect the properties

![](../../../images/unity/tutorial/13/ut-13-46.png)

Make sure `Affects Navigation` is set.   Do this for all the static prefabs (Walls, doors, fence etc)

![](../../../images/unity/tutorial/13/ut-13-47.png)


Now run the game and you'll see the navigation mesh

![](../../../images/unity/tutorial/13/ut-13-48.jpg)



You don't want holes under dynamic objects like NPCs, Keys etc

![](../../../images/unity/tutorial/13/ut-13-49.jpg)

Make sure you've not set them to affect the nav mesh generation

![](../../../images/unity/tutorial/13/ut-13-51.png)

![](../../../images/unity/tutorial/13/ut-13-50.jpg)
