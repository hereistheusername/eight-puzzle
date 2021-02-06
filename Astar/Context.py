from base.Context import AbstractContext

class AStarContext(AbstractContext):

    def __init__(self, problem, operators, queue):
        self.problem = problem
        self.operators = operators
        self.queue = queue
        
    def onExpand(self, node):
        pass

    def onSuccess(self, node):
        pass