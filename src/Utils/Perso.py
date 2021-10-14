import os
from Utils.DefaultController import DefaultController
from Utils.logger import debug
import random


def choose_skill() -> None:
    print('Hello')


def save() -> None:
    print('Save file')


class Perso(DefaultController):
    """
        A class used to represent a personnage

        Methods
        -------
        load()
            Get all the Perso files
    """
    def __init__(self) -> None:
        super().__init__()
        self.__allowed_skills_points__ = 25
        self.name: str
        self.age: str
        self.yeux: str
        self.taille: int
        self.poids: int
        self.peau: int
        self.race: str
        self.alignement: str
        self.pe = 0
        self.force = 0
        self.dexterite = 0
        self.intelligence = 0
        self.charisme = 0
        self.constitution = 0
        self.sagesse = 0
        self.vitesse = 0
        self.pdv = 0

    @staticmethod
    def list_perso():
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


    """
    Verify that allowed points is not 0.
    If total points are less than 1, then remove 1 point.
    """
    def __verify_allowed_points__(self) -> bool:
        debug('Verify allowed points, current=%d', self.__allowed_skills_points__)
        is_valid = self.__allowed_skills_points__ > 1
        if is_valid:
            self.__allowed_skills_points__ -= 1
        return is_valid

    def add_one_point_to_pe(self) -> None:
        if self.__verify_allowed_points__():
            self.pe += 1

    def add_one_point_to_force(self) -> None:
        if self.__verify_allowed_points__():
            self.force += 1

    def add_one_point_to_dexterite(self) -> None:
        if self.__verify_allowed_points__():
            self.dexterite += 1

    def add_one_point_to_intelligence(self) -> None:
        if self.__verify_allowed_points__():
            self.intelligence += 1

    def add_one_point_to_charisme(self) -> None:
        if self.__verify_allowed_points__():
            self.charisme += 1

    def add_one_point_to_constitution(self) -> None:
        if self.__verify_allowed_points__():
            self.constitution += 1

    def add_one_point_to_sagesse(self) -> None:
        if self.__verify_allowed_points__():
            self.sagesse += 1

    def add_one_point_to_vitesse(self) -> None:
        if self.__verify_allowed_points__():
            self.vitesse += 1

    def add_one_point_to_pdv(self) -> None:
        if self.__verify_allowed_points__():
            self.pdv += 1
