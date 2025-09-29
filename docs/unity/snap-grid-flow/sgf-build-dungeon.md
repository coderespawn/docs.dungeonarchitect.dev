---
title: Build Dungeon
---


It's time to use everything we've created to build a dungeon

## Create Theme file

Create an empty theme file somewhere in the content browser.  We'll visit this later to spawn items in our modules
(like NPCs, Spawners, Pickups, player prefab etc.)

![](../../../images/unity/tutorial/09/ut-09-70.png)

Rename it to `GameItemTheme`

![](../../../images/unity/tutorial/09/ut-09-71.png)


## Setup Dungeon Game Object

1. Create a new scene and drop in a `DungeonSnapGridFlow` prefab from `Assets > CodeRespawn > DungeonArchitect > Prefabs`

   ![](../../../images/unity/tutorial/09/ut-09-72.png)

2. Select the `DungeonSnapGridFlow` game object and inspect the properties

   ![](../../../images/unity/tutorial/09/ut-09-73.png)

   ![](../../../images/unity/tutorial/09/ut-09-74.png)

   We'll assign the three assets we've created earlier

3. Assign the `GameItemTheme` create created above

   ![](../../../images/unity/tutorial/09/ut-09-75.png)

4. Assign the Snap Grid Flow Graph

   ![](../../../images/unity/tutorial/09/ut-09-76.png)

5. Assign the Module Database

   ![](../../../images/unity/tutorial/09/ut-09-77.png)
   

## Build Dungeon

Select the `DungeonSnapGridFlow` game object and click `Build Dungeon`

![](../../../images/unity/tutorial/09/ut-09-78.png)
   
![](../../../images/unity/tutorial/09/ut-09-79.png)

![](../../../images/unity/tutorial/09/ut-09-80.jpg)

Change the seed and click build again to get a different dungeon

![](../../../images/unity/tutorial/09/ut-09-81.png)

![](../../../images/unity/tutorial/09/ut-09-82.jpg)


## Debug Draw

You get a debug overlay of the layout graph rendered by default when you build the dungoen. You'll want to turn this off in your final dungeon

Do this by unchecking the `Debug Draw` check box and rebuild the dungeon

![](../../../images/unity/tutorial/09/ut-09-84.png)

![](../../../images/unity/tutorial/09/ut-09-83.jpg)


Let's keep the `Debug Draw` check box on for now so we can see the layout graph overlayed in the scene

![](../../../images/unity/tutorial/09/ut-09-85.jpg)

![](../../../images/unity/tutorial/09/ut-09-95.jpg)

## Keep Things Organized

When you build the dungeon, it clutters up the hierarchy

![](../../../images/unity/tutorial/09/ut-09-86.png)

We'll configure it so that our dungeon is built under a certain game object and won't clutter the root.  

1. Create a new empty game object and name it `DungeonItems`

   ![](../../../images/unity/tutorial/09/ut-09-87.png)

   ![](../../../images/unity/tutorial/09/ut-09-88.png)


2. Reset the transform

   ![](../../../images/unity/tutorial/09/ut-09-89.png)

3. Set it to **static**

   ![](../../../images/unity/tutorial/09/ut-09-91.png)

4. Assign this game object to the *DungeonSnapGridFlow* gameobject's *Pool Dungeon Scene Provider* component

   ![](../../../images/unity/tutorial/09/ut-09-90.png)

5. Click `Build Dungeon` again and our dungeon will be built under the `DungeonItems` game object

## Save Map

We've set up our dungeon game object. Save this scene somewhere, we'll revisit it later
