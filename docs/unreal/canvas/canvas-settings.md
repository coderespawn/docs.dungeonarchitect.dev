<show-structure />

# Canvas Settings

## Preview Panel

The same dungeon canvas asset can be used for different types of dungeons (Grid, GridFlow, SGF, SnapMap, CellFlow etc).

Click the  `Preview Dungeon Settings` button

![image|690x46](../images/unreal/tutorial/Canvas/b2c80deaa2673f8797fca6ac0a0a16a1b5858382.png)

This opens up the preview dungeon settings. Change the builder type from here to visualize how your theme looks with different dungeon types

![image|585x500](../images/unreal/tutorial/Canvas/15c29118815393cb2bf636f130e1a9dcb89864c6.png)

![image|483x499](../images/unreal/tutorial/Canvas/08bcb148de0a5fdd4f2d200fdc264138e9fc178b.jpeg)

Click the Randomize Dungeon button to see how the dungeon looks with different layouts

![C018.png](../images/unreal/tutorial/Canvas/C018.png)

### Layout Draw Margin Percent

![image|557x56](../images/unreal/tutorial/Canvas/fce2dceadbffd5948abce021194c587eef59cf68.png)

![image|500x500](../images/unreal/tutorial/Canvas/db0701677b4f98d55ca6b602f1aca7c8e074fa67.jpeg)

We have a certain background and want the dungeon to fit within it.  So we'll give it a value of 50.  Adjust it according to your needs

![image|567x43](../images/unreal/tutorial/Canvas/a453c7b2c40da50d190d2df6cb60d449582708e4.png)

![image|499x499](../images/unreal/tutorial/Canvas/e63cfc340fb269aec1d1693af8ba000d92f9f4a7.jpeg)


## Dungeon Canvas Settings

Click the `Canvas Settings` icon on the toolbar

![C021.png](../images/unreal/tutorial/Canvas/C021.png)

![C022.png](../images/unreal/tutorial/Canvas/C022.png)

**Effects**: You can extend the system with your own advanced effects on top of it and manage the lifecycle of your custom textures yourself.   We use this to create voronoi maps on top of the dungeon and create an effect like this, where the size of the voronoi cell changes based on how close it is to the dungeon border.  This will be covered in detail in another section

![image|500x500](../images/unreal/tutorial/Canvas/d3685856653dcff8cb4c679efd3916fbe4692481.jpeg)

**Material Template Canvas**:   Change the master cavnas material, we won't change this, so leave it to the default value

**Material Template Fog of War**:  Provide your own custom fog of war material. Your custom material can change the color, texture etc.   (see below for a custom implementation)

### Custom fog of war Material

![image|690x353](../images/unreal/tutorial/Canvas/c58b1140523fff84fde3bd0502361f599410d804.png)

![image|533x500](../images/unreal/tutorial/Canvas/d8ef93744a5a5191bb9f3da794393d6f13cc97fc.jpeg)

![image|546x500](../images/unreal/tutorial/Canvas/c4883de7359434f5b8ce72a38c33c92e90dc20a1.jpeg)

In this example I copied over the template and added a bit of curl noise to the fog of war texture UV


Before: (Original template)

![image|390x499](../images/unreal/tutorial/Canvas/03691f71334738228a7b6b4155433b60ad3df787.png)

After curl noise:

![image|690x286](../images/unreal/tutorial/Canvas/21fb1646584ed667f74753d94097d6d941e7bee5.png)

Animate the curl noise by specifying time (instead of 0) in the `Append Vector` node

![image|673x500](../images/unreal/tutorial/Canvas/b8eec6de52e4e1caec4fb55baef9bea412a57ffc.png)


[M_NoisyCanvasFogOfWar.uasset](https://forums.dungeonarchitect.dev/uploads/short-url/iPO6GXGhIPKEPnHG36EOPLPGkeo.uasset) (25.1 KB)

