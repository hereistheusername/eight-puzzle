import numpy as np
import unittest
from Astar.utils import misplaced_distance, manhattan_distance

class AStarUtilsTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.goal = np.roll(np.arange(9), -1).reshape(3,3)
        self.mis_case = np.array([[1,2,3],
                                [4,5,6],
                                [7,0,8] ])
        self.manha_case = np.array([[3,2,8],
                                    [4,5,6],
                                    [7,1,0]])

    def test_misplaced_distance(self):
        self.assertEqual(misplaced_distance(self.mis_case, self.goal), 1)
        self.assertEqual(misplaced_distance(self.mis_case, self.mis_case), 0)
        self.assertEqual(misplaced_distance(self.goal, self.goal), 0)

    def test_manhattan_distance(self):
        self.assertEqual(manhattan_distance(self.manha_case, self.goal), 8)
        self.assertEqual(manhattan_distance(self.manha_case, self.manha_case), 0)
        self.assertEqual(manhattan_distance(self.goal, self.goal), 0)