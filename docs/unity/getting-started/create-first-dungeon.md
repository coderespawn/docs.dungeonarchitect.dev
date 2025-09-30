---
title: Create your first Dungeon
slug: /unity/getting-started
sidebar_position: 2
---

## Install Dungeon Architect

Install and import [Dungeon Architect](https://u3d.as/nAL) from the Asset Store. You should see the following folders:

![](../images/unity/tutorial/01/ut-01-da_folders.png)

## Setup Dungeon Prefab

Create a new Scene

Navigate to `CodeRespawn > DungeonArchitect > Prefabs` and drop in the `DungeonGrid` prefab on to the scene

![](../images/unity/tutorial/01/ut-01-drop_grid_prefab.png)

Select the dungeon game object and inspect the properties. We'll need to assign a new theme before we can build the dungeon

![](../images/unity/tutorial/01/ut-01-select_dungeon_go.png)

![](../images/unity/tutorial/01/ut-01-da_dungeon_prop.png)


## Assign Theme

Assign an existing theme to the dungeon actor

* Navigate to `Assets\DungeonArchitect_Samples\Demo_Theme_Candy\Themes`
* Assign theme file named `CandyDungeonTheme` as shown in the image below

![](../images/unity/tutorial/01/ut-01-dungeon_assign_theme.png)


## Build Dungeon

Select the `DungeonGrid` game object and click the `Build Dungeon` button in the Inspector window

![](../images/unity/tutorial/01/ut-01-build_dungeon.png)

![](../images/unity/tutorial/01/ut-01-candy_dungeon.jpg)


## Randomize Dungeon

Select the `DungeonGrid` game object and change the Seed value in the configuration.  Changing this value will create a dungeon with a different layout


![](../images/unity/tutorial/01/ut-01-rand_dungeon.png)

Click `Build Dungeon` button to rebuild the dungeon with the new seed


## Organization

All the dungeon objects are created on the root hierarchy and makes it difficult to organize.   We'll configure it so all objects are spawned under a certain game object

![](../images/unity/tutorial/01/ut-01-org01.png)

Lets destroy this current dungeon, configure it for better organization and then rebuild

### Destroy Existing Dungeon

Search for `dungeon` on the hierarchy search box

![](../images/unity/tutorial/01/ut-01-org02.png)

Select the DungeonGrid game object and click the `Destroy Dungeon` button

Clear out the search text box in the hierarchy.  Your hierarchy should now look like this

![](../images/unity/tutorial/01/ut-01-org04.png)


### Configure Parent Object

Create an empty Game Object.  All our dungeon items will go inside this parent object

![Create an empty game object](../images/unity/tutorial/01/ut-01-create_empty.png)


Rename the parent object (e.g. `Dungeon Items`)

![](../images/unity/tutorial/01/ut-01-org05.png)

Select the parent object and **Reset the transform**

![](../images/unity/tutorial/01/ut-01-org06.png)

![](../images/unity/tutorial/01/ut-01-org07.png)


Select the parent object and set it to **static**

![](../images/unity/tutorial/01/ut-01-org08.png)


Assign the parent object to the GridDungeon game object

![](../images/unity/tutorial/01/ut-01-org09.png)


### Rebuild Dungeon

Select the GridDungeon game object and click `Build Dungeon`

All your dungeon game objects will be organized under the parent object

![](../images/unity/tutorial/01/ut-01-org10.png)
