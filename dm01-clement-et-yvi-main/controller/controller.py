from contract.icontroller import IController
from contract.imodel import IModel
from contract.iview import IView


class Controller(IController):
    __view: IView
    __model: IModel
    __nombre: int


    def __init__(self, view: IView, model: IModel,):
        self.__view = view
        self.__model = model
        self.__nombre = self.__model.getnumber()


    def getView(self) -> IView:
        return self.__view

    def getModel(self) -> IModel:
        return self.__model

    def start(self):
        self.__view.display(self.__model.getnumber())
        self.__view.display(self.__model.entreznombre())
        self.__model.nombrechoisit()

        if self.__model.__nombrechoisit() != self.__model.getnumber():
            print("Pas trouvé !")








