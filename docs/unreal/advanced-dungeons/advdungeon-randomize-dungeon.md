# Randomize Dungeons

Dungeon Architect can build a new dungeon everytime you play.  A configuration value called the `Seed` controls the randomness. 
Changing this to another number (say from a value `0` to `1234`) would produce a different dungeon. 

So if you want to have a different dungeon every time you play, change this value to some random number

Alternatively, if you want to generate the same dungeon (e.g. in a multiplayer game, you'd want all the clients to generate the exact same dungeon), you'd pass the same seed to every client

Select the Dungeon actor and open the level blueprint.   Right click and create the `Dungeon1` node (referencing the selected actor)

![Randomize Dungeon Seed](X-randomize_seed.png)

Here, we grab the config object of the dungeon actor and change the seed variable to a random value, before calling build


