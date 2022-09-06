import json
import time
from tkinter import *
import pygame
import os
import tkinter as tk
from random import *
from functools import partial

from Combat.combat import Combat
from Inventory.inventory import Inventory
from Perso.perso import Perso
from Perso.person import Person
from Rooms.rooms import Room
from Utils.load_json import LoadJson


def quest_frame(self):
    frame = Frame(self.q, width=1024, height=600, bg="#FF0000")

    image_path = os.path.join(self.base_folder, '../medias/entrance.png')
    bg = PhotoImage(file=r'' + image_path)
    canvas = Canvas(frame, width=1024, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    canvas.image = bg

    # Get the welcome message
    json = LoadJson()
    quest = json.load(os.path.join(self.base_folder, '../../Datas/Story/initialQuest.json'))

    def choice():
        frame.pack_forget()
        frame.destroy()
        self.rooms = Room()

        start_quest_frame()

    labelTextQuestFrame = Label(frame, text="Bienvenue " + self.perso["name"] + ", que souhaitez-vous faire ?",
                                fg='dark grey', bg=None)
    labelTextQuestFrame_config = ('Calibri (Body)', 20, 'bold')
    labelTextQuestFrame.config(font=labelTextQuestFrame_config)
    labelTextQuestFrame.place(x=100, y=200)

    questButton = Button(quest_frame, text="Démarrer une quête", command=choice, border=0,
                         activebackground='#12c4c0', bg="#12c4c0")
    questButton.place(x=490, y=300)

    frame.place(x=0, y=0)
    frame.lower()

    def inventory():
        frame.pack_forget()
        frame.destroy()
        perso = Perso("andolorion.json")
        inventory = Inventory(perso, self.q)
        inventory.show()
        perso.save()

    InventaireButton = Button(frame, text="Inventaire", command=inventory, border=0,
                              activebackground='#12c4c0',
                              bg="#12c4c0")
    InventaireButton.place(x=850, y=500)


def start_quest_frame(self):
    def fight():

        started_quest_frame.pack_forget()
        started_quest_frame.destroy()
        combat(self, 0)

    def boss_fight():
        started_quest_frame.pack_forget()
        started_quest_frame.destroy()
        combat(self, 1)

    def run_away():
        difficult = randint(1, 10) + self.difficultFactor
        if difficult >= 6:
            started_quest_frame.pack_forget()
            started_quest_frame.destroy()
            print("Vous vous êtes fait agro")
            combat(self, 0)
        if difficult <= 5:
            started_quest_frame.pack_forget()
            started_quest_frame.destroy()
            print("Fuyez vite")
            quest_frame(self)
            self.difficultFactor += 1
        print(difficult)
        print(self.difficultFactor)

    def exit_room():
        started_quest_frame.pack_forget()
        started_quest_frame.destroy()
        quest_frame(self)

    def next_room():
        self.donjonRoom += 1
        started_quest_frame.pack_forget()
        started_quest_frame.destroy()
        start_quest_frame(self)

    if self.rooms.donjon[self.donjonRoom]["name"] == "Rencontre":
        started_quest_frame = Frame(self.q, width=1024, height=600, bg="#FF0000")
        started_quest_frame.place(x=0, y=0)
        started_quest_frame.lower()

        image_path = os.path.join(self.base_folder, '../medias/encounter.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas = Canvas(started_quest_frame, width=1024, height=600)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")
        canvas.image = bg

        fightButton = Button(started_quest_frame, text="Combattre !", command=fight, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
        fightButton.place(x=750, y=200)

        runButton = Button(started_quest_frame, text="Fuir !", command=run_away, border=0,
                           activebackground='#12c4c0', bg="#12c4c0")
        runButton.place(x=750, y=250)
    elif self.rooms.donjon[self.donjonRoom]["name"] == "Boss":
        started_quest_frame = Frame(self.q, width=1024, height=600, bg="#FF0000")
        started_quest_frame.place(x=0, y=0)
        started_quest_frame.lower()

        image_path = os.path.join(self.base_folder, '../medias/boss.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas = Canvas(started_quest_frame, width=1024, height=600)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")
        canvas.image = bg

        fightButton = Button(started_quest_frame, text="Combattre !", command=boss_fight, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
        fightButton.place(x=750, y=200)

    elif self.rooms.donjon[self.donjonRoom]["name"] == "Trésor":
        started_quest_frame = Frame(self.q, width=1024, height=600)
        started_quest_frame.place(x=0, y=0)
        started_quest_frame.lower()

        image_path = os.path.join(self.base_folder, '../medias/treasure.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas = Canvas(started_quest_frame, width=1024, height=600)
        canvas.pack(fill="both", expand=False)
        canvas.create_image(0, 0, image=bg, anchor="nw")
        canvas.image = bg

        continueButton = Button(started_quest_frame, text="Continuer", command=next_room, border=0,
                                activebackground='#12c4c0', bg="#12c4c0")
        continueButton.place(x=750, y=200)

    elif self.rooms.donjon[self.donjonRoom]["name"] == "Couloir":
        started_quest_frame = Frame(self.q, width=1024, height=600, bg="#FF0000")
        started_quest_frame.place(x=0, y=0)
        started_quest_frame.lower()

        image_path = os.path.join(self.base_folder, '../medias/corridor.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas = Canvas(started_quest_frame, width=1024, height=600)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")
        canvas.image = bg

        continueButton = Button(started_quest_frame, text="Continuer", command=next_room, border=0,
                                activebackground='#12c4c0', bg="#12c4c0")
        continueButton.place(x=750, y=200)

    elif self.rooms.donjon[self.donjonRoom]["name"] == "Rien":
        started_quest_frame = Frame(self.q, width=1024, height=600, bg="#FF0000")
        started_quest_frame.place(x=0, y=0)
        started_quest_frame.lower()

        image_path = os.path.join(self.base_folder, '../medias/nothing.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas = Canvas(started_quest_frame, width=1024, height=600)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")
        canvas.image = bg

        continueButton = Button(started_quest_frame, text="Continuer", command=next_room, border=0,
                                activebackground='#12c4c0', bg="#12c4c0")
        continueButton.place(x=750, y=200)

    tQuestStarted = Label(started_quest_frame, text=self.rooms.donjon[self.donjonRoom]["name"], fg='dark grey')
    tQuestStartedFont = ('Calibri (Body)', 24, 'bold')
    tQuestStarted.config(font=tQuestStartedFont)
    tQuestStarted.place(x=50, y=70)

    lQuestStarted = Label(started_quest_frame, text=self.rooms.donjon[self.donjonRoom]["description"], fg='dark grey')
    lQuestStartedFont = ('Calibri (Body)', 18, 'bold')
    lQuestStarted.config(font=lQuestStartedFont)
    lQuestStarted.place(x=50, y=120)

def combat(self, isBoss):
    if isBoss == 1:
        print("boss FIGHT")
        monstre = self.rooms.boss
        image_path = os.path.join(self.base_folder, '../medias/bestiaire/' + str(self.rooms.boss) + '.png')
    else:
        print("normal FIGHT")
        # List des monstres générés pour le donjon : self.rooms.monsters[self.actualMonster]
        # Ajouter +1 à "actualMonster" pour passer au prochain monstre
        monstre = self.rooms.monsters[self.actualMonster]
        image_path = os.path.join(self.base_folder,
                                  '../medias/bestiaire/' + str(self.rooms.monsters[self.actualMonster]) + '.png')

    selectButton = []
    hero = self.perso
    heroHp = hero.get('pdv')
    Combatframe = Frame(self.q, width=1024, height=600)
    Combatframe.place(x=0, y=0)
    Combatframe.lower()

    bg = PhotoImage(file=r'' + image_path)
    canvas1 = Canvas(Combatframe, width=1024, height=600)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.image = bg
    combat = Combat(hero, monstre, isBoss)
    combat.initiative()

    def whoStart(startHp, initHp):
        if startHp == initHp:
            print("vous avez l'initiative")
            initLabel.config(text="Vous avez gagnez votre jet d'initiative")
        else:
            print("le monstre a l'initiative")
            initLabel.config(text="Le monstre gagne le jet d'initiative")
            dmg = startHp - initHp
            updateLabel(startHp, dmg, False)
            heroHpLabel.config(text=str(initHp) + '/' + str(heroHp))

    def updateLabel(hp, dmg, isHero):
        if isHero:
            heroDmgLabel.place(x=300, y=30)
            heroDmgLabel.config(text="hero deal : " + str(dmg))
            monsterHpLabel.config(text=str(hp))
        else:
            monsterDmgLabel.place(x=300, y=300)
            monsterDmgLabel.config(text="monster deal : " + str(dmg))
            heroHpLabel.config(text=str(hp) + '/' + str(heroHp))

    def attack(selectWeapon, button):
        AttackButton.place(x=750, y=500)
        InventaireButton.place(x=850, y=500)
        FuiteButton.place(x=850, y=550)
        for x in range(len(button)):
            selectButton[x].place_forget()
        monsterHpBeforeHit = combat.monster_hp
        monsterHp = combat.monster_get_damaged(str(selectWeapon))
        herodmgDeal = int(monsterHpBeforeHit) - monsterHp
        updateLabel(monsterHp, herodmgDeal, True)
        if combat.monster_is_dead() == 0:
            print("monster is dead")
            hero["pdv"] = combat.hero_hp
            Person.update(hero.get('name'), hero)
            Combatframe.destroy()
            win(self, isBoss)
        else:
            heroHpbeforeHit = combat.hero_hp
            heroHp = combat.hero_get_damaged()
            monsterdmgDeal = heroHpbeforeHit - heroHp
            updateLabel(heroHp, monsterdmgDeal, False)
            if combat.hero_is_dead() == 0:
                Combatframe.destroy()
                death(self)

    def selectWeapon():
        AttackButton.place_forget()
        InventaireButton.place_forget()
        FuiteButton.place_forget()
        initLabel.place_forget()
        weaponList = self.perso.get('armes')
        print(weaponList)
        x = 750
        for count, weapon in enumerate(weaponList):
            print(weaponList[count].get('name'))
            selectButton.insert(count, Button(Combatframe, text=weapon.get('name'),
                                              command=lambda weapon=weapon, count=count: attack(weapon.get('name'),
                                                                                                selectButton),
                                              border=0, activebackground='#12c4c0', bg="#12c4c0"))
            selectButton[count].place(x=x, y=500)
            x += 100

    def fuite():
        print("Vous tentez de prendre la fuite")

    ## Début -> Inventaire
    #
    #
    def inventory():
        perso = self.perso
        itemTab = []
        inventory = Inventory(perso)
        getItems = perso.get('inventaire')

        
        # Utiliser une potion
        def healHero(name, amount, hp):
            initHp = combat.hero_hp

            combat.hero_hp = inventory.useItem(name, amount, hp)

            back()

            return updateLabel(combat.hero_hp, initHp, False)

        # Sortir de l'inventaire
        def back():
            for i, lbl in enumerate(itemTab):
                itemTab[i].place_forget()

            returnButton.place_forget()
            AttackButton.place(x=750, y=500)
            InventaireButton.place(x=850, y=500)
            FuiteButton.place(x=850, y=550)

        # Bouton pour sortir de l'inventaire
        returnButton = Button(Combatframe,
                              text="Retour",
                              command=back,
                              border=0,
                              activebackground='#12c4c0',
                              bg="#12c4c0")
        returnButton.place(x=750, y=500)

        #
        #
        ## Fin -> Inventaire

    AttackButton = Button(Combatframe, text="Attack", command=selectWeapon, border=0, activebackground='#12c4c0',
                          bg="#12c4c0")
    AttackButton.place(x=750, y=500)

    InventaireButton = Button(Combatframe, text="Inventaire", command=inventory, border=0,
                              activebackground='#12c4c0',
                              bg="#12c4c0")
    InventaireButton.place(x=850, y=500)

    FuiteButton = Button(Combatframe, text="Fuite", command=fuite, border=0, activebackground='#12c4c0',
                         bg="#12c4c0")
    FuiteButton.place(x=850, y=550)

    heroDmgLabel = Label(Combatframe, text="", fg='white', bg='black')
    heroDmgLabelfont = ('Calibri (Body)', 24, 'bold')
    heroDmgLabel.config(font=heroDmgLabelfont)

    monsterDmgLabel = Label(Combatframe, text="", fg='white', bg='black')
    monsterDmgLabelfont = ('Calibri (Body)', 24, 'bold')
    monsterDmgLabel.config(font=monsterDmgLabelfont)

    heroHpLabel = Label(Combatframe, text=(str(hero.get('pdv')) + '/' + str(heroHp)), fg='white', bg='black')
    heroHpLabelfont = ('Calibri (Body)', 24, 'bold')
    heroHpLabel.config(font=heroHpLabelfont)
    heroHpLabel.place(x=30, y=30)

    monsterHpLabel = Label(Combatframe, text=str(combat.monster_hp), fg='white', bg='black')
    monsterHpLabelfont = ('Calibri (Body)', 24, 'bold')
    monsterHpLabel.config(font=monsterHpLabelfont)
    monsterHpLabel.place(x=30, y=300)

    initLabel = Label(Combatframe, text="", fg='white', bg='black')
    initLabelfont = ('Calibri (Body)', 24, 'bold')
    initLabel.config(font=initLabelfont)
    initLabel.place(x=200, y=150)
    if isBoss == 1:
        nameLabel = Label(Combatframe, text="vous rencontrer un " + str(self.rooms.boss),
                          fg='white', bg='black')
    else:
        nameLabel = Label(Combatframe, text="vous rencontrer un " + str(self.rooms.monsters[self.actualMonster]),
                          fg='white', bg='black')

    nameLabelfont = ('Calibri (Body)', 24, 'bold')
    nameLabel.config(font=nameLabelfont)
    nameLabel.place(x=100, y=100)

    whoStart(heroHp, combat.hero_hp)


def death(self):
    death_frame = Frame(self.q, width=1024, height=600)
    death_frame.place(x=0, y=0)
    death_frame.lower()

    image_path = os.path.join(self.base_folder, '../medias/dead.png')
    bg = PhotoImage(file=r'' + image_path)
    canvas1 = Canvas(death_frame, width=1024, height=600)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.image = bg

    def Retry():
        self.donjonRoom = 0
        death_frame.destroy()
        self.textWelcomeFrame()

    retryButton = Button(death_frame, text="Retry", command=Retry, border=0, activebackground='#12c4c0',
                         bg="#12c4c0")
    retryButton.place(x=500, y=300)


def win(self, isBoss):
    win_frame = Frame(self.q, width=1024, height=600)
    win_frame.place(x=0, y=0)
    win_frame.lower()
    if isBoss == 1:
        image_path = os.path.join(self.base_folder, '../medias/sortie.png')
    else:
        image_path = os.path.join(self.base_folder, '../medias/treasure.png')

    bg = PhotoImage(file=r'' + image_path)
    canvas1 = Canvas(win_frame, width=1024, height=600)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.image = bg

    def next_room():
        win_frame.destroy()
        if isBoss == 1:
            self.textWelcomeFrame()
        else:
            self.donjonRoom += 1
            self.actualMonster += 1
            start_quest_frame(self)

    nextButton = Button(win_frame, text="next", command=next_room, border=0, activebackground='#12c4c0',
                        bg="#12c4c0")
    nextButton.place(x=500, y=300)
    if isBoss == 1:
        winLabel = Label(win_frame,
                         text="bravo vous avez vaincu " + str(self.rooms.boss) + " ici s'achève votre aventure",
                         fg='white', bg='black')
    else:
        winLabel = Label(win_frame, text="bravo vous avez vaincu " + str(self.rooms.monsters[self.actualMonster]),
                         fg='white', bg='black')
    winLabelfont = ('Calibri (Body)', 24, 'bold')
    winLabel.config(font=winLabelfont)
    winLabel.place(x=200, y=150)