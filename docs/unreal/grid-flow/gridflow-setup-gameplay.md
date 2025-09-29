# Setup GridFlow Gameplay

We'll clone an GridFlow sample scene and setup gameplay on it from scratch

Open Launch pad and clone this scene somewhere

![image|689x141](../images/unreal/tutorial/E2/E2-f2ac33995166aec74cc3f9d4cad78cc32a03a86d.png)

![image|690x424](../images/unreal/tutorial/E2/E2-73c3a01a2d8724fe688f97a733abe80b7fd9667b.jpeg)

Open the scene, select the dungeon actor and destroy the dungeon

![image|690x408](../images/unreal/tutorial/E2/E2-e0172240a835b5ad10654e7bb3582648462d9c18.png)


Hitting play won't do anything, as there's no gameplay in this scene.    We'll set that up now.  For this, we need a custom GameMode

# Game Mode
Create a blueprint that derives from `GameMode` (not `GameModeBase`)

![image|472x375](../images/unreal/tutorial/E2/E2-a507031bdf2ab3faa536773c5c878e2b3c87e70b.png)


![image|564x431](../images/unreal/tutorial/E2/E2-8f80e371e1e376541ad38131dbb93eba4963bb50.png)

![image|674x479](../images/unreal/tutorial/E2/E2-ae4588e394b9123dbfe6daec47c7fcd9a9a6de27.png)


We want our dungeon to build in a non-blocking way, where it's built over multiple frames.    During this time, you may show an animated loading screen.   In this example, we'll keep the player in specitator mode and start the game (spawn our character) only after the dungeon has been fully built

## Build the dungeon
Do thie following:
* Create a bool variable to control when the game starts.  Call this `CanStartGame` and set the default value to false
  ![image|369x109](../images/unreal/tutorial/E2/E2-a0fd100a746d3ad93fa278ca8f1eca7e6550adb6.png)
* Place this logic in BeginPlay.  Here we randomize the seed and build the dungoen.  Before that, we hook on to the `OnDungeonBuildComplete` event so we get notified when it is fully built.  When that happens, we set the boolean flag to true, which would then start the game (logic for that later below)
  ![image|690x174](../images/unreal/tutorial/E2/E2-d70bf22a9568ea9936c8082b576541630b1a3363.png)

## ReadToStartMatch - Control when the game starts
Override the function `Read to Start Match`

![image|381x500](../images/unreal/tutorial/E2/E2-feb326bc2ede0268fc4022187c39068564176278.png)

> If you don't see this override, this means your game mode derives from `GameModeBase` and not `GameMode`

Return the `Can Start Game` bool variable value.

![image|690x366](../images/unreal/tutorial/E2/E2-b5ddf5e7dbb5497ba9d81ddaa315e05683434308.png)

This would tell the engine to start the game only after our dungeon is fully built.

### Detailed explanation of how this function works:
`Read to Start Match` gets called by the engine repeatedly every tick to check if we can start the game.   If you don't want to start the game, keep returning false here until you are ready, which is what we're doing here
This flag gets set to true after our dungeon gets fully built, at which point we're ready to start

## Find Player Start
You need to tell the engine which player start to use
Override the `FindPlayerStart` function in your game mode blueprint

![image|690x441](../images/unreal/tutorial/E2/E2-ff33dea85942888644cb72c2367604ae34080202.png)

Put this code in:

![image|690x213](../images/unreal/tutorial/E2/E2-7bdad8eb72c2bfecfa9def6b5d7cc5a3d0a493a3.png)


## Delete default Player Start
Our theme file spawns a `Player Start` actor in the spawn room.   We want our `FindPlayerStart` function to search and pick this one up.  So, we need to make sure we don't have any other PlayerStart actors in the scene.

When we created a new scene, there was a default PlayerStart actor,  We need to delete this so it doesn't pick that up and place our character in an invalid location

![image|637x230](../images/unreal/tutorial/E2/E2-df1e0426bfc14daeeb31adb142c3c1ed22de82fb.png)

![image|637x230](../images/unreal/tutorial/E2/E2-94db6fb6d09011f1f4d3dcd60bd8642218e727cc.png)


## Assign the game mode

With the level opened, open the `World Settings` window. Navigate to Settings > World Settings

![image|690x445](../images/unreal/tutorial/E2/E2-409cc1a5718764be5372ad5292fc699ef57b1e45.png)

You'll find the `Settings` button on the top right corner of Unreal Editor

![image|690x257](../images/unreal/tutorial/E2/E2-30567fe606e873ad49723686603e07dbf0799acb.png)

