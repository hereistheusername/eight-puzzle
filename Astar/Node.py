from base import Node

# the node should store the state and the path to this state
# every node should be able to store the path to current state

class AStarNode(Node.AbstractNode):
    def __init__(self, state):
        self.state = state
        self.cumulative_cost = 0
        self.path = []

    def __inherit(self, child_node, operator):
        if child_node is None:
            return None
        # inherit cost
        child_node.cumulative_cost += self.cumulative_cost
        # add cost of operator
        child_node.cumulative_cost += operator.get_cost()
        # inherit path
        child_node.path += self.path
        # add new operation
        child_node.path.append(operator)
        return child_node

    # operators are moving blank to 4 directions
    # first, get the coordinate of the blank
    # second, check if 4 neighbor coordinates are valid
    # if valid, exchange the blank with the number in that position
    # otherwise, do not do that
    # return a list of valid nodes after operations
    def expand(self, operators):
        # ret = [o.operate(self) for o in operators]
        ret = [ self.__inherit(o.operate(self), o) for o in operators]
        return [e for e in ret if e]


    def get_current_state(self):
        return self.state
