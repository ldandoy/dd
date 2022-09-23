class PointCharacter:
    max = 10
    maxPoint = 5
    indexPoint = 0
    currentPoint = maxPoint

    def __init__(self, label, defaultStats):
        self.points =  defaultStats
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
