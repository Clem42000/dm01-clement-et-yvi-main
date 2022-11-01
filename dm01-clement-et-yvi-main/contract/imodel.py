from abc import ABC, abstractmethod


class IModel(ABC):
        @abstractmethod
        def getnumber(self) -> str:
            ...
