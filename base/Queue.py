from abc import ABC, abstractmethod

class AbstractQueue(ABC):

    # return true if there is no node in the queue
    @abstractmethod
    def isEmpty(self):
        pass

    # remove front
    # return the removed front
    @abstractmethod
    def remove_front(self):
        pass

    # append a list of nodes
    @abstractmethod
    def queueing(self, expanded_nodes):
        pass