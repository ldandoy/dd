import json
import time
from tkinter import *
import pygame
import os
import tkinter as tk
from random import *
from functools import partial
from Utils.resized_image import ResizedImage

from Combat.combat import Combat
from Inventory.inventory import Inventory
from Perso.perso import Perso
from Perso.person import Person
from Rooms.rooms import Room
from Window.QuestEndingScreen import questEnding
from Window.QuestEscapeScreen import questEscape
from Utils.load_json import LoadJson


def quest_frame(self):
    w = self.q.winfo_screenwidth()
    h = self.q.winfo_screenheight()
    frame = Frame(self.q, width=w, height=h, bg="#FF0000")

    # image_path = Image.open(os.path.join(self.base_folder, '../medias/entrance.png'))
    # resized_image = image_path.resize((w, h), Image.ANTIALIAS)
    resized_image = ResizedImage.resize(self, '../medias/entrance.png')
    canvas = Canvas(frame, width=w, height=h)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=resized_image, anchor="nw")
    canvas.image = resized_image

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
    labelTextQuestFrame.place(x=w*0.25, y=h*0.05)

    questButton = Button(quest_frame, text="Démarrer une quête", command=choice, border=0,
                         activebackground='#12c4c0', bg="#12c4c0")
    questButton.place(x=w*0.25, y=h*0.1)

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
    w = self.q.winfo_screenwidth()
    h = self.q.winfo_screenheight()
    print(self.rooms.donjon[self.donjonRoom]["name"])
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
            exit_room()
            self.difficultFactor += 1
        print(difficult)
        print(self.difficultFactor)

    def exit_room():
        started_quest_frame.pack_forget()
        started_quest_frame.destroy()
        questEscape(self)

    def next_room():
        self.donjonRoom += 1
        started_quest_frame.pack_forget()
        started_quest_frame.destroy()
        start_quest_frame(self)

    if self.rooms.donjon[self.donjonRoom]["name"] == "Rencontre":
        started_quest_frame = Frame(self.q, width=w, height=h, bg="#FF0000")
        started_quest_frame.place(x=0, y=0)

        resized_image = ResizedImage.resize(self, '../medias/encounter.png')
        canvas = Canvas(started_quest_frame, width=w, height=h)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=resized_image, anchor="nw")
        canvas.image = resized_image

        fightButton = Button(started_quest_frame, text="Combattre !", command=fight, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
        fightButton.place(x=w*0.8, y=h*0.8)

        runButton = Button(started_quest_frame, text="Fuir !", command=run_away, border=0,
                           activebackground='#12c4c0', bg="#12c4c0")
        runButton.place(x=w*0.8, y=h*0.85)
    elif self.rooms.donjon[self.donjonRoom]["name"] == "Boss":
        started_quest_frame = Frame(self.q, width=w, height=h, bg="#FF0000")
        started_quest_frame.place(x=0, y=0)

        resized_image = ResizedImage.resize(self, '../medias/boss.png')
        canvas = Canvas(started_quest_frame, width=w, height=h)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=resized_image, anchor="nw")
        canvas.image = resized_image

        fightButton = Button(started_quest_frame, text="Combattre !", command=boss_fight, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
        fightButton.place(x=w*0.5, y=h*0.5)

    elif self.rooms.donjon[self.donjonRoom]["name"] == "Trésor":
        started_quest_frame = Frame(self.q, width=w, height=h)
        started_quest_frame.place(x=0, y=0)

        resized_image = ResizedImage.resize(self, '../medias/treasure.png')
        canvas = Canvas(started_quest_frame, width=w, height=h)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=resized_image, anchor="nw")
        canvas.image = resized_image

        continueButton = Button(started_quest_frame, text="Continuer", command=next_room, border=0,
                                activebackground='#12c4c0', bg="#12c4c0")
        continueButton.place(x=w*0.5, y=h*0.5)

    elif self.rooms.donjon[self.donjonRoom]["name"] == "Couloir":
        started_quest_frame = Frame(self.q, width=w, height=h, bg="#FF0000")
        started_quest_frame.place(x=0, y=0)

        resized_image = ResizedImage.resize(self, '../medias/corridor.png')
        canvas = Canvas(started_quest_frame, width=w, height=h)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=resized_image, anchor="nw")
        canvas.image = resized_image

        continueButton = Button(started_quest_frame, text="Continuer", command=next_room, border=0,
                                activebackground='#12c4c0', bg="#12c4c0")
        continueButton.place(x=w*0.5, y=h*0.5)

    elif self.rooms.donjon[self.donjonRoom]["name"] == "Rien":
        started_quest_frame = Frame(self.q, width=w, height=h, bg="#FF0000")
        started_quest_frame.place(x=0, y=0)

        resized_image = ResizedImage.resize(self, '../medias/nothing.png')
        canvas = Canvas(started_quest_frame, width=w, height=h)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=resized_image, anchor="nw")
        canvas.image = resized_image

        continueButton = Button(started_quest_frame, text="Continuer", command=next_room, border=0,
                                activebackground='#12c4c0', bg="#12c4c0")
        continueButton.place(x=w*0.5, y=h*0.5)

    tQuestStarted = Label(started_quest_frame, text=self.rooms.donjon[self.donjonRoom]["name"], fg='dark grey')
    tQuestStartedFont = ('Calibri (Body)', 24, 'bold')
    tQuestStarted.config(font=tQuestStartedFont)
    tQuestStarted.place(x=w*0.5, y=h*0.25)

    lQuestStarted = Label(started_quest_frame, text=self.rooms.donjon[self.donjonRoom]["description"], fg='dark grey')
    lQuestStartedFont = ('Calibri (Body)', 18, 'bold')
    lQuestStarted.config(font=lQuestStartedFont)
    lQuestStarted.place(x=w*0.35, y=h*0.3)

