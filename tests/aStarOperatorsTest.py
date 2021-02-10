import unittest
import numpy as np
from Astar.Operators import Move_Blank_left, Move_Blank_right, Move_Blank_up, Move_Blank_down
from Astar.Node import AStarNode

class AStarOpeatorsTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        h = lambda n: 0
        g = lambda n: n.cumulative_cost
        self.move_left = Move_Blank_left('Move_Blank_left', 1)
        self.move_right = Move_Blank_right('Move_Blank_right', 1)
        self.move_up = Move_Blank_up('Move_Blank_up', 1)
        self.move_down = Move_Blank_down('Move_Blank_down', 1)
        self.case1 = AStarNode(np.array([[1,2,3],
                                        [4,0,6],
                                        [7,5,8]]), [], 0, 0, h)
        self.case2 = AStarNode(np.array([[1,2,3],
                                        [4,8,0],
                                        [7,6,5]]), [], 0, 0, h)

    def test_move_blank_left(self):
        state1 = self.move_left.operate(self.case1).get_current_state()
        expected_state1 = np.array([[1,2,3],
                                    [0,4,6],
                                    [7,5,8]])
        self.assertTrue( (expected_state1 == state1).all())

        state2 = self.move_left.operate(self.case2).get_current_state()
        expected_state2 = np.array([[1,2,3],
                                    [4,0,8],
                                    [7,6,5]])
        self.assertTrue( (expected_state2 == state2).all())

    def test_move_blank_right(self):
        state1 = self.move_right.operate(self.case1).get_current_state()
        expected_state1 = np.array([[1,2,3],
                                    [4,6,0],
                                    [7,5,8]])
        self.assertTrue( (expected_state1 == state1).all())

        state2 = self.move_right.operate(self.case2)
        expected_state2 = None
        self.assertTrue( (state2 == expected_state2))

    def test_move_blank_up(self):
        state1 = self.move_up.operate(self.case1).get_current_state()
        expected_state1 = np.array([[1,0,3],
                                    [4,2,6],
                                    [7,5,8]])
        self.assertTrue( (expected_state1 == state1).all())

        state2 = self.move_up.operate(self.case2).get_current_state()
        expected_state2 = np.array([[1,2,0],
                                    [4,8,3],
                                    [7,6,5]])
        self.assertTrue( (expected_state2 == state2).all())

        
    def test_move_blank_down(self):
        state1 = self.move_down.operate(self.case1).get_current_state()
        expected_state1 = np.array([[1,2,3],
                                    [4,5,6],
                                    [7,0,8]])
        self.assertTrue( (expected_state1 == state1).all())

        state2 = self.move_down.operate(self.case2).get_current_state()
        expected_state2 = np.array([[1,2,3],
                                    [4,8,5],
                                    [7,6,0]])
        self.assertTrue( (expected_state2 == state2).all())

    def test_getters(self):
        self.assertEqual( self.move_right.get_name(), 'Move_Blank_right')
        self.assertEqual( self.move_right.get_cost(), 1)
