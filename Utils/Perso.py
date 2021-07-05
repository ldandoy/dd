import os


class Perso:
    def __init__(self):
        pass

    @classmethod
    def load(cls):
        list = os.listdir('Datas/Perso')
        print(list)
