"""main_window.py

Start file of the project
"""
import json

from Monster.monster import Monster
from Window.main_window import MainWindow


if __name__ == '__main__':
    print("Bienvenue dans Donjon & Dragon")
    mainWindow = MainWindow()
    # initialQuest = InitialQuest()
    # initialQuest.welcome()

    monster = Monster('gobelin.json')
    