from abc import ABC, abstractmethod
class AbstractContext(ABC):
    @abstractmethod
    def onExpand(self, node):
        pass

    @abstractmethod
    def onSuccess(self, node):
        pass