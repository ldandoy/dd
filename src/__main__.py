"""MainWindow.py

Start file of the project
"""
import json

from Utils.Perso import Perso
from Window.MainWindow import MainWindow
from Monster.Monster import Monster


if __name__ == '__main__':
    print("Bienvenue dans Donjon & Dragon")

    mainWindow = MainWindow()
    # initialQuest = InitialQuest()
    # initialQuest.welcome()

    monster = Monster('gobelin.json')
