import os
from Utils.DefaultController import DefaultController


class Perso(DefaultController):
    """
        A class used to represent a personnage

        Methods
        -------
        load()
            Get all the Perso files
    """
    def __init__(self):
        pass

    @staticmethod
    def listPerso():
        """Return the list of the Perso"""
        list = os.path.join('Datas', 'Perso')
        return list
