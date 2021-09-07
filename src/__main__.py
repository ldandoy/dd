"""MainWindow.py

Start file of the project
"""


from Utils.Perso import Perso
from Story.initialQuest import InitialQuest
from Window.LoadWindow import LoadWindow


if __name__ == '__main__':
    print("Bienvenue dans Donjon & Dragon")
    list_perso = Perso.listPerso()
    print(list_perso)

    mw = LoadWindow()
    # initialQuest = InitialQuest()
    # initialQuest.welcome()
