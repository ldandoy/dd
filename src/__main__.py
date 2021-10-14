"""MainWindow.py

Start file of the project
"""
import json

from Utils.Perso import Perso
from Window.MainWindow import MainWindow



if __name__ == '__main__':
    print("Bienvenue dans Donjon & Dragon")
    list_perso = Perso.list_perso()
    print(list_perso)

    mainWindow = MainWindow()
    # initialQuest = InitialQuest()
    # initialQuest.welcome()
