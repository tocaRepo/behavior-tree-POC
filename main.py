import py_trees
import py_trees.display
import time
from behaviours.drink import DrinkWater
from behaviours.thirsty import CheckThirst
import py_trees.blackboard as bb

# create a new instance of the blackboard
blackboard = bb.Blackboard()

# set a value on the blackboard
# set a variable on the blackboard
blackboard.set("thirsty_level", 20)
# Create a root node for the behavior tree
# In this example, we set the memory parameter of the Sequence node to True. This tells the Sequence node to use memory to store the state of its children. If we set memory to False, the Sequence node would not store any state and always start executing its children from the beginning.
root_node = py_trees.composites.Sequence(name="Root", memory=True)

check_thirst = CheckThirst()
drink_water = DrinkWater()
root_node.add_children([check_thirst, drink_water])

behavior_tree = py_trees.trees.BehaviourTree(root_node)


# Generate the XHTML tree with status shown
xhtml_tree = py_trees.display.xhtml_tree(behavior_tree.root, show_status=True)
unicode = py_trees.display.unicode_tree(behavior_tree.root, show_status=True)

# Write the XHTML tree to a file
with open("my_behavior_tree.xhtml", "w") as f:
    f.write(xhtml_tree)

# Write the XHTML tree to a file
with open("unicode.txt", "w") as f:
    f.write(unicode)
# Print the behavior tree to the console

index=0
while(True):
    # Print the behavior tree to the console
    status = behavior_tree.tick()

    # Print the status
    print(f"Iteration {index+1}: {status}")
    print(py_trees.display.unicode_tree(
        behavior_tree.root, show_status=True
    ))
    print(py_trees.display.unicode_blackboard(blackboard.keys()))
    blackboard.set("thirsty_level", blackboard.get("thirsty_level")+2)
    index=index+1
    time.sleep(0.5)
