import unittest
import numpy as np
from Astar import Problem

class AStarProblemTestCase(unittest.TestCase):
    def test_functionality(self):
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
            ("Move Blank left", 1),
            ("Move Blank right", 1),
            ("Move Blank up", 1),
            ("Move Blank down", 1)
        ]

        problem = Problem.AStarProblem(initial_state,
                                        goal_state,
                                        operators)
        self.assertTrue( (initial_state == problem.get_initial_state()).all() )
        self.assertTrue( (goal_state == problem.get_goal_state()).all() )

        self.assertFalse( problem.goal_test(initial_state))
