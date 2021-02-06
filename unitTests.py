import unittest
from tests import abstractNodeTest
from tests import aStarQueueTest
from tests import aStarProblemTest
from tests import aStarOperatorsTest
from tests import aStarNodeTest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromModule(abstractNodeTest))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(aStarQueueTest))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(aStarProblemTest))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(aStarOperatorsTest))
    suite.addTests(unittest.TestLoader().loadTestsFromModule(aStarNodeTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)