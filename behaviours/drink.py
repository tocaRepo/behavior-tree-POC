import py_trees
import py_trees.blackboard as bb

# create a new instance of the blackboard

class DrinkWater(py_trees.behaviour.Behaviour):
    def __init__(self, name="Drink Water"):
        super().__init__(name=name)
        self.blackboard = bb.Blackboard()
        
        
    def update(self):
        if self.blackboard.get("thirsty_level") > 50:
            self.blackboard.set("thirsty_level",self.blackboard.get("thirsty_level")-10)
            print("Drinking water. thirsty_level is now: {}".format(self.blackboard.get("thirsty_level")))
            return py_trees.common.Status.SUCCESS
        else:
            print("not too thirsty")
            return py_trees.common.Status.FAILURE
