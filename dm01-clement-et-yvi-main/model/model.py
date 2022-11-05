from contract.imodel import IModel
import random

class Model (IModel):

    __nombrerandom: int
    __nombreessaie: int
    __nombrechoisit: int
    __findepartie = str
    __entrezvaleur : str

    def __init__(self):
        self.__nombreessaie= 10
        self.__nombrerandom = 0
        self.__nombrechoisit = 0
        self.__findepartie = str
        self.__entrezvaleur =str

    def entreznombre(self):
       self.__entrezvaleur = "entrez une valeur"
       return self.__entrezvaleur

    def nombrechoisit(self):
        self.__nombrechoisit = input()
        print("la valeur choisit est :", self.__nombrechoisit)
        return self.__nombrechoisit

    def getnumber(self):
        self.__nombrerandom = random.randint(1, 100)
        return self.__nombrerandom

    def jeu(self):
        if self.__nombreessaie == 0:
            self.__findepartie = "Perdu"
            return self.__findepartie




