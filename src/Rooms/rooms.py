from Utils.loadJson import LoadJson


class Room:

    def __init__(self):
        j = LoadJson()
        self.data = j.load('Datas/Rooms/')
