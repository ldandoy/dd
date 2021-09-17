from Utils.loadJson import LoadJson
from random import *


class Room:

    j = LoadJson()
    generatedrooms = []

    def __init__(self):
        # Generating a number that is going to determinate the number of rooms in the quest
        generatenbrooms = randint(3, 10)

        # Generating a number that is going to determinate the type of each room
        for i in range(generatenbrooms):
            randomtype = randint(1, 4)
            self.generatedrooms.append(randomtype)

    #for i in generatedrooms:
    #    if (i = 1):
    #        couloir
    #        self.data = j.load('Datas/Rooms/')
    #    if (i = 2):
    #        trésor
    #        self.data = j.load('Datas/Rooms/')
    #    if (i = 3):
    #        rencontre
    #        self.data = j.load('Datas/Rooms/')
    #    if (i = 4):
    #        rien
    #        self.data = j.load('Datas/Rooms/')
