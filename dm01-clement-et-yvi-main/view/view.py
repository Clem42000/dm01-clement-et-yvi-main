from contract.iview import IView


class View(IView):
    def display(self, message: str):
        print(message)