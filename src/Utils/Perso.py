import os
import random

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

    @staticmethod
    def dice(jet):
        bonus_split = jet.split("+")
        my_split = bonus_split[0].split("d")
        nb_dice = my_split[0]
        rand_range = my_split[1]
        dmg_deal = 0
        bonus = int(bonus_split[1])

        for x in range(int(nb_dice)):
            rand = random.randint(1, int(rand_range))
            dmg_deal = dmg_deal + rand
        print("dmg dealt : " + str(dmg_deal))
        return dmg_deal + bonus

