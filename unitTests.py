import unittest
from tests import abstractNodeTest
from tests import aStarQueueTest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromModule(abstractNodeTest))
    suite.addTest(unittest.TestLoader().loadTestsFromModule(aStarQueueTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)