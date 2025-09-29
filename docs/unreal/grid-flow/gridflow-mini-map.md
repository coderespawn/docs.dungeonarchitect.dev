# Mini-Map

## Setup

Display a 2D minimap with fog of war

![](../images/unreal/tutorial/E/E-107.jpg)


Drop in a `Grid Flow Mini Map` actor on to the scene and configure it like below

![](../images/unreal/tutorial/E/E-108.png)

![](../images/unreal/tutorial/E/E-109.png)

![](../images/unreal/tutorial/E/E-110.png)


Check the player controller on how to initialize the minimap and show it on the screen ``DungeonArchitect Content > Showcase > Legacy > Samples > DA_GridFlow_Game > Blueprints > BP_GridFlowDemo_PlayerController``

![`Right Click > Open Image In New Tab` for a clearer image](../images/unreal/tutorial/E/E-111.png)
 
![](../images/unreal/tutorial/E/E-112.png)


Check the HUD widget on how to display this in the screen

``DungeonArchitect Content > Showcase > Legacy > Samples > DA_GridFlow_Game > UI > UI_GridFowDemo_HUD``


## Minimap Tracked Objects

To track an object in the minimap, simple add the ``DungeonMiniMapTrackedObject`` component to it and configure it.


![](../images/unreal/tutorial/E/E-114.png)


![](../images/unreal/tutorial/E/E-113.png)

The id maps to the id you specified in the MiniMap actor's icon list

![](../images/unreal/tutorial/E/E-115.png)