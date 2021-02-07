import numpy as np
from base import Operator
from Astar import Node

class Move_Blank_left(Operator.AbstractOperator):

    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def get_cost(self):
        return self.cost

    def get_name(self):
        return self.name

    def operate(self, node):
        # 0 represents blank
        blank = list(zip(*np.where( node.get_current_state() == 0)))
        x, y = blank[0]
        yy = y - 1
        # generate new state if this operation is valid
        if yy >= 0:
            state = np.copy(node.get_current_state())
            state[x,y], state[x,yy] = state[x,yy], state[x,y]
            return Node.AStarNode(state, self)
        else:
            return None

    def __str__(self):
        return self.name

class Move_Blank_right(Move_Blank_left):
    def __init__(self, name, cost):
        super().__init__(name, cost)

    def operate(self, node):
        blank = list(zip(*np.where( node.get_current_state() == 0)))
        x, y = blank[0]
        yy = y + 1
        x_size, y_size = np.shape(node.get_current_state())
        if yy < y_size:
            state = np.copy(node.get_current_state())
            state[x,y], state[x,yy] = state[x,yy], state[x,y]
            return Node.AStarNode(state, self)
        else:
            return None



class Move_Blank_up(Move_Blank_left):
    def __init__(self, name, cost):
        super().__init__(name, cost)
    
    def operate(self, node):
        blank = list(zip(*np.where( node.get_current_state() == 0)))
        x, y = blank[0]
        xx = x - 1
        if xx >= 0:
            state = np.copy(node.get_current_state())
            state[x,y], state[xx, y] = state[xx, y], state[x, y]
            return Node.AStarNode(state, self)
        else:
            return None


class Move_Blank_down(Move_Blank_left):
    def __init__(self, name, cost):
        super().__init__(name, cost)
    
    def operate(self, node):
        blank = list(zip(*np.where( node.get_current_state() == 0)))
        x, y = blank[0]
        xx = x + 1
        x_size, y_size = np.shape(node.get_current_state())
        if xx < x_size:
            state = np.copy(node.get_current_state())
            state[x,y], state[xx, y] = state[xx, y], state[x, y]
            return Node.AStarNode(state, self)
        else:
            return None
