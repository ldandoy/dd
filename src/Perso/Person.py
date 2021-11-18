import os
import tkinter as tk
from re import sub
from json import dump
import random


from Utils.loadJson import LoadJson
from Utils.DefaultController import DefaultController
from Utils.logger import debug


class Person(DefaultController):
    """
        A class used to represent a person

        Methods
        -------
        load()
            Get all the Person files
        save()
            Save person to local (JSON format).
    """
    def __init__(self,
                 name: tk.StringVar,
                 age: tk.IntVar,
                 yeux: tk.StringVar,
                 taille: tk.IntVar,
                 poids: tk.IntVar,
                 peau: tk.StringVar,
                 race: tk.StringVar,
                 classe: tk.StringVar,
                 alignement: tk.StringVar,
                 pe: tk.IntVar,
                 force: tk.IntVar,
                 dexterite: tk.IntVar,
                 intelligence: tk.IntVar,
                 charisme: tk.IntVar,
                 constitution: tk.IntVar,
                 sagesse: tk.IntVar,
                 vitesse: tk.IntVar) -> None:
        super().__init__()
        self.__allowed_skills_points__ = 25
        self.name: str = name.get()
        self.age: int = age.get()
        self.yeux: str = yeux.get()
        self.taille: int = taille.get()
        self.poids: int = poids.get()
        self.peau: str = peau.get()
        self.race: str = race.get()
        self.classe: str = classe.get()
        self.alignement: str = alignement.get()
        self.pe: int = pe.get()
        self.force: int = force.get()
        self.dexterite: int = dexterite.get()
        self.intelligence: int = intelligence.get()
        self.charisme: int = charisme.get()
        self.constitution: int = constitution.get()
        self.sagesse: int = sagesse.get()
        self.vitesse: int = vitesse.get()
        self.pdv = 100

    @staticmethod
    def list_person() -> list:
        """Return the list of all person"""
        folder = os.path.join('Datas', 'Perso')
        return os.listdir(folder)

    def perso_choose(filename):
        json = LoadJson()
        return json.load(os.path.join('Datas', 'Perso', filename))

    def save(self):
        transformed_name = self.__get_transformed_name()
        debug('Should save new character with file name: ' + transformed_name)

        # verify that character with this name does not exist yet
        if self.__is_this_name_already_exists():
            debug('Character with this name already exists')
            return False

        else:
            debug('Character with this name does not exist yet, will save')
            json_to_save = {
                'name': self.name,
                'age': self.age,
                'yeux': self.yeux,
                'taille': self.taille,
                'poids': self.poids,
                'peau': self.peau,
                'race': self.race,
                'classe': self.classe,
                'alignement': self.alignement,
                'pe': self.pe,
                'force': self.force,
                'dexterite': self.dexterite,
                'intelligence': self.intelligence,
                'charisme': self.charisme,
                'constitution': self.constitution,
                'sagesse': self.sagesse,
                'vitesse': self.vitesse,
                'pdv': self.pdv,
                'armes': [
                    {
                        'name': 'Epee courte',
                        'degat': '1d10',
                        'test': 'force'
                    }, {
                        'name': 'Arc Long',
                        'degat': '1d10',
                        'test': 'dexterite'
                    }
                ],
                'inventaire': [
                    {
                        "name": "potion",
                        "amount": 1
                    },
                    {
                        "name": "super-potion",
                        "amount": 1
                    },
                    {
                        "name": "mega-potion",
                        "amount": 1
                    }
                ]
            }

            json_file_path = os.path.join('Datas', 'Perso', f'{transformed_name}.json')

            with open(json_file_path, 'w+') as outfile:
                dump(json_to_save, outfile, indent=2)
            debug(f'{json_file_path} Successfully saved')

    def __get_transformed_name(self) -> str:
        """
        Get a transformed name compatible for file name.
        """
        return sub(r'/[^A-Za-z0-9 _\-\+\&]/', '_', self.name.lower())

    def __is_this_name_already_exists(self) -> bool:
        """
        Check if a file with this name already exists.
        """
        # retrieve all characters
        found = False
        for person in Person.list_person():
            if self.__get_transformed_name() in person:
                found = True
        return found

    def __verify_allowed_points__(self) -> bool:
        """
        Verify that allowed points is not 0.
        If total points are less than 1, then remove 1 point.
        """
        debug('Verify allowed points, current=%d', self.__allowed_skills_points__)
        is_valid = self.__allowed_skills_points__ > 1
        if is_valid:
            self.__allowed_skills_points__ -= 1
        return is_valid

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
        print("dmg dealt : " + str(dmg_deal + bonus))
        return dmg_deal + bonus

    @staticmethod
    def bonus(carac):
        if carac < 10:
            return 0
        if carac >= 10 & carac < 15:
            return 1
        if carac >= 15 & carac < 20:
            return 2
        if carac >= 20 & carac < 25:
            return 3
        if carac >= 25 & carac < 40:
            return 4
        else:
            return 5

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

    def update(filename,perso):
        json_file_path = open(os.path.join('Datas', 'Perso', filename.lower()+'.json'),"w")
        print('my perso from update ' + str(perso))
        json_to_save = {
            'name': perso.get('name'),
            'age': perso.get('age'),
            'yeux': perso.get('yeux'),
            'taille': perso.get('taille'),
            'poids': perso.get('poids'),
            'peau': perso.get('peau'),
            'race': perso.get('race'),
            'classe': perso.get('classe'),
            'alignement': perso.get('alignement'),
            'pe': perso.get('pe'),
            'force': perso.get('force'),
            'dexterite': perso.get('dexterite'),
            'intelligence': perso.get('intelligence'),
            'charisme': perso.get('charisme'),
            'constitution': perso.get('constitution'),
            'sagesse': perso.get('sagesse'),
            'vitesse': perso.get('vitesse'),
            'pdv': perso.get('pdv'),
            'armes': perso.get('armes'),
            'inventaire': perso.get('inventaire')
        }
        print("my json to save " + str(json_to_save))

        dump(json_to_save, json_file_path,indent=2)
        debug(f'{json_file_path} Successfully saved')

