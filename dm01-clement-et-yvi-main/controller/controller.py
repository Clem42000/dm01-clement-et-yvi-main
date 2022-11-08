from contract.icontroller import IController
from contract.imodel import IModel
from contract.iview import IView


class Controller(IController):
    __view: IView
    __model: IModel

    def __init__(self, view: IView, model: IModel,):
        self.__view = view
        self.__model = model

    def getView(self) -> IView:
        return self.__view

    def getModel(self) -> IModel:
        return self.__model

    def start(self):
        print(self.__model.getTitre())
        self.__model.getNumber()
      #  self.__view.display(self.__model.getEndNumber())   ---> Permet de voir la solution s'afficher
        self.__model.getNombreEssaie()

        while self.__model.getNombreEssaie() >0 :

            self.__model.setUserChoice(self.__view.nombreChoisit())

            if self.__model.getEndNumber() != self.__model.getUserChoice():
                self.__model.getEssaiemoins()
                if self.__model.getEndNumber() < self.__model.getUserChoice():
                    self.__view.display("Trop grand !")
                if self.__model.getEndNumber() > self.__model.getUserChoice():
                    self.__view.display("Trop petit !")

            if self.__model.getEndNumber() == self.__model.getUserChoice():
                print ("Gagné !")
                self.__model.getEnd()

        if self.__model.getNombreEssaie() == 0:
            print("Vous avez perdu")

        if self.__model.getNombreEssaie() ==-1 :
            print("Vous avez gagné !")