Hit play and you should see your default pawn (with fly mode) placed at the spawn room

![image|690x331](../images/unreal/tutorial/E2/E2-bc8f0e6b9e4184d3ff564e1d6fdaab6101f15c65.jpeg)


## Use a custom character

Lets use a Third Person character.    Open up your game mode asset, navigate to `Class Defaults`

![image|420x107](../images/unreal/tutorial/E2/E2-1a1068223a9ab782f58714e2e9773e25869fa15b.png)

Set the `Default Pawn Class` to something else.  I've set it to a third person character (if you don't have it, then add it from the Content Browser > Add > Add Content or Feature Pack > Third Person Character)

`/Game/ThirdPerson/Blueprints/BP_ThirdPersonCharacter`

![image|690x301](../images/unreal/tutorial/E2/E2-f9e63fd1163cb950699d7ded7dcf4908e5bb9e8d.png)


![image|689x399](../images/unreal/tutorial/E2/E2-2fd1b6c31053c5798530a5f5a0df68ca76c71df5.jpeg)

If you're not able to move the character or look around, open up the character blueprint and check the `Begin Play` event. This is how it looks like:

![image|690x161](../images/unreal/tutorial/E2/E2-84a2c16afceebdc8549750ad938f76ea5bdaf8d5.png)

To fix it,  do this:

![image|690x373](../images/unreal/tutorial/E2/E2-e316b3f9941893309b7ebf2365793c7aed8e40dc.png)

## Async Build

If you want your dungeon to build over multiple frames and not stall for a bit while the meshes spawn in, set it to a non-zero value.

![image|634x500](../images/unreal/tutorial/E2/E2-cc5aa50fb10deaa0104cb754805682f3f95048f2.png)

Here, I allow the system to use up a max of 64ms per frame to spawn in the meshes.  It will spread out the mesh spawns over multiple frames.


# HUD and Inventory

## Setup Player Controller

Create a Player Controller so we can display the inventory HUD, that comes along with the sample.

![image|595x304](../images/unreal/tutorial/E2/E2-c4ca294778a043102a25d47b6c6f0917b17f5ca6.png)

![image|583x467](../images/unreal/tutorial/E2/E2-e1827da088a142c17a6f5e9996db3294cdad77b5.png)

Open up the Game Mode asset and assign the new player controller, so it picks it up

![image|298x383](../images/unreal/tutorial/E2/E2-c4c250124114513d35add6c778b323e28766d8bc.png)

![image|514x92](../images/unreal/tutorial/E2/E2-f4a7094ab7944ea8ed46dab6ace255a45057fe9e.png)

![image|690x346](../images/unreal/tutorial/E2/E2-c369158700453b176f327acf61c52a8b9c7b86a4.png)

## Spawn HUD
Open the new player controller

![image|258x376](../images/unreal/tutorial/E2/E2-aa5dc48ccdb09c5f1dfaa76bd6ad2327e4687d13.png)

Spawn this widget in:
/Script/UMGEditor.WidgetBlueprint'/DungeonArchitect/Showcase/Legacy/Samples/DA_GridFlow_Game/UI/UI_GridFowDemo_HUD.UI_GridFowDemo_HUD'

![image|690x176](../images/unreal/tutorial/E2/E2-bf0a5b7592fba0541a245a8972025682af105b08.png)

![image|690x435](../images/unreal/tutorial/E2/E2-1856afb19c2dc1a005908cb0af4ac9d06548927d.jpeg)


## Setup Inventory

Open the third person character and add the inventory component

![image|690x363](../images/unreal/tutorial/E2/E2-05cc3c20162cfb176faf9ecc730de8fbb50d95e8.png)


Your character should now be able to pick up keys

![image|690x468](../images/unreal/tutorial/E2/E2-f08cfb928922a20a76ebc6d27868b2451eb91b4c.jpeg)

![image|690x468](../images/unreal/tutorial/E2/E2-10d8ad639ec0791ddfa087fb74b36d7cee0010a7.jpeg)


and open the right doors with those keys

![image|690x468](../images/unreal/tutorial/E2/E2-8f2885b201d25107e70f3be0a766790e72844ef9.jpeg)

![image|690x468](../images/unreal/tutorial/E2/E2-3e235584cad66b86b15b19a742d5eb636ead6e1e.jpeg)


> The inventory component `GF_Inventory` and the UI are simple blueprint implementation in the samples folder and are not part of the core of DA.   This means you can integrate your own inventory system easily or build on this
