from Utils.loadJson import LoadJson
import os


class Monster:
    __monster = None

    def __init__(self, filename):
        self.base_folder = os.path.dirname(__file__)
        json = LoadJson()
        print(self.base_folder, filename)
        self.__monster = json.load(os.path.join(self.base_folder, '../../Datas/Monsters', filename))

        print(self.__monster)


    def getMonster(self):
        return self.__monster