def combat(self, isBoss):
    w = self.q.winfo_screenwidth()
    h = self.q.winfo_screenheight()
    if isBoss == 1:
        print("boss FIGHT")
        monstre = self.rooms.boss
        resized_image = ResizedImage.resize(self, '../medias/bestiaire/' + str(self.rooms.boss) + '.png')
    else:
        print("normal FIGHT")
        # List des monstres générés pour le donjon : self.rooms.monsters[self.actualMonster]
        # Ajouter +1 à "actualMonster" pour passer au prochain monstre
        monstre = self.rooms.monsters[self.actualMonster]
        resized_image = ResizedImage.resize(self, '../medias/bestiaire/' + str(self.rooms.monsters[self.actualMonster]) + '.png')


    selectButton = []
    hero = self.perso
    heroHp = hero.get('pdv')
    Combatframe = Frame(self.q, width=w, height=h)
    Combatframe.place(x=0, y=0)
    Combatframe.lower()

    canvas = Canvas(Combatframe, width=w, height=h)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=resized_image, anchor="nw")
    canvas.image = resized_image
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
            heroDmgLabel.place(x=w*0.45, y=h*0.2)
            heroDmgLabel.config(text="hero deal : " + str(dmg))
            monsterHpLabel.config(text=str(hp))
        else:
            monsterDmgLabel.place(x=w*0.45, y=h*0.4)
            monsterDmgLabel.config(text="monster deal : " + str(dmg))
            heroHpLabel.config(text=str(hp) + '/' + str(heroHp))

    def attack(selectWeapon, button):
        AttackButton.place(x=w*0.8, y=h*0.8)
        InventaireButton.place(x=w*0.85, y=h*0.8)
        FuiteButton.place(x=w*0.8, y=h*0.85)
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
        x = w*0.8
        for count, weapon in enumerate(weaponList):
            print(weaponList[count].get('name'))
            selectButton.insert(count, Button(Combatframe, text=weapon.get('name'),
                                              command=lambda weapon=weapon, count=count: attack(weapon.get('name'),
                                                                                                selectButton),
                                              border=0, activebackground='#12c4c0', bg="#12c4c0"))
            selectButton[count].place(x=x, y=h*0.8)
            x = x + x*0.1

    def fuite():
        print("Vous tentez de prendre la fuite")
        Combatframe.pack_forget()
        Combatframe.destroy()
        questEscape(self)

    ## Début -> Inventaire
    #
    #
    def inventory():
        perso = self.perso
        itemTab = []
        inventory = Inventory(perso)
        getItems = perso.get('inventaire')

        # Afficher mes objets sous forme de liste
        for i, item in enumerate(getItems):
            itemTab.insert(i, Button(Combatframe,
                                     text=getItems[i].get('name'),
                                     command=lambda name=getItems[i].get('name'), amount=getItems[i].get('amount'),
                                                    hp=combat.hero_hp: healHero(name, amount, hp),
                                     fg='black',
                                     border=0,
                                     activebackground='#12c4c0',
                                     bg="#12c4c0"))
            itemTab[i].place(x=w*0.85, y=h*0.8 + (i * h*0.05))

        # Faire disparaître les anciens boutons de la frame combat
        AttackButton.place_forget()
        InventaireButton.place_forget()
        FuiteButton.place_forget()

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
            AttackButton.place(x=w*0.8, y=h*0.8)
            InventaireButton.place(x=w*0.85, y=h*0.8)
            FuiteButton.place(x=w*0.8, y=h*0.85)

        # Bouton pour sortir de l'inventaire
        returnButton = Button(Combatframe,
                              text="Retour",
                              command=back,
                              border=0,
                              activebackground='#12c4c0',
                              bg="#12c4c0")
        returnButton.place(x=w*0.8, y=h*0.85)

        #
        #
        ## Fin -> Inventaire

    AttackButton = Button(Combatframe, text="Attack", command=selectWeapon, border=0, activebackground='#12c4c0',
                          bg="#12c4c0")
    AttackButton.place(x=w*0.8, y=h*0.8)

    InventaireButton = Button(Combatframe, text="Inventaire", command=inventory, border=0,
                              activebackground='#12c4c0',
                              bg="#12c4c0")
    InventaireButton.place(x=w*0.85, y=h*0.8)

    FuiteButton = Button(Combatframe, text="Fuite", command=fuite, border=0, activebackground='#12c4c0',
                         bg="#12c4c0")
    FuiteButton.place(x=w*0.8, y=h*0.85)

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
    initLabel.place(x=w*0.35, y=h*0.2)
    if isBoss == 1:
        nameLabel = Label(Combatframe, text="vous rencontrer un " + str(self.rooms.boss),
                          fg='white', bg='black')
    else:
        nameLabel = Label(Combatframe, text="vous rencontrer un " + str(self.rooms.monsters[self.actualMonster]),
                          fg='white', bg='black')

    nameLabelfont = ('Calibri (Body)', 24, 'bold')
    nameLabel.config(font=nameLabelfont)
    nameLabel.place(x=w*0.4, y=h*0.5)

    whoStart(heroHp, combat.hero_hp)


