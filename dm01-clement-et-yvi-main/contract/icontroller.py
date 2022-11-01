from abc import ABC, abstractmethod

from contract.imodel import IModel
from contract.iview import IView


class IController(ABC):
    @abstractmethod
    def getView(self) -> IView:
        ...

    @abstractmethod
    def getModel(self) -> IModel:
        ...

    @abstractmethod
    def start(self):
        ...
