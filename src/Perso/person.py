import os
import tkinter as tk
from re import sub
from json import dump
import random

from Utils.load_json import LoadJson
from Utils.default_controller import DefaultController
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
        self.descriptionDuPeronnage = f"Je m'appelle {self.name}, je suis un {self.classe} et je ne vis que pour servir les miens. Que les {self.race}s vivent à jamais !! "

    @staticmethod
    def list_person() -> list:
        """Return the list of all person"""
        folder = os.path.join('Datas', 'Perso')
        return os.listdir(folder)

    @staticmethod
    def perso_choose(filename):
        json = LoadJson()
        return json.load(os.path.join('Datas', 'Perso', filename))

    def skill_points_difference(self) -> int:
        """
        Get difference between all skills points and maximum allowed.
        """
        return self.__allowed_skills_points__ - (self.pe + self.force + self.dexterite + self.intelligence + self.charisme + self.constitution + self.sagesse + self.vitesse)

    def verify_inputs(self) -> list:
        """
        Verify input before save
        Returns list contains errors message or empty list
        """
        errors = []
        if not self.name or self.name.strip() == '':
            errors.append('Le nom ne peut pas etre vide')
        if not self.age or self.age <= 0:
            errors.append('L\'age doit etre supérieur à 0')
        if not self.yeux or self.yeux.strip() == '':
            errors.append('La couleur des yeux ne peut pas etre vide')
        if not self.taille or self.taille <= 0:
            errors.append('La taille doit etre supérieur à 0')
        if not self.poids or self.poids <= 0:
            errors.append('Le poids doit etre supérieur à 0')
        if not self.peau or self.peau.strip() == '':
            errors.append('La couleur de peau ne peut pas etre vide')
        if not self.race or self.race.strip() == '':
            errors.append('L\'origine ethnique ne peut pas etre vide')
        if not self.classe or self.classe.strip() == '':
            errors.append('La classe ne peut pas etre vide')
        if not self.alignement or self.alignement.strip() == '':
            errors.append('L\'alignement ne peut pas etre vide')
        if not self.pe or self.pe <= 0:
            errors.append('Les points d\'expérience doit etre supérieur à 0')
        if not self.force or self.force <= 0:
            errors.append('La force doit etre supérieure à 0')
        if not self.dexterite or self.dexterite <= 0:
            errors.append('La dexterité doit etre supérieure à 0')

        # verify skills points attribution
        skill_points_difference = self.skill_points_difference()
        if skill_points_difference < 0 and not skill_points_difference == -400:
            abs_skill_points_difference = abs(skill_points_difference)
            points_msg = 'point' if abs_skill_points_difference == 1 else 'points'
            errors.append(f'Points de compétences insuffisant,'
                          f'vous devez retirer {abs_skill_points_difference} {points_msg}')
        return errors

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
                'description': self.descriptionDuPeronnage,
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
                ],
                "budget": 30
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

    @staticmethod
    def dice(jet):
        bonus_split = jet.split("+")
        my_split = bonus_split[0].split("d")
        nb_dice = min(1, int(my_split[0]))
        rand_range = min(1, int(my_split[1]))
        dmg_deal = 0
        bonus = int(bonus_split[1])
        print(nb_dice)
        print(my_split)
        for x in range(nb_dice):
            rand = random.randint(1, rand_range+1)
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

    @staticmethod
    def update(perso):
        json_file_path = open(os.path.join('Datas', 'Perso', str(perso['name'].lower()) + '.json'), "w")
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

        dump(json_to_save, json_file_path, indent=2)
        debug(f'{json_file_path} Successfully saved')