def death(self):
    w = self.q.winfo_screenwidth()
    h = self.q.winfo_screenheight()
    death_frame = Frame(self.q, width=w, height=h)
    death_frame.place(x=0, y=0)
    death_frame.lower()

    resized_image = ResizedImage.resize(self, '../medias/dead.png')
    canvas = Canvas(death_frame, width=w, height=h)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=resized_image, anchor="nw")
    canvas.image = resized_image

    def Retry():
        self.donjonRoom = 0
        death_frame.destroy()
        self.renderHomeScreen()

    retryButton = Button(death_frame, text="Retry", command=Retry, border=0, activebackground='#12c4c0',
                         bg="#12c4c0")
    retryButton.place(x=w*0.5, y=h*0.5)


def win(self, isBoss):
    w = self.q.winfo_screenwidth()
    h = self.q.winfo_screenheight()
    win_frame = Frame(self.q, width=w, height=h)
    win_frame.place(x=0, y=0)
    win_frame.lower()
    if isBoss == 1:
        resized_image = ResizedImage.resize(self, '../medias/sortie.png')
    else:
        resized_image = ResizedImage.resize(self, '../medias/treasure.png')

    canvas = Canvas(win_frame, width=w, height=h)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=resized_image, anchor="nw")
    canvas.image = resized_image

    def next_room():
        win_frame.destroy()
        if isBoss == 1:
            questEnding(self)
        else:
            self.donjonRoom += 1
            self.actualMonster += 1
            start_quest_frame(self)

    nextButton = Button(win_frame, text="next", command=next_room, border=0, activebackground='#12c4c0',
                        bg="#12c4c0")
    nextButton.place(x=w*0.5, y=h*0.5)
    if isBoss == 1:
        winLabel = Label(win_frame,
                         text="Bravo vous avez vaincu " + str(self.rooms.boss) + " ici s'achève votre aventure",
                         fg='white', bg='black')
        winLabel.place(x=w*0.25, y=h*0.4)
    else:
        winLabel = Label(win_frame, text="Bravo vous avez vaincu " + str(self.rooms.monsters[self.actualMonster]),
                         fg='white', bg='black')
        winLabel.place(x=w*0.4, y=h*0.4)
    winLabelfont = ('Calibri (Body)', 24, 'bold')
    winLabel.config(font=winLabelfont)
    