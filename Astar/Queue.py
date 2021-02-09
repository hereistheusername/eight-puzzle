# Due to that Uniform Cost Search is just A* with h(n) hardcoded to equal zero,
# only A* needs to be implemented

from base import Queue

class AStarQueue(Queue.AbstractQueue):

    # input the initial node to initialize the queue
    def __init__(self, initial_node, sort_method):
        # use a list to store nodes
        self.nodes = []
        self.nodes.append(initial_node)
        self.sort_method = sort_method

    def isEmpty(self):
        return (len(self.nodes) == 0)

    # nodes sort by estimate cost in ascending
    # the first node has the lowest cost
    def remove_front(self):
        minimum_front_index = 0
        minimum_estimate_cost = self.sort_method(self.nodes[minimum_front_index])
        for i in range(1, len(self.nodes)):
            current_estimate_cost = self.sort_method(self.nodes[i])
            if current_estimate_cost < minimum_estimate_cost:
                minimum_front_index = i
                minimum_estimate_cost = current_estimate_cost
        
        return self.nodes.pop(minimum_front_index)

    def queueing(self, expanded_nodes):
        self.nodes.extend(expanded_nodes)
        # self.sort_by_estimate_cost_to_goal()

    # the queue can still keep FIFO order, but nodes in the queue
    # should be sorted before removing the front
    def sort_by_estimate_cost_to_goal(self):
        self.nodes.sort(key=self.sort_method)

