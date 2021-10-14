from Utils.loadJson import LoadJson
from random import *


class Room:

    j = LoadJson()
    generatedrooms = []
    donjon = []

    def __init__(self):
        # Génération d'un chiffre aléatoires pour déterminer le nombre de salles dans le donjon
        generatenbrooms = randint(3, 10)

        # Génération d'un chiffre aléatoire pour déterminer la nature de chaque salle
        for i in range(generatenbrooms):
            randomtype = randint(1, 4)
            if i == range(generatenbrooms)[-1]:
                randomtype = 5
            self.generatedrooms.append(randomtype)

        # Chargement de chaque salle
        for i in self.generatedrooms:
            if i == 1:
                self.donjon.append(self.j.load('Datas/Rooms/couloir.json'))
            elif i == 2:
                self.donjon.append(self.j.load('Datas/Rooms/fight.json'))
            elif i == 3:
                self.donjon.append(self.j.load('Datas/Rooms/nothing.json'))
            elif i == 4:
                self.donjon.append(self.j.load('Datas/Rooms/tresor.json'))
            elif i == 5:
                self.donjon.append(self.j.load('Datas/Rooms/bossfight.json'))
                