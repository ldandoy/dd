from Utils.loadJson import LoadJson


class Pnj:
    data = []

    def __init__(self, file):
        j = LoadJson()
        self.data = j.load('Datas/PNJ/Darko.json')

    def getInfo(self):
        return self.data
