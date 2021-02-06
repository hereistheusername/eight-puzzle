from base import Node

# the node should store the state and the path to this state
# every node should be able to store the path to current state

class AStarNode(Node.AbstractNode):
    def __init__(self, state, operation=None):
        self.state = state
        if operation is None:
            self.cumulative_cost = 0
            self.path = []
        else:
            self.cumulative_cost = operation.get_cost()
            self.path = [operation]

    # child node inherits from parent node, then return itself
    def __inherit(self, parent_node):
        # inherit cost
        self.cumulative_cost += parent_node.cumulative_cost
        # inherit path
        self.path += parent_node.path
        return self

    # operators are moving blank to 4 directions
    # first, get the coordinate of the blank
    # second, check if 4 neighbor coordinates are valid
    # if valid, exchange the blank with the number in that position
    # otherwise, do not do that
    # return a list of valid nodes after operations
    def expand(self, operators):
        ret = [o.operate(self) for o in operators]
        # e represents a valid node, let it inherit from parent
        return [ e.__inherit(self) for e in ret if e]


    def get_current_state(self):
        return self.state
