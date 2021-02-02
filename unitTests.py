import unittest
from tests import abstractNodeTest

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromModule(abstractNodeTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)