import unittest
from tests import abstractNodeTest
from tests import aStarQueueTest
from tests import aStarProblemTest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromModule(abstractNodeTest))
    suite.addTest(unittest.TestLoader().loadTestsFromModule(aStarQueueTest))
    suite.addTest(unittest.TestLoader().loadTestsFromModule(aStarProblemTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)