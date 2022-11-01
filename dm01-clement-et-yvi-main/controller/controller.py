from contract.icontroller import IController
from contract.imodel import IModel
from contract.iview import IView


class Controller(IController):
    __view: IView
    __model: IModel

    def __init__(self, view: IView, model: IModel):
        self.__view = view
        self.__model = model

    def getView(self) -> IView:
        return self.__view

    def getModel(self) -> IModel:
        return self.__model

    def start(self):
        print("Not yet implemented")
