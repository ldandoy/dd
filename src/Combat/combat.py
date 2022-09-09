from Perso.person import Person
from Utils.load_json import LoadJson

class Combat:
    j = LoadJson()
    def __init__(self, hero, monstre,isBoss):
        ## load my hero and monster data
        self.hero = hero
        print(str(monstre)+'.json')
        if isBoss == 1:
            self.monster = self.j.load('Datas/Boss/'+monstre+'.json')
        else:
            self.monster = self.j.load('Datas/Monsters/'+monstre+'.json')
        print(self.monster)
        #Hero var
        self.hero_damage = self.hero.get('attaque')
        self.hero_hp = self.hero.get('pdv')
        self.hero_vit = self.hero.get('vitesse')
        self.hero_for = self.hero.get('force')
        self.hero_int = self.hero.get('intellignce')
        self.hero_dex = self.hero.get('dexterite')
        self.hero_cha = self.hero.get('charisme')
        self.hero_con = self.hero.get('constitution')
        self.hero_sag = self.hero.get('sagesse')
        #Hero weapon
        self.hero_weapon = self.hero.get('armes')
        self.hero_weapon_attaque = self.hero_weapon[1].get('attaque')
        self.hero_weapon_test = self.hero_weapon[1].get('test')
        #Monster var
        self.monster_damage = self.monster.get('attaque')
        self.monster_vit = self.monster.get('vitesse')
        self.monster_hp = self.monster.get('pdv')

    def selectedWeapon(self, weapon_selected):
        for x in range(len(self.hero_weapon)):
            if str(self.hero_weapon[x].get('name')) == str(weapon_selected):
                self.hero_weapon_attaque = self.hero_weapon[x].get('degat')
                self.hero_weapon_test = self.hero_weapon[x].get('test')
                print('weapon updated')
        print(self.hero_weapon_attaque)
        print(self.hero_weapon_test)

    def createDice(self):
        if self.hero_weapon_test == 'force':
            return str(self.hero_weapon_attaque)+"+"+str(Person.bonus(self.hero_for))
        if self.hero_weapon_test == 'dexterite':
            return str(self.hero_weapon_attaque)+"+"+str(Person.bonus(self.hero_dex))
        if self.hero_weapon_test == 'intelligence':
            return str(self.hero_weapon_attaque)+"+"+str(Person.bonus(self.hero_int))

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
        self.hero_hp = int(self.hero_hp) - int(Person.dice(self.monster_damage))
        print("hero hp : " + str(self.hero_hp))
        return self.hero_hp

    def monster_get_damaged(self, weapon_selected):
        print('monster will get hit')
        self.selectedWeapon(weapon_selected)
        my_dice = self.createDice()
        self.monster_hp = int(self.monster_hp) - int(Person.dice(my_dice))
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