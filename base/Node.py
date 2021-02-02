from abc import ABC, abstractmethod
class AbstractNode(ABC):

    # expand node
    # return a list of nodes expanded according to operators
    @abstractmethod
    def expand(self, operators):
        pass

    # return current state
    @abstractmethod
    def get_current_state(self):
        pass