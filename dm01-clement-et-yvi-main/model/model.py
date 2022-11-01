from contract.imodel import IModel
import random

class Model(IModel):

    __nombrerandom: int
    __nombreessaie: int

    def __init__(self):
        self.__nombreessaie=0
        self.__nombrerandom = 0

    def getnumber(self):
        self.__nombrerandom = random.randint(1, 100)
        return self.__nombrerandom


