from Utils.load_json import LoadJson
from random import *


class Room:

    j = LoadJson()
    generatedRooms = []
    donjon = []
    monstersList = ["gobelin", "orc", "bouftou"]
    randomMonsters = []
    monsters = []
    bossList = ["meulou", "crocabulia", "moon"]
    randomBoss = randint(0, 2)
    boss = None;

    def __init__(self):
        # Génération d'un chiffre aléatoires pour déterminer le nombre de salles dans le donjon
        generateNbRooms = randint(3, 10)

        # Génération d'un chiffre aléatoire pour déterminer la nature de chaque salle
        for i in range(generateNbRooms):
            randomType = 0
            randomType = randint(1, 4)
            if len(self.generatedRooms) >= 2:
                if 2 not in self.generatedRooms[-2:]:
                    randomType = 2
            if i == range(generateNbRooms)[-1]:
                randomType = 5
            self.generatedRooms.append(randomType)

        # Chargement de chaque salle
        for i in self.generatedRooms:
            if i == 1:
                self.donjon.append(self.j.load('Datas/Rooms/couloir.json'))
            elif i == 2:
                self.randomMonsters.append(randint(0, (len(self.monstersList) - 1)))
                self.donjon.append(self.j.load('Datas/Rooms/fight.json'))
            elif i == 3:
                self.donjon.append(self.j.load('Datas/Rooms/nothing.json'))
            elif i == 4:
                self.donjon.append(self.j.load('Datas/Rooms/tresor.json'))
            elif i == 5:
                self.boss = self.bossList[self.randomBoss]
                self.donjon.append(self.j.load('Datas/Rooms/bossfight.json'))

        for i in self.randomMonsters:
            self.monsters.append(self.monstersList[i])
