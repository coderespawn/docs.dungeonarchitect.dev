---
title: "Landscape Transformer"
sidebar_position: 7
---

Using the Landscape Transformer, you can modify a landscape's height and weights (textures) around the dungeon's layout

<video src="https://www.youtube.com/watch?v=9MI9IzNytuY" />

The landscape transformer is implemented as a event listener, so you'll need to register it in the Dungeon actor's event listener list under the Advanced category


![Landscape Transformer](../images/unreal/tutorial/H/H-landscape_transformer.png)

After setting the landscape transformer, expand it and set the Landscape you'd wish to modify


![Landscape Transformer](../images/unreal/tutorial/H/H-landscape_transformer2.png)

Under the Layers array, add two entries

The first entry should be the Layer Info for filling the entire area
The second entry is for the inner path way.

You would have already created these layer info assets while creating the landscape and setting up the material

To find where you layer info is, Navigate to the Landscape tab > Paint section.  There you'd see entries for each layer that was defined in your material.   If you didn't create a layer info yet, create one or click the Find icon to find where it is.  Then assign the appropriate layer


![Landscape Transformer](../images/unreal/tutorial/H/H-landscape_transformer_layer.png)
