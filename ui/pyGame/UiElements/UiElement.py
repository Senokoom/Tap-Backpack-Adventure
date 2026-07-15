from abc import ABC, abstractmethod

class UiElement(ABC):

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def update(self):
        pass