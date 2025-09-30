---
title: "Spatial Constraints"
sidebar_position: 6
---

Spatial constraints are great of checking the state of nearby tiles and using it as a condition to place items on the scene

Spatial constraints are set in the theme graph's node.


![Spatial Constraints ](../images/unreal/tutorial/G/G-spatial_constraint_a.jpg)

In the above example, a statue mesh is added to the ground marker.    We want this to appear only on the corners and not on each tile

Select a mesh node and in the details panel, enable *Use Spatial Constraint*

Then select the spatial constraint type.  Since this is a ground mesh, it is surrounded by 3x3 tiles


![Spatial Constraints](../images/unreal/tutorial/G/G-spatial_constraint2.png)

Expand the spatial setup. Here you specify the rules of the adjacent tiles, whether it should be empty, occupied or should be ignored.   The rules will try to rotate to best fit the layout


![Spatial Constraints](../images/unreal/tutorial/G/G-spatial_constraint3.jpg)

With this setup, the statues spawn only at the corners

<iframe
    width="100%"
    height="540"
    src="https://www.youtube.com/embed/eL4C42A7rx4"
    frameBorder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowFullScreen
/>
