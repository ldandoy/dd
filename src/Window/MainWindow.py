import time
from tkinter import *
import pygame
import os
import tkinter as tk
from random import *

from Utils.loadJson import LoadJson
from Perso.Person import Person
from Rooms.rooms import Room
from Combat.combat import *
from Utils.GetLastFeatures import GetLastFeatures
from functools import partial

from Combat.combat import Combat


class MainWindow:
    rooms = []
    json = LoadJson()
    perso = None

    donjonRoom = 0
    actualMonster = 0
    difficultFactor = 0



    def toogleWin(self):
        f1 = Frame(self.q, width=300, height=600, bg='#12c4c0')
        f1.place(x=0, y=0)

        def dele():
            f1.destroy()

        def bttn(x, y, text, bcolor, fcolor, cmd):
            def onEnter(e):
                myButton['background'] = bcolor #ffcc66
                myButton['foreground'] = '#262626' #000d33

            def onLeaves(e):
                myButton['background'] = fcolor
                myButton['foreground'] = '#262626'

            myButton = Button(f1,
                text=text,
                width=42,
                height=2,
                fg="#262626",
                bg=fcolor,
                border=0,
                activeforeground="#262626",
                activebackground=bcolor,
                command=cmd)

            myButton.bind("<Enter>", onEnter)
            myButton.bind("<Leave>", onLeaves)

            myButton.place(x=x, y=y)

        bttn(0, 80, 'A C E R', "#0f9d9a", "#12c4c0", None)
        bttn(0, 117, 'D E L L', "#0f9d9a", "#12c4c0", None)
        bttn(0, 154, 'A P P L E', "#0f9d9a", "#12c4c0", None)
        bttn(0, 191, 'A S U S', "#0f9d9a", "#12c4c0", None)
        bttn(0, 228, 'A C E R', "#0f9d9a", "#12c4c0", None)
        bttn(0, 265, 'S O N Y', "#0f9d9a", "#12c4c0", None)


        Button(f1, text="close", command=dele, border=0, activebackground='#12c4c0', bg="#12c4c0").place(x=5, y=10)

    def __init__(self):
        self.base_folder = os.path.dirname(__file__)
        self.q = Tk()
        self.q.title("Donjon & Dragon")
        self.q.geometry('1024x600')
        self.q.configure(bg='')
        # Add no size update

        Button(self.q, command=self.toogleWin, text='Menu', border=0, bg="#12c4c0").place(x=5, y=10)

        self.textWelcomeFrame()

        self.q.mainloop()

    def textWelcomeFrame( self ):
        textwelcomeframe = Frame( self.q, width=1024, height=600 )
        textwelcomeframe.place( x=0, y=0 )
        textwelcomeframe.lower()

        image_path = os.path.join( self.base_folder, '../medias/montagne.png' )
        bg = PhotoImage( file=r'' + image_path )
        canvas1 = Canvas( textwelcomeframe, width=1024, height=600 )
        canvas1.pack( fill="both", expand=True )
        canvas1.create_image( 0, 0, image=bg, anchor="nw" )
        canvas1.image = bg

        label_textwelcomeframe = Label( textwelcomeframe, text="Bienvenue dans Donjon et Dragon", fg='dark grey',
                                        bg=None )
        label_textwelcomeframe_config = ('Calirbi (Body)', 36, 'bold')
        label_textwelcomeframe.config( font=label_textwelcomeframe_config )
        label_textwelcomeframe.place( x=250, y=100 )

        lastFeaturesObj = GetLastFeatures( 3 )

        label_textinfo_config = ('Calirbi (Body)', 24, 'bold')

        label_textinfo_x_position = 25
        label_showmore_y_position = 100

        def newsShowMoreFrame( self, feature ):
            news_show_more_frame = Frame( self.q, width=1024, height=600 )

            image2_path = os.path.join( self.base_folder, '../medias/newsBg/' + feature[ 'picture' ] )
            bg2 = PhotoImage( file=image2_path )
            canvas2 = Canvas( news_show_more_frame, width=1024, height=600 )
            canvas2.pack( fill="both", expand=True )
            canvas2.create_image( 0, 0, image=bg2, anchor="nw" )
            canvas2.image = bg2

            for i, info in enumerate( feature ):
                if(info != 'picture' ):
                    label_textinfo = Label( news_show_more_frame, text=feature[info], fg='white', bg='#0483d1' )
                    label_textinfo.config( font=label_textinfo_config )
                    label_textinfo.place( x=25, y= label_showmore_y_position + (i * 40))


            def choice():
                news_show_more_frame.pack_forget()
                news_show_more_frame.destroy()

                self.textWelcomeFrame()

            ChoiceButton = Button( news_show_more_frame, text="retour", command=choice, border=0,
                                   activebackground='#12c4c0', bg="#12c4c0" )
            ChoiceButton.place( x=950, y=550 )

            news_show_more_frame.place( x=0, y=0 )
            news_show_more_frame.lower()

        def showMore( feature ):
            textwelcomeframe.pack_forget()
            textwelcomeframe.destroy()
            newsShowMoreFrame( self, feature )

        for i, feature in enumerate( lastFeaturesObj ):
            label_textinfo = Label( textwelcomeframe, text=feature[ 'title' ][ 0:50 ], fg='white',
                                    bg='#0483d1', )
            label_textinfo.config( font=label_textinfo_config )
            label_textinfo.place( x=label_textinfo_x_position + (i * 350), y=250 )
            news_Button = Button( textwelcomeframe, text="En savoir plus", command=partial( showMore, feature ),
                                  border=0,
                                  activebackground='#12c4c0',
                                  bg="#12c4c0" )
            news_Button.place( x=label_textinfo_x_position + (i * 350), y=300 )

        def play():
            textwelcomeframe.pack_forget()
            textwelcomeframe.destroy()

            self.choicePersoFrame()

        PlayButton = Button(textwelcomeframe, text="Jouer", command=play, border=0, activebackground='#12c4c0', bg="#12c4c0")
        PlayButton.place(x=950, y=550)


    def choicePersoFrame(self):
        """window to choice a character"""
        choicePersoFrame = Frame(self.q, width=1024, height=600)

        image2_path = os.path.join(self.base_folder, '../medias/forest.png')
        bg2 = PhotoImage(file=image2_path)
        canvas2 = Canvas(choicePersoFrame, width=1024, height=600)
        canvas2.pack(fill="both", expand=True)
        canvas2.create_image(0, 0, image=bg2, anchor="nw")
        canvas2.image = bg2

        # About character -------
        card = Canvas(choicePersoFrame, width=650, height=154)
        card.place(x=105, y=420)
        # card.create_rectangle(55, 30, 140, 70, fill="blue")


        lwelcome = Label(choicePersoFrame, text="Choissez votre personnage", fg='white', bg ='black')
        lwelcomefont = ('Calirbi (Body)', 24, 'bold')
        lwelcome.config(font=lwelcomefont)
        lwelcome.place(x=105, y=30)

        pygame.mixer.init()

        def play():
            pygame.mixer.music.load(os.path.join(self.base_folder, '../medias/audio/epic.mp3'))
            pygame.mixer.music.play(loops=0)
        play()


        def choice():
            choicePersoFrame.pack_forget()
            choicePersoFrame.destroy()

            self.questFrame()

        ChoiceButton = Button(choicePersoFrame, text="Choisir", command=choice, state=DISABLED, border=0,
                              activebackground='#12c4c0', bg="#12c4c0", width=27, height=7)
        ChoiceButton.place(x=780, y=420)

        #select champion
        def selected(perso, count):
            ChoiceButton['state'] = NORMAL
            self.perso = Person.perso_choose(perso)

        selectButton = []
        persoJson = Person.list_person()
        print(persoJson)
        x = 105
        y=100

        count_character = 1
        for count, perso in enumerate(persoJson):

            print(y)

            if count == 4:
                x=105
                y=250
                print("this is " + str(x))

            file = os.path.join(os.path.dirname(__file__), "..", 'medias', 'characters', f'{count_character}.png').replace("\\", '/')

            count_character += 1

            imageCharacter = PhotoImage(file=file)
            print(file)

            perso_button = Button(choicePersoFrame,
                                              text=perso,
                                              command=lambda perso=perso, count=count: selected(perso,count),
                                              image=imageCharacter
                                              )
            perso_button.image = imageCharacter

            selectButton.insert(count, perso_button)
            selectButton[count].place(x=x, y=y, width=110, height=110, )

            choicePersoFrame.lower()
            x += 200


        # # character area ---------
        # def getJson():
        #     persoList = []
        #     persoJson = Person.list_person()
        #     for i in persoJson:
        #         persoList.append(i)
        #     return persoList
        #
        # def getJsonSelected(perso):
        #     return self.json.load(os.path.join(self.base_folder, '../../Datas/Perso/' + perso))
        #
        # def getNamePerso(perso):
        #     for persoJson in getJson():
        #         if perso == persoJson:
        #             data = getJsonSelected(perso)
        #             name = data["name"]
        #             return name
        #         else:
        #             print('no name')
        #
        #
        # getJson()
        #
        # def displayChampion():
        #     for perso in getJson():
        #         print(perso)
        #         x = 105
        #         selectButton['text'] = getNamePerso(perso)
        #         selectButton.place(x=x, y=100, width=110, height=110, )
        #
        #         print(x)
        #         x += 20
        #
        def displayChampionInformation():
            pass
        #
        # displayChampion()


        def goToNewPerso() -> None:
            choicePersoFrame.pack_forget()
            choicePersoFrame.destroy()

            self.new_person_frame()

        #Button in choicePersoFrame window
        #ChoiceButton = Button(choicePersoFrame, text="Choisir", command=choice, border=0, activebackground='#12c4c0', bg="#12c4c0")
        new_button = Button(choicePersoFrame, text="Créer un nouveau personnage", command=goToNewPerso, border=0, activebackground='#12c4c0', bg="#12c4c0", width=27)
        #ChoiceButton.place(x=950, y=550)
        new_button.place(x=780, y=550)

        choicePersoFrame.place(x=0, y=0)
        choicePersoFrame.lower()

    def questFrame(self):
        questFrame = Frame(self.q, width=1024, height=600, bg="#FF0000")

        image_path = os.path.join(self.base_folder, '../medias/entrance.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas = Canvas(questFrame, width=1024, height=600)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")
        canvas.image = bg

        # Get the welcome message
        json = LoadJson()
        quest = json.load(os.path.join(self.base_folder, '../../Datas/Story/initialQuest.json'))

        def choice():
            questFrame.pack_forget()
            questFrame.destroy()
            self.rooms = Room()

            self.questStartedFrame()

        labelTextQuestFrame = Label(questFrame, text="Bienvenue " + self.perso["name"] + ", que souhaitez-vous faire ?",
                                     fg='dark grey', bg=None)
        labelTextQuestFrame_config = ('Calibri (Body)', 20, 'bold')
        labelTextQuestFrame.config(font=labelTextQuestFrame_config)
        labelTextQuestFrame.place(x=100, y=200)

        questButton = Button(questFrame, text="Démarrer une quête", command=choice, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
        questButton.place(x=490, y=300)

        questFrame.place(x=0, y=0)
        questFrame.lower()

    def questStartedFrame(self):

        def fight():

            questStartedFrame.pack_forget()
            questStartedFrame.destroy()
            self.CombatFrame(0)
        def bossFight():
            questStartedFrame.pack_forget()
            questStartedFrame.destroy()
            self.CombatFrame(1)
        def runAway():
            difficult = randint(1, 10) + self.difficultFactor
            if difficult >= 6:
                questStartedFrame.pack_forget()
                questStarame.destroy()
                print("Vous vous etes fait agro")
                self.CombatFrame(0)
            if difficult < 5:
                questStartedFrame.pack_forget()
                questStartedFrame.destroy()
                print("Fuyez vite")
                self.questFrame()
                self.difficultFactor += 1
            print(difficult)
            print(self.difficultFactor)

        def exitRoom():
            questStartedFrame.pack_forget()
            questStartedFrame.destroy()
            self.questFrame()
        def nextRoom():
            self.donjonRoom += 1
            questStartedFrame.pack_forget()
            questStartedFrame.destroy()
            self.questStartedFrame()

        if self.rooms.donjon[self.donjonRoom]["name"] == "Rencontre":
            questStartedFrame = Frame(self.q, width=1024, height=600, bg="#FF0000")
            questStartedFrame.place(x=0, y=0)
            questStartedFrame.lower()

            image_path = os.path.join(self.base_folder, '../medias/encounter.png')
            bg = PhotoImage(file=r'' + image_path)
            canvas = Canvas(questStartedFrame, width=1024, height=600)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=bg, anchor="nw")
            canvas.image = bg

            fightButton = Button(questStartedFrame, text="Combattre !", command=fight, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
            fightButton.place(x=750, y=200)

            runButton = Button(questStartedFrame, text="Fuir !", command=runAway, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
            runButton.place(x=750, y=250)
        elif self.rooms.donjon[self.donjonRoom]["name"] == "Boss":
            questStartedFrame = Frame(self.q, width=1024, height=600, bg="#FF0000")
            questStartedFrame.place(x=0, y=0)
            questStartedFrame.lower()

            image_path = os.path.join(self.base_folder, '../medias/boss.png')
            bg = PhotoImage(file=r'' + image_path)
            canvas = Canvas(questStartedFrame, width=1024, height=600)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=bg, anchor="nw")
            canvas.image = bg

            fightButton = Button(questStartedFrame, text="Combattre !", command=bossFight, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
            fightButton.place(x=750, y=200)

        elif self.rooms.donjon[self.donjonRoom]["name"] == "Trésor":
            questStartedFrame = Frame(self.q, width=1024, height=600)
            questStartedFrame.place(x=0, y=0)
            questStartedFrame.lower()

            image_path = os.path.join(self.base_folder, '../medias/treasure.png')
            bg = PhotoImage(file=r'' + image_path)
            canvas = Canvas(questStartedFrame, width=1024, height=600)
            canvas.pack(fill="both", expand=False)
            canvas.create_image(0, 0, image=bg, anchor="nw")
            canvas.image = bg

            continueButton = Button(questStartedFrame, text="Continuer", command=nextRoom, border=0,
                                    activebackground='#12c4c0', bg="#12c4c0")
            continueButton.place(x=750, y=200)

        elif self.rooms.donjon[self.donjonRoom]["name"] == "Couloir":
            questStartedFrame = Frame(self.q, width=1024, height=600, bg="#FF0000")
            questStartedFrame.place(x=0, y=0)
            questStartedFrame.lower()

            image_path = os.path.join(self.base_folder, '../medias/corridor.png')
            bg = PhotoImage(file=r'' + image_path)
            canvas = Canvas(questStartedFrame, width=1024, height=600)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=bg, anchor="nw")
            canvas.image = bg

            continueButton = Button(questStartedFrame, text="Continuer", command=nextRoom, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
            continueButton.place(x=750, y=200)

        elif self.rooms.donjon[self.donjonRoom]["name"] == "Rien":
            questStartedFrame = Frame(self.q, width=1024, height=600, bg="#FF0000")
            questStartedFrame.place(x=0, y=0)
            questStartedFrame.lower()

            image_path = os.path.join(self.base_folder, '../medias/nothing.png')
            bg = PhotoImage(file=r'' + image_path)
            canvas = Canvas(questStartedFrame, width=1024, height=600)
            canvas.pack(fill="both", expand=True)
            canvas.create_image(0, 0, image=bg, anchor="nw")
            canvas.image = bg

            continueButton = Button(questStartedFrame, text="Continuer", command=nextRoom, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
            continueButton.place(x=750, y=200)

        tQuestStarted = Label(questStartedFrame, text=self.rooms.donjon[self.donjonRoom]["name"], fg='dark grey')
        tQuestStartedFont = ('Calibri (Body)', 24, 'bold')
        tQuestStarted.config(font=tQuestStartedFont)
        tQuestStarted.place(x=50, y=70)

        lQuestStarted = Label(questStartedFrame, text=self.rooms.donjon[self.donjonRoom]["description"], fg='dark grey')
        lQuestStartedFont = ('Calibri (Body)', 18, 'bold')
        lQuestStarted.config(font=lQuestStartedFont)
        lQuestStarted.place(x=50, y=120)

    ## Frame jamais utiliser Illies confirme suppression 
    # def newPersoFrame(self):
    #     frame = Frame(self.q, width=1024, height=600, bg="#FFF")

    #     # main message
    #     main_message = Label(frame, text='Créer un personnage', fg='dark grey')
    #     main_message.config(font=('Calibri (Body)', 24, 'bold'))
    #     main_message.place(x=200, y=200)

    #     # new perso form
    #     Label(frame, text="Name").grid(row=0, column=0)
    #     Label(frame, text="Age").grid(row=1, column=0)
    #     name = Entry(frame).grid(row=0, column=1)
    #     age = Entry(frame).grid(row=1, column=1)

    #     def makeForm(root, fields):
    #         entries = {}
    #         for field in fields:
    #             row = Frame(root)
    #             lab = Label(row, width=22, text=field + ": ", anchor='w')
    #             ent = Entry(row)
    #             ent.insert(0, "0")
    #             row.pack(side=TOP, fill=X, padx=5, pady=5)
    #             lab.pack(side=LEFT)
    #             ent.pack(side=RIGHT, expand=YES, fill=X)
    #             entries[field] = ent
    #         return entries

    #     fields = ('Name', 'Age')
    #     ents = makeForm(self.q, fields)
    #     print(name)

    #     def triggerSubmitNewForm():
    #         submit_new_perso(ents.get('Name'))

    #     btn = Button(frame, text="Submit", command=submit_new_perso).grid(row=4, column=0)

    #     frame.place(x=0, y=0)
    #     frame.lower()

    def CombatFrame(self,isBoss):
        if isBoss == 1:
            print("boss FIGHT")
            monstre = self.rooms.boss
            image_path = os.path.join(self.base_folder, '../medias/bestiaire/'+ str(self.rooms.boss)+'.png')
        else:
            print("normal FIGHT")
            # List des monstres générés pour le donjon : self.rooms.monsters[self.actualMonster]
            # Ajouter +1 à "actualMonster" pour passer au prochain monstre
            monstre = self.rooms.monsters[self.actualMonster]
            image_path = os.path.join(self.base_folder, '../medias/bestiaire/' + str(self.rooms.monsters[self.actualMonster]) + '.png')

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
        combat = Combat(hero, monstre,isBoss)
        combat.initiative()

        def whoStart(startHp,initHp):
            if startHp == initHp:
                print("vous avez l'initiative")
                initLabel.config(text="Vous avez gagnez votre jet d'initiative")
            else:
                print("le monstre a l'initiative")
                initLabel.config(text="Le monstre gagne le jet d'initiative")
                dmg = startHp - initHp
                updateLabel(startHp, dmg, False)
                heroHpLabel.config(text=str(initHp))

        def updateLabel(hp,dmg,isHero):
            if isHero:
                heroDmgLabel.place(x=300, y=30)
                heroDmgLabel.config(text="hero deal : " + str(dmg))
                monsterHpLabel.config(text=str(hp))
            else:
                monsterDmgLabel.place(x=300, y=300)
                monsterDmgLabel.config(text="monster deal : " + str(dmg))
                heroHpLabel.config(text=str(hp))

        def attack(selectWeapon,button):
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
                Combatframe.destroy()
                self.winFrame()
            else:
                heroHpbeforeHit = combat.hero_hp
                heroHp = combat.hero_get_damaged()
                monsterdmgDeal = heroHpbeforeHit - heroHp
                updateLabel(heroHp, monsterdmgDeal, False)
                if combat.hero_is_dead() == 0:
                    Combatframe.destroy()
                    self.deadFrame()
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
                                                  command=lambda weapon=weapon, count=count: attack(weapon.get('name'),selectButton),
                                                  border=0, activebackground='#12c4c0', bg="#12c4c0"))
                selectButton[count].place(x=x, y=500)
                x += 100

        def inventaire():
            print("ceci est une ouverture d'inventaire")

        def fuite():
            print("Vous tentez de prendre la fuite")


        AttackButton = Button(Combatframe, text="Attack", command=selectWeapon, border=0, activebackground='#12c4c0',
                              bg="#12c4c0")
        AttackButton.place(x=750, y=500)

        InventaireButton = Button(Combatframe, text="Inventaire", command=inventaire, border=0, activebackground='#12c4c0',
                              bg="#12c4c0")
        InventaireButton.place(x=850, y=500)

        FuiteButton = Button(Combatframe, text="Fuite", command=fuite, border=0, activebackground='#12c4c0',
                              bg="#12c4c0")
        FuiteButton.place(x=850, y=550)

        heroDmgLabel = Label(Combatframe, text="",fg='white', bg='black')
        heroDmgLabelfont = ('Calirbi (Body)', 24, 'bold')
        heroDmgLabel.config(font=heroDmgLabelfont)


        monsterDmgLabel = Label(Combatframe, text="", fg='white', bg='black')
        monsterDmgLabelfont = ('Calirbi (Body)', 24, 'bold')
        monsterDmgLabel.config(font=monsterDmgLabelfont)


        heroHpLabel = Label(Combatframe, text=str(hero.get('pdv')), fg='white', bg='black')
        heroHpLabelfont = ('Calirbi (Body)', 24, 'bold')
        heroHpLabel.config(font=heroHpLabelfont)
        heroHpLabel.place(x=30, y=30)

        monsterHpLabel = Label(Combatframe, text=str(combat.monster_hp), fg='white', bg='black')
        monsterHpLabelfont = ('Calirbi (Body)', 24, 'bold')
        monsterHpLabel.config(font=monsterHpLabelfont)
        monsterHpLabel.place(x=30, y=300)

        initLabel = Label(Combatframe, text="", fg='white', bg='black')
        initLabelfont = ('Calirbi (Body)', 24, 'bold')
        initLabel.config(font=initLabelfont)
        initLabel.place(x=200, y=150)

        nameLabel = Label(Combatframe, text="vous rencontrer un " + str(self.rooms.monsters[self.actualMonster]), fg='white', bg='black')
        nameLabelfont = ('Calirbi (Body)', 24, 'bold')
        nameLabel.config(font=nameLabelfont)
        nameLabel.place(x=100, y=100)

        whoStart(heroHp,combat.hero_hp)

    def deadFrame(self):
        deadFrame = Frame(self.q, width=1024, height=600)
        deadFrame.place(x=0, y=0)
        deadFrame.lower()

        image_path = os.path.join(self.base_folder, '../medias/dead.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas1 = Canvas(deadFrame, width=1024, height=600)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        canvas1.image = bg

        def Retry():
            self.donjonRoom = 0
            deadFrame.destroy()
            self.textWelcomeFrame()

        retryButton = Button(deadFrame, text="Retry", command=Retry, border=0, activebackground='#12c4c0',
                              bg="#12c4c0")
        retryButton.place(x=500, y=300)

    def winFrame(self):
        winFrame = Frame(self.q, width=1024, height=600)
        winFrame.place(x=0, y=0)
        winFrame.lower()

        image_path = os.path.join(self.base_folder, '../medias/win.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas1 = Canvas(winFrame, width=1024, height=600)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        canvas1.image = bg

        def next():
            winFrame.destroy()
            self.donjonRoom += 1
            self.actualMonster += 1
            self.questStartedFrame()

        nextButton = Button(winFrame, text="next", command=next, border=0, activebackground='#12c4c0',
                              bg="#12c4c0")
        nextButton.place(x=500, y=300)

        winLabel = Label(winFrame, text="bravo vous avez vaincu "+str(self.rooms.monsters[self.actualMonster]), fg='white', bg='black')
        winLabelfont = ('Calirbi (Body)', 24, 'bold')
        winLabel.config(font=winLabelfont)
        winLabel.place(x=200, y=150)

    def new_person_frame(self):
        """
        Create new person page
        """
        frame = Frame(self.q, width=1024, height=600, bg="#FFF")

        # main message
        Label(self.q,
              text="Créer votre personnage",
              bg="white",
              font=('Calibri (Body)', 24, 'bold')).pack()

        # main_message = tk.Text(self.q, text='Créer un personnage', fg='black')
        # main_message.config(font=('Calibri (Body)', 24, 'bold'))

        # name label
        name_label = tk.StringVar(self.q)
        name_label.set("Nom")
        Label(self.q, textvariable=name_label, bg="white").pack()

        # name entry
        name = tk.StringVar(self.q)
        Entry(self.q, textvariable=name, width=100, bd=3).pack()

        # age label
        age_label = tk.StringVar(self.q)
        age_label.set("Age")
        Label(self.q, textvariable=age_label, bg="white").pack()

        # age entry
        age = tk.IntVar(self.q)
        Entry(self.q, textvariable=age, width=100, bd=3).pack()

        # eyes label
        eyes_label = tk.StringVar(self.q)
        eyes_label.set("Yeux")
        Label(self.q, textvariable=eyes_label, bg="white").pack()

        # eyes entry
        eyes = tk.StringVar(self.q)
        Entry(self.q, textvariable=eyes, width=100, bd=3).pack()

        # height label
        height_label = tk.StringVar(self.q)
        height_label.set("Taille (en centimètres)")
        Label(self.q, textvariable=height_label, bg="white").pack()

        # height entry
        height = tk.IntVar(self.q)
        Entry(self.q, textvariable=height, width=100, bd=3).pack()

        # weight label
        weight_label = tk.StringVar(self.q)
        weight_label.set("Poids (en Kilogrammes)")
        Label(self.q, textvariable=weight_label, bg="white").pack()

        # weight entry
        weight = tk.IntVar(self.q)
        Entry(self.q, textvariable=weight, width=100, bd=3).pack()

        # skin label
        skin_label = tk.StringVar(self.q)
        skin_label.set("Couleur de peau")
        Label(self.q, textvariable=skin_label, bg="white").pack()

        # skin entry
        skin = tk.StringVar(self.q)
        Entry(self.q, textvariable=skin, width=100, bd=3).pack()

        # race label
        race_label = tk.StringVar(self.q)
        race_label.set("Origine ethnique")
        Label(self.q, textvariable=race_label, bg="white").pack()

        # race entry
        race = tk.StringVar(self.q)
        Entry(self.q, textvariable=race, width=100, bd=3).pack()

        # class label
        class_label = tk.StringVar(self.q)
        class_label.set("Classe")
        Label(self.q, textvariable=class_label, bg="white").pack()

        # class entry
        class_entry = tk.StringVar(self.q)
        Entry(self.q, textvariable=class_entry, width=100, bd=3).pack()

        # alignment label
        alignment_label = tk.StringVar(self.q)
        alignment_label.set("Alignement")
        Label(self.q, textvariable=alignment_label, bg="white").pack()

        # alignment entry
        alignment = tk.StringVar(self.q)
        Entry(self.q, textvariable=alignment, width=100, bd=3).pack()

        # pe label
        pe_label = tk.StringVar(self.q)
        pe_label.set("PE")
        Label(self.q, textvariable=pe_label, bg="white").pack()

        # pe entry
        pe = tk.IntVar(self.q)
        Entry(self.q, textvariable=pe, width=100, bd=3).pack()

        # strength label
        strength_label = tk.StringVar(self.q)
        strength_label.set("Force")
        Label(self.q, textvariable=pe_label, bg="white").pack()

        # strength entry
        strength = tk.IntVar(self.q)
        Entry(self.q, textvariable=strength, width=100, bd=3).pack()

        # dexterity label
        dexterity_label = tk.StringVar(self.q)
        dexterity_label.set("Dextérité")
        Label(self.q, textvariable=dexterity_label, bg="white").pack()

        # dexterity entry
        dexterity = tk.IntVar(self.q)
        Entry(self.q, textvariable=dexterity, width=100, bd=3).pack()

        # intelligence label
        intelligence_label = tk.StringVar(self.q)
        intelligence_label.set("Intelligence")
        Label(self.q, textvariable=intelligence_label, bg="white").pack()

        # intelligence entry
        intelligence = tk.IntVar(self.q)
        Entry(self.q, textvariable=intelligence, width=100, bd=3).pack()

        # charisma label
        charisma_label = tk.StringVar(self.q)
        charisma_label.set("Charisme")
        Label(self.q, textvariable=charisma_label, bg="white").pack()

        # charisma entry
        charisma = tk.IntVar(self.q)
        Entry(self.q, textvariable=charisma, width=100, bd=3).pack()

        # constitution label
        constitution_label = tk.StringVar(self.q)
        constitution_label.set("Constitution")
        Label(self.q, textvariable=constitution_label, bg="white").pack()

        # constitution entry
        constitution = tk.IntVar(self.q)
        Entry(self.q, textvariable=constitution, width=100, bd=3).pack()

        # wisdom label
        wisdom_label = tk.StringVar(self.q)
        wisdom_label.set("Sagesse")
        Label(self.q, textvariable=constitution_label, bg="white").pack()

        # wisdom entry
        wisdom = tk.IntVar(self.q)
        Entry(self.q, textvariable=wisdom, width=100, bd=3).pack()

        # speed label
        speed_label = tk.StringVar(self.q)
        speed_label.set("Vitesse")
        Label(self.q, textvariable=speed_label, bg="white").pack()

        # speed entry
        speed = tk.IntVar(self.q)
        Entry(self.q, textvariable=speed, width=100, bd=3).pack()

        # function executed when form submitted
        def create_person():
            person = Person(name,
                            age,
                            eyes,
                            height,
                            weight,
                            skin,
                            race,
                            class_entry,
                            alignment,
                            pe,
                            strength,
                            dexterity,
                            intelligence,
                            charisma,
                            constitution,
                            wisdom,
                            speed
                            )
            person.save()

        # submit button
        tk.Button(self.q,
                  text='Créer',
                  height=1,
                  width=10,
                  command=create_person).pack()

        frame.place(x=0, y=0)
        frame.lower()
