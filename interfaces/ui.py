from abc import ABC, abstractmethod

class UIInterface(ABC):
    @abstractmethod
    def display(self, garderie):
        pass
