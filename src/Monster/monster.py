from src.Utils.load_json import LoadJson
import os


class Monster:
    __monster = None

    def __init__(self, filename):
        json = LoadJson()
        self.__monster = json.load(os.path.join('Datas', 'Monsters', filename))

    def getMonster(self):
        return self.__monster
