import py_trees
import py_trees.blackboard as bb
class CheckThirst(py_trees.behaviour.Behaviour):
    def __init__(self, name="Check Thirst"):
        super().__init__(name=name)
        self.blackboard = bb.Blackboard()
        
    def update(self):
        if self.blackboard.get("thirsty_level") > 70:
            print("Thirsty!")
            return py_trees.common.Status.SUCCESS
        else:
            print("Not thirsty:"+str(self.blackboard.get("thirsty_level")))
            return py_trees.common.Status.FAILURE
