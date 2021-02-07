from abc import ABC, abstractmethod
class AbstractContext(ABC):
    @abstractmethod
    def get_problem(self):
        pass

    @abstractmethod
    def get_queue_function(self):
        pass

    @abstractmethod
    def onInit(self):
        pass
    
    @abstractmethod
    def onExpand(self, node):
        pass

    @abstractmethod
    def onSuccess(self, node):
        pass