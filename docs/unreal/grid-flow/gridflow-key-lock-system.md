# Key-Lock System

## Setup

The  Key and Lock actors that were spawned by the theme engine would have the `Item Metadata` filled up by Dungeon Architect, provided the actor has the ``Dungeon Flow Item Metadata`` component attached to it

In the sample, the Key and Lock blueprints has the above component added to it

![Key blueprint](E-101.png)

![Lock blueprint](E-102.png)


When these actors are spawned in the scene, the item information will be filled in.   This includes the `Item Id`, list of references to other items (like keys referencing all the other lock ids it can open)


![](E-103.jpg)

Key Metadata

![Lock Metadata](E-104.jpg)


Notice the Key metadata has a reference to the red locked door's id

![](E-105.jpg)


## Sample

Try out the Game Sample from the Launch Pad. Navigate to ``Launch Pad > Showcase > Legacy > Samples > Grid Flow Builder > Grid Flow Game > Clone Scene``

![](E-106.jpg)


The GridFlow game sample contains a working example of how you can implement a key lock system. There are many ways of implementing this, this sample shows one such way.

The Sample has the following scripts:

* Inventory: Saves the picked up keys in the inventory
* LockedDoor: Blueprint function ``CanOpenDoor`` to check if the door can be opened. This is done by checking if the collided actor has an inventory. If so, it checks if the inventory contains a key that can open this locked door id

Check the door blueprint ``Dungeon Architect Content > Builders > GridFlowContent > Art > Blueprints >  Locks > BP_GFT_LockBase > CanOpenDoor``
