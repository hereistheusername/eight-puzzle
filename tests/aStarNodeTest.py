import unittest
import numpy as np
from Astar.Node import AStarNode
from Astar.Operators import Move_Blank_left,Move_Blank_right,Move_Blank_up,Move_Blank_down

class AStarNodeTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.move_left = Move_Blank_left('Move_Blank_left', 1)
        self.move_right = Move_Blank_right('Move_Blank_right', 1)
        self.move_up = Move_Blank_up('Move_Blank_up', 1)
        self.move_down = Move_Blank_down('Move_Blank_down', 1)
        self.case1 = AStarNode(np.array([[1,2,3],
                                        [4,0,6],
                                        [7,5,8]]))
        self.case2 = AStarNode(np.array([[1,2,3],
                                        [4,8,0],
                                        [7,6,5]]))
        self.operators = [self.move_left, self.move_right, self.move_up, self.move_down]
        self.case1_expected = [
            AStarNode(np.array([[1,2,3],
                    [0,4,6],
                    [7,5,8]])),
            AStarNode(np.array([[1,2,3],
                    [4,6,0],
                    [7,5,8]])),
            AStarNode(np.array([[1,0,3],
                    [4,2,6],
                    [7,5,8]])),
            AStarNode(np.array([[1,2,3],
                    [4,5,6],
                    [7,0,8]]))
        ]
        self.case2_expected = [
            AStarNode(np.array([[1,2,3],
                    [4,0,8],
                    [7,6,5]])),
            AStarNode(np.array([[1,2,0],
                    [4,8,3],
                    [7,6,5]])),
            AStarNode(np.array([[1,2,3],
                    [4,8,5],
                    [7,6,0]]))
        ]

    def test_getters(self):
        state = np.array([[1,2,3],
                        [4,0,6],
                        [7,5,8]])
        self.assertTrue( (state == self.case1.get_current_state()).all())

    def test_expand(self):
        case1_expanded = self.case1.expand(self.operators)
        self.assertEqual(len(case1_expanded), 4)
        for i in range(0, len(self.case1_expected)):
            # check new node
            self.assertTrue( (case1_expanded[i].get_current_state() == self.case1_expected[i].get_current_state()).all())
            # check cumulative cost
            self.assertTrue( case1_expanded[i].cumulative_cost == 1)
            # check path
            self.assertTrue( case1_expanded[i].path[0] == self.operators[i])
        case2_expanded = self.case2.expand(self.operators)
        self.assertEqual(len(case2_expanded), 3)
        # pop out move_right
        self.operators.pop(1)
        for i in range(0, len(self.case2_expected)):
            self.assertTrue( (case2_expanded[i].get_current_state() == self.case2_expected[i].get_current_state()).all())
            self.assertTrue( case2_expanded[i].cumulative_cost == 1)
            self.assertTrue( case2_expanded[i].path[0] == self.operators[i])
