from abc import ABC, abstractmethod


class ItemABC(ABC):
    @abstractmethod
    def get_info(self):
        pass
