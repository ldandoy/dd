# The start of the Project
from Utils.Perso import LoadPerso
from Story.initialQuest import InitialQuest

if __name__ == '__main__':
    print("Bienvenue dans Donjon & Dragon")
    LoadPerso.load()

    initialQuest = InitialQuest()
    initialQuest.welcome()
