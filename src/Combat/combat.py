import json

from Perso.Person import Person
import json

class Combat:
    def __init__(self, hero, monster):
        self.hero = json.loads(hero)
        self.monster = json.loads(monster)
        self.hero_damage = self.hero.get('attaque')
        self.monster_hp = self.monster.get('hp')
        self.monster_damage = self.monster.get('attaque')
        self.hero_hp = self.hero.get('hp')
        self.hero_vit = self.hero.get('vit')
        self.monster_vit = self.monster.get('vit')

    def initiative(self):
        self.hero_vit = Person.dice("1d"+str(self.hero_vit)+"+0")
        self.monster_vit = Person.dice("1d"+str(self.monster_vit)+"+0")
        print("Monster jet init : " + str(self.monster_vit))
        print("Hero jet init : " + str(self.hero_vit))
        if self.hero_vit < self.monster_vit:
            self.hero_get_damaged()
        return 0

    def hero_is_dead(self):
        if int(self.hero_hp) <= 0:
            return 0
        else:
            return 1

    def monster_is_dead(self):
        if int(self.monster_hp) <= 0:
            return 0
        else:
            return 1

    def hero_get_damaged(self):
        print('hero will get hit')
        self.hero_hp = self.hero_hp - Person.dice(self.monster_damage)
        print("hero hp : " + str(self.hero_hp))
        return self.hero_hp

    def monster_get_damaged(self):
        print('monster will get hit')
        self.monster_hp = int(self.monster_hp) - int(Person.dice(self.hero_damage))
        print("monster hp : " + str(self.monster_hp))
        return self.monster_hp

    ##functiopn test déroulement du combat
    def fight(self):
        combat_done = 1
        while combat_done == 1:
            self.hero_get_damaged()
            print('my hero is dead ? ' + str(self.hero_is_dead()))
            if self.hero_is_dead() == 0:
                combat_done = 0
            else:
                self.monster_get_damaged()
                print('my monster is dead ? ' + str(self.monster_is_dead()))
                if self.monster_is_dead() == 0:
                    combat_done = 0
                else:
                    print("hp hero :" + str(self.hero_hp) + " monster hp : " + str(self.monster_hp))
            print("my combat status" + str(combat_done))
        return 0



