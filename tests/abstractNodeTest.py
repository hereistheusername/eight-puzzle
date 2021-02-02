import unittest
from base import Node

class NodeMock(Node.AbstractNode):
    def __init__(self, initial_state):
        self.state = initial_state

    def expand(self, operators):
        ret = [NodeMock(operator) for operator in operators ]
        return ret

    def get_current_state(self):
        return self.state

class AbstractNodeTestCase(unittest.TestCase):
    
    def test_get_current_state(self):

        initial_state = 1
        node = NodeMock(initial_state)
        self.assertEqual(initial_state, node.get_current_state())

    def test_expand(self):
        initial_state = 1
        node = NodeMock(initial_state)

        operators = [x for x in range(2,5)]
        nodes = node.expand(operators)

        i = 0
        for node in nodes:
            self.assertEqual(node.get_current_state(), operators[i])
            i += 1
        
if __name__ == '__main__':
    unittest.main(verbosity=1)