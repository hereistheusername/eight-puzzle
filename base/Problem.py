from abc import ABC, abstractmethod

class AbstractProblem(ABC):

    # test if given state is the goal state    
    @abstractmethod
    def goal_test(self, state):
        pass

    # return the initial state
    @abstractmethod
    def get_initial_state(self):
        pass

    # return the goal state
    @abstractmethod
    def get_goal_state(self):
        pass

    # return all operators
    @abstractmethod
    def get_operators(self):
        pass