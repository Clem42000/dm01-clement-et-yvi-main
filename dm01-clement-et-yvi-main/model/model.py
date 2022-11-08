from contract.imodel import IModel
import random


class Model (IModel):

    __randomNumber = int
    __userChoice: int
    __nombreEssaies: int
    __user : str
    __rejouer: str
    __titre: str

    def __init__(self):
        self.__randomNumber = 0
        self.__nombreEssaies = 10
        self.__rejouer="oui"

    def getTitre(self)->str:
        self.__titre = "--------Bienvenue---------\nLe but est de trouver le nombre magique ! \nIl est caché entre 1 et 100 \nBon courage !\n "
        return self.__titre
    def getNumber(self) -> int:
        self.__randomNumber = random.randint(1,100)
    def getEndNumber(self)-> int:
        return self.__randomNumber

    def getUserChoice(self) -> int:
        return self.__userChoice

    def setUserChoice(self, userChoice) ->None :
        self.__userChoice = userChoice

    def getNombreEssaie(self) -> int:
        return self.__nombreEssaies

    def getEssaiemoins(self)->int:
        self.__nombreEssaies=self.__nombreEssaies-1
        return self.__nombreEssaies
    def getEnd(self)->int:
        self.__nombreEssaies =-1
        return self.__nombreEssaies

