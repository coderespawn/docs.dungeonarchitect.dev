# Mini-Map

## Setup

Display a 2D minimap with fog of war

![](E-107.jpg)


Drop in a `Grid Flow Mini Map` actor on to the scene and configure it like below

![](E-108.png)

![](E-109.png)

![](E-110.png)


Check the player controller on how to initialize the minimap and show it on the screen ``DungeonArchitect Content > Showcase > Legacy > Samples > DA_GridFlow_Game > Blueprints > BP_GridFlowDemo_PlayerController``

![`Right Click > Open Image In New Tab` for a clearer image](E-111.png)
 
![](E-112.png)


Check the HUD widget on how to display this in the screen

``DungeonArchitect Content > Showcase > Legacy > Samples > DA_GridFlow_Game > UI > UI_GridFowDemo_HUD``


## Minimap Tracked Objects

To track an object in the minimap, simple add the ``DungeonMiniMapTrackedObject`` component to it and configure it.


![](E-114.png)


![](E-113.png)

The id maps to the id you specified in the MiniMap actor's icon list

![](E-115.png)