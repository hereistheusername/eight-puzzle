import unittest
import numpy as np
from Astar import Problem
from Astar import Operators
from Astar.Node import AStarNode

class AStarProblemTestCase(unittest.TestCase):
    def test_functionality(self):
        AStarNode.h = (lambda n: 0)
        initial_state = np.array(
            [[1, 2, 3],
            [4, 5, 6],
            [7, 0, 8] ]
        )
        goal_state = np.array(
            [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0] ]
        )
        operators = [
            Operators.Move_Blank_left('Move Blank left', 1),
            Operators.Move_Blank_right('Move Blank right', 1),
            Operators.Move_Blank_up('Move Blank up', 1),
            Operators.Move_Blank_down('Move Blank down', 1)
        ]

        problem = Problem.AStarProblem(initial_state,
                                        goal_state,
                                        operators)
        self.assertTrue( (initial_state == problem.get_initial_state()).all() )
        self.assertTrue( (goal_state == problem.get_goal_state()).all() )

        self.assertFalse( problem.goal_test(initial_state))
