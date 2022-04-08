import json
import time
from tkinter import *
import pygame
import os
import tkinter as tk
from random import *
from functools import partial

from src.Perso.perso import Perso
from src.Perso.person import Person
from src.Utils.last_features import GetLastFeatures
from src.Utils.load_json import LoadJson
from src.Inventory.inventory import Inventory
from src.Rooms.rooms import Room
from src.Combat.combat import Combat

from src.Window.news_frame import newsShowMoreFrame
from src.Utils.logger import debug


class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)


class MainWindow:
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

    rooms = []
    json = LoadJson()
    perso = None

    donjonRoom = 0
    actualMonster = 0
    difficultFactor = 0

    newsToggleFrameOpen = False
    newsToggleFrame = None

    def newsToggle(self):
        self.newsToggleFrameOpen = True
        self.newsToggleFrame = Frame(self.q, width=764, height=600, bg='#FFFFFF')
        self.newsToggleFrame.place(x=300, y=0)
        label_textinfo_config = ('Calibri (Body)', 24, 'bold')

        label_textinfo_x_position = 25
        label_showmore_y_position = 100
        lastFeaturesObj = GetLastFeatures()
        label_textinfo_config = ('Calibri (Body)', 24, 'bold')

        for i, feature in enumerate(lastFeaturesObj):
            label_textinfo = Label(self.newsToggleFrame, text=feature['title'][0:50], fg='white',
                                   bg='#000000', )
            label_textinfo.config(font=label_textinfo_config)
            label_textinfo.place(x=100, y=50 + (i * 40))
            news_Button = Button(self.newsToggleFrame, text="En savoir plus",
                                 border=0,
                                 activebackground='#12c4c0',
                                 bg="#12c4c0")
            news_Button.place(x=5, y=50 + (i * 40))

        def newsToggleClose():
            self.newsToggleFrame.pack_forget()
            self.newsToggleFrame.destroy()

        Button(self.newsToggleFrame, text="close", command=newsToggleClose, border=0, activebackground='#12c4c0',
               bg="#12c4c0").place(x=650, y=10)

    def toogleWin(self):
        f1 = Frame(self.q, width=300, height=600, bg='#12c4c0')
        f1.place(x=0, y=0)

        def dele():
            f1.pack_forget()
            f1.destroy()
            if (self.newsToggleFrameOpen):
                self.newsToggleFrame.pack_forget()
                self.newsToggleFrame.destroy()

        def bttn(x, y, text, bcolor, fcolor, cmd):
            def onEnter(e):
                myButton['background'] = bcolor  # ffcc66
                myButton['foreground'] = '#262626'  # 000d33

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

        bttn(0, 80, 'News', "#0f9d9a", "#12c4c0", self.newsToggle)
        bttn(0, 117, 'D E L L', "#0f9d9a", "#12c4c0", None)
        bttn(0, 154, 'A P P L E', "#0f9d9a", "#12c4c0", None)
        bttn(0, 191, 'A S U S', "#0f9d9a", "#12c4c0", None)
        bttn(0, 228, 'A C E R', "#0f9d9a", "#12c4c0", None)
        bttn(0, 265, 'S O N Y', "#0f9d9a", "#12c4c0", None)

        Button(f1, text="close", command=dele, border=0, activebackground='#12c4c0', bg="#12c4c0").place(x=5, y=10)

    def textWelcomeFrame(self):
        textwelcomeframe = Frame(self.q, width=1024, height=600)
        textwelcomeframe.place(x=0, y=0)
        textwelcomeframe.lower()

        image_path = os.path.join(self.base_folder, '../medias/montagne.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas1 = Canvas(textwelcomeframe, width=1024, height=600)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        canvas1.image = bg

        label_textwelcomeframe = Label(textwelcomeframe, text="Bienvenue dans Donjon et Dragon", fg='black',
                                       bg="white")
        label_textwelcomeframe_config = ('Calibri (Body)', 36, 'bold')
        label_textwelcomeframe.config(font=label_textwelcomeframe_config)
        label_textwelcomeframe.place(x=250, y=100)

        lastFeaturesObj = GetLastFeatures(3)

        label_textinfo_config = ('Calibri (Body)', 24, 'bold')

        label_textinfo_x_position = 25
        label_showmore_y_position = 100

        def newsShowMoreFrame(self, feature):
            news_show_more_frame = Frame(self.q, width=1024, height=600)

            image2_path = os.path.join(self.base_folder, '../medias/newsBg/' + feature['picture'])
            bg2 = PhotoImage(file=image2_path)
            canvas2 = Canvas(news_show_more_frame, width=1024, height=600)
            canvas2.pack(fill="both", expand=True)
            canvas2.create_image(0, 0, image=bg2, anchor="nw")
            canvas2.image = bg2

            for i, info in enumerate(feature):
                if (info != 'picture'):
                    label_textinfo = Label(news_show_more_frame, text=feature[info], fg='white', bg='#0483d1')
                    label_textinfo.config(font=label_textinfo_config)
                    label_textinfo.place(x=25, y=label_showmore_y_position + (i * 40))

            def choice():
                news_show_more_frame.pack_forget()
                news_show_more_frame.destroy()

                self.textWelcomeFrame()

            ChoiceButton = Button(news_show_more_frame, text="retour", command=choice, border=0,
                                  activebackground='#12c4c0', bg="#12c4c0")
            ChoiceButton.place(x=950, y=550)

            news_show_more_frame.place(x=0, y=0)
            news_show_more_frame.lower()

        def showMore(feature):
            self.newsShowMoreFrameOpen = True
            textwelcomeframe.pack_forget()
            textwelcomeframe.destroy()
            newsShowMoreFrame(self, feature, label_textinfo_config, label_showmore_y_position)

        for i, feature in enumerate(lastFeaturesObj):
            label_textinfo = Label(textwelcomeframe, text=feature['title'][0:50], fg='white',
                                   bg='#0483d1', )
            label_textinfo.config(font=label_textinfo_config)
            label_textinfo.place(x=label_textinfo_x_position + (i * 350), y=250)
            news_Button = Button(textwelcomeframe, text="En savoir plus", command=partial(showMore, feature),
                                 border=0,
                                 activebackground='#12c4c0',
                                 bg="#12c4c0")
            news_Button.place(x=label_textinfo_x_position + (i * 350), y=300)

        def play():
            textwelcomeframe.pack_forget()
            textwelcomeframe.destroy()

            self.choicePersoFrame()

        PlayButton = Button(textwelcomeframe, text="Jouer", command=play, border=0, activebackground='#12c4c0',
                            bg="#12c4c0")
        PlayButton.place(x=950, y=550)

    def choicePersoFrame(self):

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

        # Title of window -------
        lwelcome = Label(choicePersoFrame, text="Choissez votre personnage", fg='white', bg='black')
        lwelcomefont = ('Calibri (Body)', 24, 'bold')
        lwelcome.config(font=lwelcomefont)
        lwelcome.place(x=105, y=30)

        pygame.mixer.init()

        def playSong() -> None:
            """
            This function load the sound in background
            """
            pygame.mixer.music.load(os.path.join(self.base_folder, '../medias/audio/epic.ogg'))
            pygame.mixer.music.play(loops=0)
            pygame.mixer.music.set_volume(0.5)

        playSong()

        def choice() -> None:
            """
            The selected champion is sending in the city frame then the choice button is clicked
            """
            choicePersoFrame.pack_forget()
            choicePersoFrame.destroy()

            self.cityFrame()

        ChoiceButton = Button(choicePersoFrame, text="Choisir", command=choice, state=DISABLED, border=0,
                              activebackground='#12c4c0', bg="#12c4c0", width=27, height=7)
        ChoiceButton.place(x=780, y=420)

        # select champion ------
        def selected(perso, count) -> None:
            card.delete('all')
            ChoiceButton['state'] = NORMAL
            self.perso = Person.perso_choose(perso)
            displayChampionInformation()

        selectButton = []
        persoJson = Person.list_person()
        print(persoJson)
        x = 105
        y = 100
        count_character = 1

        for count, perso in enumerate(persoJson):
            if count == 4:
                x = 105
                y = 250

            file = os.path.join(os.path.dirname(__file__), "..", 'medias', 'characters',
                                f'{count_character}.png').replace("\\", '/')
            count_character += 1
            imageCharacter = PhotoImage(file=file)
            perso_button = Button(choicePersoFrame,
                                  text=perso,
                                  command=lambda perso=perso, count=count: selected(perso, count),
                                  image=imageCharacter
                                  )
            perso_button.image = imageCharacter

            selectButton.insert(count, perso_button)
            selectButton[count].place(x=x, y=y, width=110, height=110, )

            choicePersoFrame.lower()
            x += 200

        def displayChampionInformation():
            if perso['description']:
                print(self.perso['description'])
                descr = self.descr = self.perso['description']
                card.create_text(199, 26, fill="black", font="Helvetica",
                             text=descr, width=400, justify=LEFT)

        def goToNewPerso() -> None:
            choicePersoFrame.pack_forget()
            choicePersoFrame.destroy()

            self.new_person_frame()

        # Button in choicePersoFrame window
        # ChoiceButton = Button(choicePersoFrame, text="Choisir", command=choice, border=0, activebackground='#12c4c0', bg="#12c4c0")
        new_button = Button(choicePersoFrame, text="Créer un nouveau personnage", command=goToNewPerso, border=0,
                            activebackground='#12c4c0', bg="#12c4c0", width=27)
        # ChoiceButton.place(x=950, y=550)
        new_button.place(x=780, y=550)

        choicePersoFrame.place(x=0, y=0)
        choicePersoFrame.lower()

    def cityFrame(self):
        cityFrame = Frame(self.q, width=1024, height=600, bg="#FF0000")

        image_path = os.path.join(self.base_folder, '../medias/city.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas = Canvas(cityFrame, width=1024, height=600)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")
        canvas.image = bg

        labelTextSeller = Label(cityFrame, text="Bienvenue à Erthilia " + self.perso.get('name') + ", où souhaites-tu "
                                                                                                   "aller?",
                                fg='black', bg='white')
        labelTextcityFrame_config = ('Calibri (Body)', 30, 'bold')
        labelTextSeller.config(font=labelTextcityFrame_config)
        labelTextSeller.place(x=60, y=50)

        def QuestChoice():
            cityFrame.pack_forget()
            cityFrame.destroy()
            self.rooms = Room()
            self.questStartedFrame()

        def SellerChoice():
            cityFrame.pack_forget()
            cityFrame.destroy()
            self.SellerFrame()

        questCharPath = PhotoImage(file=os.path.join(self.base_folder, '../medias/questGiverChar.png'))
        questIconButton = Button(cityFrame,
                                 text="test",
                                 image=questCharPath,
                                 command=QuestChoice
                                 )
        questIconButton.image = questCharPath
        questIconButton.place(x=150, y=150, width=250, height=250, )

        labelTextQuest = Label(cityFrame, text="Commencer une quête\nd'Everard",
                               fg='black', bg='white')
        labelTextcityFrame_config = ('Calibri (Body)', 24, 'bold')
        labelTextQuest.config(font=labelTextcityFrame_config)
        labelTextQuest.place(x=140, y=425)

        sellerIcon = PhotoImage(file=os.path.join(self.base_folder, '../medias/sellerChar.png'))
        sellerIconButton = Button(cityFrame,
                                  text="test",
                                  image=sellerIcon,
                                  command=SellerChoice
                                  )
        sellerIconButton.image = sellerIcon
        sellerIconButton.place(x=650, y=150, width=250, height=250, )

        labelTextSeller = Label(cityFrame, text="Faire le plein chez Ambrose\nla vendeuse d'items",
                                fg='black', bg='white')
        labelTextcityFrame_config = ('Calibri (Body)', 24, 'bold')
        labelTextSeller.config(font=labelTextcityFrame_config)
        labelTextSeller.place(x=625, y=425)

        cityFrame.place(x=0, y=0)
        cityFrame.lower()

    def SellerFrame(self):
        sellerFrame = Frame(self.q, width=1024, height=600, bg="#FF0000")

        image_path = os.path.join(self.base_folder, '../medias/sellerBackground.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas = Canvas(sellerFrame, width=1024, height=600)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=bg, anchor="nw")
        canvas.image = bg

        def goTown():
            sellerFrame.pack_forget()
            sellerFrame.destroy()
            self.cityFrame()

        BackButton = Button(sellerFrame, text="Retourner en ville", command=goTown, border=0,
                            activebackground='#12c4c0', bg="#12c4c0")
        BackButton.place(x=850, y=550)

        json = LoadJson()
        sellerItems = json.load(os.path.join(self.base_folder, '../../Datas/PNJ/AmbroseSeller.json'))

        sellerFrame.place(x=0, y=0)
        sellerFrame.lower()

        print(self.perso)

        # Récupération du wallet du perso s'il existe
        persoWallet = self.perso.get("budget") if self.perso.get("budget") else 0

        labelBudget = Label(sellerFrame, text="Budget : " + str(persoWallet) + " $", fg='white', bg='black')
        labelBudget.config(font=('Calibri (Body)', 28, 'bold'))
        labelBudget.place(x=750, y=30)

        def buy():
            print('acheter')

        for i, item in enumerate(sellerItems["inventaire"]):
            label_itemName = Label(sellerFrame, text=str(item["name"]) + " : ", fg='white', bg='black')
            label_itemName.config(font=('Calibri (Body)', 24, 'bold'))
            label_itemName.place(x=25, y=125 + (i * 40))

            label_itemQuantite = Label(sellerFrame, text="Quantité : " + str(item["quantite"]), fg='white',
                                       bg='black')
            label_itemQuantite.config(font=('Calibri (Body)', 24, 'bold'))
            label_itemQuantite.place(x=label_itemName.winfo_reqwidth() + 50, y=125 + (i * 40))

            label_itemPrix = Label(sellerFrame, text="Prix : " + str(item["prix"]) + " $", fg='white', bg='black')
            label_itemPrix.config(font=('Calibri (Body)', 24, 'bold'))
            label_itemPrix.place(x=label_itemName.winfo_reqwidth() + label_itemQuantite.winfo_reqwidth() + 75,
                                 y=125 + (i * 40))

            BuyButton = Button(sellerFrame, text="Acheter", command=buy, border=0,
                               activebackground='#12c4c0', bg="#12c4c0")
            BuyButton.place(x=label_itemName.winfo_reqwidth() + label_itemQuantite.winfo_reqwidth() +
                              label_itemPrix.winfo_reqwidth() + 100,
                            y=128 + (i * 40))

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

        def inventaire():
            questframe.pack_forget()
            questframe.destroy()
            perso = Perso("andolorion.json")
            inventory = Inventory(perso, self.q)
            inventory.show()
            perso.save()

        InventaireButton = Button(questframe, text="Inventaire", command=inventaire, border=0,
                                  activebackground='#12c4c0',
                                  bg="#12c4c0")
        InventaireButton.place(x=850, y=500)

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
            if difficult <= 5:
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

    def CombatFrame(self, isBoss):
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
                self.winFrame(isBoss)
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
                itemTab[i].place(x=850, y=500 + (i * 25))

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

    def winFrame(self, isBoss):
        winFrame = Frame(self.q, width=1024, height=600)
        winFrame.place(x=0, y=0)
        winFrame.lower()
        if isBoss == 1:
            image_path = os.path.join(self.base_folder, '../medias/sortie.png')
        else:
            image_path = os.path.join(self.base_folder, '../medias/treasure.png')

        bg = PhotoImage(file=r'' + image_path)
        canvas1 = Canvas(winFrame, width=1024, height=600)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        canvas1.image = bg

        def next():
            winFrame.destroy()
            if isBoss == 1:
                self.textWelcomeFrame()
            else:
                self.donjonRoom += 1
                self.actualMonster += 1
                self.questStartedFrame()

        nextButton = Button(winFrame, text="next", command=next, border=0, activebackground='#12c4c0',
                            bg="#12c4c0")
        nextButton.place(x=500, y=300)
        if isBoss == 1:
            winLabel = Label(winFrame,
                             text="bravo vous avez vaincu " + str(self.rooms.boss) + " ici s'achève votre aventure",
                             fg='white', bg='black')
        else:
            winLabel = Label(winFrame, text="bravo vous avez vaincu " + str(self.rooms.monsters[self.actualMonster]),
                             fg='white', bg='black')
        winLabelfont = ('Calibri (Body)', 24, 'bold')
        winLabel.config(font=winLabelfont)
        winLabel.place(x=200, y=150)

    def new_person_frame(self):
        """
        Create new person page
        """
        frame = Frame(self.q, width=1024, height=600)

        # background
        bg_path = os.path.join('src', 'medias', 'new_person.png')
        bg = PhotoImage(file=bg_path)
        background_label = tk.Label(self.q, image=bg)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = bg

        # main message
        Label(self.q,
              text="Créer votre personnage",
              bg='black',
              fg='white',
              font=('Calibri (Body)', 24, 'bold')).pack()

        # main_message = tk.Text(self.q, text='Créer un personnage', fg='black')
        # main_message.config(font=('Calibri (Body)', 24, 'bold'))

        # name label
        name_label = tk.StringVar(self.q)
        name_label.set("Nom")
        Label(self.q, textvariable=name_label, bg="black", fg='white').pack()

        # name entry
        name = tk.StringVar(self.q)
        Entry(self.q, textvariable=name, width=100, bd=0).pack()

        # age label
        age_label = tk.StringVar(self.q)
        age_label.set("Age")
        Label(self.q, textvariable=age_label, bg="black", fg='white').pack()

        # age entry
        age = tk.IntVar(self.q)
        Entry(self.q, textvariable=age, width=100, bd=0).pack()

        # eyes label
        eyes_label = tk.StringVar(self.q)
        eyes_label.set("Yeux")
        Label(self.q, textvariable=eyes_label, bg="black", fg='white').pack()

        # eyes entry
        eyes = tk.StringVar(self.q)
        Entry(self.q, textvariable=eyes, width=100, bd=0).pack()

        # height label
        height_label = tk.StringVar(self.q)
        height_label.set("Taille (en centimètres)")
        Label(self.q, textvariable=height_label, bg="black", fg='white').pack()

        # height entry
        height = tk.IntVar(self.q)
        Entry(self.q, textvariable=height, width=100, bd=0).pack()

        # weight label
        weight_label = tk.StringVar(self.q)
        weight_label.set("Poids (en Kilogrammes)")
        Label(self.q, textvariable=weight_label, bg="black", fg='white').pack()

        # weight entry
        weight = tk.IntVar(self.q)
        Entry(self.q, textvariable=weight, width=100, bd=0).pack()

        # skin label
        skin_label = tk.StringVar(self.q)
        skin_label.set("Couleur de peau")
        Label(self.q, textvariable=skin_label, bg="black", fg='white').pack()

        # skin entry
        skin = tk.StringVar(self.q)
        Entry(self.q, textvariable=skin, width=100, bd=0).pack()

        # race label
        race_label = tk.StringVar(self.q)
        race_label.set("Origine ethnique")
        Label(self.q, textvariable=race_label, bg="black", fg='white').pack()

        # race entry
        race = tk.StringVar(self.q)
        Entry(self.q, textvariable=race, width=100, bd=0).pack()

        # class label
        class_label = tk.StringVar(self.q)
        class_label.set("Classe")
        Label(self.q, textvariable=class_label, bg="black", fg='white').pack()

        # class entry
        class_entry = tk.StringVar(self.q)
        Entry(self.q, textvariable=class_entry, width=100, bd=0).pack()

        # alignment label
        alignment_label = tk.StringVar(self.q)
        alignment_label.set("Alignement")
        Label(self.q, textvariable=alignment_label, bg="black", fg='white').pack()

        # alignment entry
        alignment = tk.StringVar(self.q)
        Entry(self.q, textvariable=alignment, width=100, bd=0).pack()

        # pe label
        pe_label = tk.StringVar(self.q)
        pe_label.set("PE")
        Label(self.q, textvariable=pe_label, bg="black", fg='white').pack()

        # pe entry
        pe = tk.IntVar(self.q)
        Entry(self.q, textvariable=pe, width=100, bd=0).pack()

        # strength label
        strength_label = tk.StringVar(self.q)
        strength_label.set("Force")
        Label(self.q, textvariable=strength_label, bg="black", fg='white').pack()

        # strength entry
        strength = tk.IntVar(self.q)
        Entry(self.q, textvariable=strength, width=100, bd=0).pack()

        # dexterity label
        dexterity_label = tk.StringVar(self.q)
        dexterity_label.set("Dextérité")
        Label(self.q, textvariable=dexterity_label, bg="black", fg='white').pack()

        # dexterity entry
        dexterity = tk.IntVar(self.q)
        Entry(self.q, textvariable=dexterity, width=100, bd=0).pack()

        # intelligence label
        intelligence_label = tk.StringVar(self.q)
        intelligence_label.set("Intelligence")
        Label(self.q, textvariable=intelligence_label, bg="black", fg='white').pack()

        # intelligence entry
        intelligence = tk.IntVar(self.q)
        Entry(self.q, textvariable=intelligence, width=100, bd=0).pack()

        # charisma label
        charisma_label = tk.StringVar(self.q)
        charisma_label.set("Charisme")
        Label(self.q, textvariable=charisma_label, bg="black", fg='white').pack()

        # charisma entry
        charisma = tk.IntVar(self.q)
        Entry(self.q, textvariable=charisma, width=100, bd=0).pack()

        # constitution label
        constitution_label = tk.StringVar(self.q)
        constitution_label.set("Constitution")
        Label(self.q, textvariable=constitution_label, bg="black", fg='white').pack()

        # constitution entry
        constitution = tk.IntVar(self.q)
        Entry(self.q, textvariable=constitution, width=100, bd=0).pack()

        # wisdom label
        wisdom_label = tk.StringVar(self.q)
        wisdom_label.set("Sagesse")
        Label(self.q, textvariable=constitution_label, bg="black", fg='white').pack()

        # wisdom entry
        wisdom = tk.IntVar(self.q)
        Entry(self.q, textvariable=wisdom, width=100, bd=0).pack()

        # speed label
        speed_label = tk.StringVar(self.q)
        speed_label.set("Vitesse")
        Label(self.q, textvariable=speed_label, bg="black", fg='white').pack()

        # speed entry
        speed = tk.IntVar(self.q)
        Entry(self.q, textvariable=speed, width=100, bd=0).pack()

        # for display errors
        scrollbar = Scrollbar(self.q)
        scrollbar.pack_forget()
        scrollbar.pack(side=RIGHT, fill=Y)
        errors_list = Listbox(self.q, yscrollcommand=scrollbar.set, width=65)

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
            # verify inputs
            errors_messages = person.verify_inputs()

            # if there are errors, then display them in a list box
            if len(errors_messages) > 0:
                errors_list.delete(0, END)
                errors_list.insert(END, "ERREUR DE FORMULAIRE:")

                for msg in errors_messages:
                    errors_list.insert(END, msg)

                errors_list.pack(side=LEFT, fill=BOTH)
                scrollbar.config(command=errors_list.yview)

            else:
                person.save()

        # submit button
        tk.Button(self.q,
                  text='Créer',
                  height=1,
                  width=10,
                  command=create_person).pack()

        frame.place(x=0, y=0)
