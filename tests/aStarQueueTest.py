import unittest
from Astar import Queue

class AStarQueueTestCase(unittest.TestCase):
    def test_functionality(self):
        inital_node = 1
        expanded_nodes = [34, 2, 5, 76, 25]

        queue = Queue.AStarQueue(inital_node, (lambda x: x))

        self.assertFalse(queue.isEmpty())
        current_node = queue.remove_front()

        self.assertTrue(queue.isEmpty())
        queue.queueing(expanded_nodes)
        self.assertFalse(queue.isEmpty())

        current_node =  queue.remove_front()
        self.assertEqual(2, current_node)

if __name__ == '__main__':
    unittest.main(verbosity=1)