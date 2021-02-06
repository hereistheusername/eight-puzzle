from base import Node

# the node should store the state and the path to this state
# every node should be able to store the path to current state

class AStarNode(Node.AbstractNode):
    def __init__(self, state, cumulative_cost=0, path=[]):
        self.state = state
        self.cumulative_cost = cumulative_cost
        self.path = path

    # def __inherit(self, parentNode, operator):
    #     self.cumulative_cost = parentNode.cumulative_cost
    #     self.cumulative_cost += operator[1]
    #     self.path = parentNode.path
    #     self.path.append(operator)

    # operators are moving blank to 4 directions
    # first, get the coordinate of the blank
    # second, check if 4 neighbor coordinates are valid
    # if valid, exchange the blank with the number in that position
    # otherwise, do not do that
    # return a list of valid nodes after operations
    def expand(self, operators):
        ret = [o.operate(self) for o in operators]
        return [e for e in ret if e]


    def get_current_state(self):
        return self.state
