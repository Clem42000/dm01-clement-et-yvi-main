from contract.iview import IView


class View(IView):

    def display(self, message: str):
        print(message)

    def nombreChoisit(self):
        userChoice = -1
        while userChoice < 1 or userChoice > 100 :
            print("Choisir un nombre entre 1 et 100")
            userChoice = int(input())
        return userChoice
