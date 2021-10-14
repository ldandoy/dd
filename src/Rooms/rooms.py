from Utils.loadJson import LoadJson
from random import *


class Room:

    j = LoadJson()
    generatedrooms = []

    def __init__(self):
        # Génération d'un chiffre aléatoires pour déterminer le nombre de salles dans le donjon
        generatenbrooms = randint(3, 10)

        # Génération d'un chiffre aléatoire pour déterminer la nature de chaque salle
        for i in range(generatenbrooms):
            randomtype = randint(1, 4)
            self.generatedrooms.append(randomtype)

        # Chargement de chaque salle
        #for i in generatedrooms:
        #    if (i = 1):
        #        couloir
        #        self.data = j.load('Datas/Rooms/couloir.json')
        #    if (i = 2):
        #        trésor
        #        self.data = j.load('Datas/Rooms/')
        #    if (i = 3):
        #        rencontre
        #        self.data = j.load('Datas/Rooms/')
        #    if (i = 4):
        #        rien
        #        self.data = j.load('Datas/Rooms/')
