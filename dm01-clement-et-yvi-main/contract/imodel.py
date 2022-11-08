from abc import ABC, abstractmethod


class IModel(ABC):
    @abstractmethod
    def getTitre(self)->int:
        ...
    @abstractmethod
    def getNumber(self)-> int:
        ...
    @abstractmethod
    def getEndNumber(self)-> int:
        ...
    @abstractmethod
    def setUserChoice(self)-> None:
        ...

    @abstractmethod
    def getUserChoice(self) -> int:
        ...
    @abstractmethod
    def getNombreEssaie(self):
        ...
    @abstractmethod
    def getEssaiemoins(self)->int:
        ...

    @abstractmethod
    def getEnd(self)->int:
        ...
