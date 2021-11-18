from Utils.loadJson import LoadJson
import os


class Stats:
    __stat = None

    def __init__(self):
        json = LoadJson()
        self.__stat = json.load(os.path.join('Datas', 'Stats', 'global.json'))

    def getStats(self):
        return self.__stat
