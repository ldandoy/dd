import json
import os

races = {}
pathFile = os.path.join('Datas', 'Races', "Races.json") 
with open(pathFile) as json_file:
    races = json.load(json_file)


class PointCharacter:
    max = 10
    maxPoint = 5
    indexPoint = 0
    currentPoint = maxPoint

    def __init__(self, label, race):
        self.race = race
        self.points =  races[race]
        self.addedPoints = {
            "force": 0,
            "dexterite": 0,
            "intelligence": 0,
            "charisme": 0,
            "constitution": 0,
            "sagesse": 0,
            "vitesse": 0,
        }
        self.label = label
        self.updateCurrentPoint()
    
    def getPointsFor(self, key):
        return self.addedPoints[key] + self.points[key]

    def updateCurrentPoint(self):
        self.currentPoint = self.maxPoint - self.indexPoint
        self.label.config(text="Point restants " + str(self.currentPoint))

    def getSommesPoints(self, who="strenght") -> int:
        return self.points[who] + self.addedPoints[who]

    def increment(self, who="strenght") -> bool:
        if self.indexPoint < self.maxPoint and self.getSommesPoints(who) < self.max:
            self.indexPoint += 1
            self.addedPoints[who] += 1
            self.updateCurrentPoint()
            return True
        return False

    def decrement(self, who="strenght") -> bool:
        if self.indexPoint > 0:
            self.indexPoint -= 1
            self.addedPoints[who] -= 1
            self.updateCurrentPoint()
            return True
        return False
