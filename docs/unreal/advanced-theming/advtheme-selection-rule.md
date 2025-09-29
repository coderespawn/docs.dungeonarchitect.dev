# Selection Rule

A selection rule is a blueprint class (or C++ class) that is used to decide if the current node is to be attached to the scene.  This rule replaces the default **Probability** property that is used for randomly deciding if visual node needs spawning based on a probability.

Selection rules gives you more power, when you need it.   In the rule's blueprint logic, you can query the dungeon model and determin if this node should be inserted into the scene

## Using Selection Rules
To assing an existing rule into the node, Check the **Use Selection Logic** property and select the rule you would like to attach to the node from the dropdown list


![Assign an existing Selection Rule](G-selection_rule_01a.png)

Create a new selection rule by creating a new blueprint class derived from the appropriate DungeonSelectorLogic.  It should match the builder you are targeting


![Create a new Selection Rule](G-create_rule_transform1.png)

Open up the blueprint and override the **Select Node** function. This function will be called by the engine and the logic you put here will let you decide if the node should to be selected


![Override function to define logic](G-selection_rule_04.png)

The selection can be combined with the Probability varaible by unchecking **Logic Overrides Probability**


![Combine selection logic with Probability variable](G-selection_rule_02b.png)

## Example #1

Here is an example of a selection logic that selects a node only if the sum of their X and Y positions are even numbers (logic for a checkerboard pattern)


![Override function to define logic](G-selection_rule_05.png)

And the result after applying this rule to the ground node:


![Custom selection rule attached to a mesh node](G-selection_rule_06.jpg)

You can add more visual nodes and experiment with the **Consume on Attach** parameter to get interesting results


![Multiple visual nodes working together](G-selection_rule_07.jpg)

In the above example, the first node has **Consume on Attach** checked.  So if your blueprint logic selects the node, the sandstone mesh will be inserted and the execution stops.   However if the selection node doesn't select the node, the execution will always proceed to the next node and execute the mesh which inserts a clay brick mesh


![](G-selection_rule_eg1_1.jpg)

In the above example, the selection rule is applied to the golden pillar.  But whenever it is selected, it stops execution because the **Consume on Attach** variable is set and doesn't build a ground mesh there.    Unchecking **Consume on Attach** on the first node lets the execution proceed even if it is inserted into the scene

![](G-selection_rule_eg1_2.jpg)



## Example #2
This example places a stone mesh on the ground, but only if the cell is inside a room (and not a corridor)


![Stone ground mesh selection only when inside rooms](G-selection_rule_eg2_1.jpg)


![Room selector logic](G-selection_rule_eg2_2.jpg)

The above Selection logic was attached to the stone mesh ground node so it gets selected only when the ground marker is inside a room

## Example #3
Ignore nodes that are near other markers.  This is very useful if you don't want to place blocking items near stairs, doors etc


![Query System](G-query_grid_near_marker_1.png)

![Query System](G-query_grid_near_marker_2.jpg)

