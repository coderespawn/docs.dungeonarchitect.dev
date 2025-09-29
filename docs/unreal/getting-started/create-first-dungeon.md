# Create your first Dungeon

## Setup Dungeon Actor

Create a new Level and drop in a Dungeon actor

![](A-02.jpg)

Reset the dungeon actor transform to (0,0,0)

![](A-02BX.png)

> Position the dungeon actor at any desired location/rotation to create the dungeon there.

## Show Plugin Content
We'd like to access an existing asset from Dungeon Architect plugin's content folder and we need to configure the Content Browser
to show these assets

On the top right of the Content Browser window, click the `Settings` button

![](A-04A1.jpg)

![](A-04A2.png)

## Assign Theme

A theme file defines the assets to use to build the dungeon.  Assign an existing theme to the dungeon actor

Select the dungeon actor and inspect the Details panel

Add a new Theme array entry by clicking the plus icon.
 
![](A-03.png)


Search for ``candy`` and select the candy theme

![](A-04.png)

![](A-04A4.png)


## Build Dungeon

* Select the Dungeon actor and inspect the Details Panel
* Click ``Build Dungeon`` button to generate the dungeon

![](A-05.png)

![](A-06.jpg)

## Randomize Dungeon

 * Select the Dungeon actor and inspect the Details Panel
 * Click ``Randomize Seed``
 * Click ``Build Dungeon`` to generate a new dungeon with a different layout
 


![](A-07.png)

![](A-08.jpg)

The ``Randomize Seed`` button is a helper function which simply changes the ``Seed`` value in the dungeon configuration.  Changing the ``Seed`` value changes the layout of the dungeon.    If you assign a random value to a seed and build, you'll get a new dungeon layout

![](A-09.png)
   
## Organization

When you build a dungeon, all the spawned dungeon actors are placed under a folder named after the dungeon actor's label

![](A-10.png)


 


