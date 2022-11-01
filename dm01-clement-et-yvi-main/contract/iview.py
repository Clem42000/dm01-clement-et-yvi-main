from abc import ABC, abstractmethod


class IView(ABC):
    @abstractmethod
    def display(self, message) -> None:
        ...
