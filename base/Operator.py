from abc import ABC, abstractmethod

# this abstract object defines the operation
class AbstractOperator(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_cost(self):
        pass

    # after operation, returns a node
    @abstractmethod
    def operate(self, node):
        pass