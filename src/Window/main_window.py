import json
import time
from tkinter import *
from turtle import width
import pygame
import os
import tkinter as tk
from random import *
from functools import partial

from Perso.perso import Perso
from Perso.person import Person
from Utils.last_features import GetLastFeatures
from Utils.load_json import LoadJson
from Inventory.inventory import Inventory
from Rooms.rooms import Room
from Combat.combat import Combat
from Window.character_selection import character_selection_frame
from Window.new_character import new_character_frame
from Window.news_frame import newsShowMoreFrame
from Utils.logger import debug
from Window.quest import quest_frame, start_quest_frame
from Utils.Sound import Sound


# TODO: a lot of refactoring in this folder :pensive:

class MainWindow:
    def __init__(self):
        self.base_folder = os.path.dirname(__file__)
        self.q = Tk()
        self.q.title("Donjon & Dragon")
        # TODO: Dynamic window resizing
        pygame.mixer.init()
        w = self.q.winfo_screenwidth()
        h = self.q.winfo_screenheight()
        self.q.geometry(f"{w}x{h}")
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
            if self.newsToggleFrameOpen:
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
            pygame.mixer.init()
            Sound.play(self.base_folder, "button_menu")

            character_selection_frame(self)

        def perso():
            new_character_frame(self)

        # Button to start the game
        PlayButton = Button(textwelcomeframe, text="Jouer", command=play, border=0, activebackground='#12c4c0',
                            bg="#12c4c0")
        PlayButton.place(x=950, y=550)

        # Button to create a character 
        PersoButton = Button(textwelcomeframe, text="Creation de perso", command=perso, border=0, activebackground='#12c4c0',
                            bg="#12c4c0")
        PersoButton.place(x=820, y=550)