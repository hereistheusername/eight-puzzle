from base.Context import AbstractContext
from Astar.Queue import AStarQueue

class AStarContext(AbstractContext):

    def __init__(self, problem, queue, node, g, h):
        self.problem = problem
        self.queue = queue
        self.node = node
        self.g = g
        self.h = h

        # f(n) = g(n) + h(n)
        def f(n):
            return g(n)+h(n)
        self.sort_method = f

        self.expand_counts = 0
        self.maximum_size_of_queue = 0
        
    def get_problem(self):
        return self.problem
    
    def get_queue_function(self):
        def queue_function(state):
            # because we have to keep maximum number of nodes in the queue
            # so we need to keep a reference of queue here
            self.queue_reference = AStarQueue(self.node(state), self.sort_method)
            return self.queue_reference
        return queue_function

    def onInit(self):
        print(
            'Expanding state\n',
            str(self.problem.initial_state),
            '\n'
        )

    def onExpand(self, node):
        self.expand_counts += 1

        if len(self.queue_reference.nodes) > self.maximum_size_of_queue:
            self.maximum_size_of_queue = len(self.queue_reference.nodes)

        print(
            'The best state to expand with a g(n) = ',
            str(self.g(node)),
            ' and h(n) = ',
            str(self.h(node)),
            ' is ...\n',
            str(node.get_current_state()),
            'Expanding this node...\n'
        )

    def onSuccess(self, node):
        print(
            'Goal!!\n\n',
            'To solve this problem the search algorithm expanded a total of ',
            str(self.expand_counts),
            ' nodes.\n',
            'The maximum number of nodes in the queue at any one time was ',
            str(self.maximum_size_of_queue),
            '\n',
            'The depth of the goal node was ',
            str(len(node.path)),
            '\n\n Solution:'
        )

        for operation in node.path:
            print(operation)