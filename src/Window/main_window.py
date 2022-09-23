from tkinter import *
import pygame
import os
from random import *
from tkinter import *

from Utils.load_json import LoadJson
from Window.character_selection import character_selection_frame
from Window.new_character import new_character_frame
from PIL import Image, ImageTk
from Utils.load_json import LoadJson
from Utils.Sound import Sound
from News.News import News

from Window.character_selection import character_selection_frame


class MainWindow:
    def __init__(self):
        self.base_folder = os.path.dirname(__file__)
        self.q = Tk()
        self.q.title("Donjon & Dragon")
        pygame.mixer.init()
        self.w = self.q.winfo_screenwidth()
        self.h = self.q.winfo_screenheight()
        self.q.geometry(f"{self.w}x{self.h}")
        self.q.configure(bg='')
        self.news = self.getAllNews()
        self.q.attributes('-fullscreen', True)
        # Add no size update
        self.renderHomeScreen()

        self.q.mainloop()

    lastNewsCount = 3
    rooms = []
    perso = None

    donjonRoom = 0
    actualMonster = 0
    difficultFactor = 0

    def getAllNews(self):
        newsList = []
        json = LoadJson()
        filePath = os.path.join(self.base_folder, '../../Datas/News/news.json')
        newsJson = json.load(filePath)
        for news in newsJson:
            newsList.append(News(news, self.q))
        return newsList

    # TODO : This is not used and we're discussing about deleting it
    # def displayMenu(self):
    #     menuFrame = Frame(self.q, width=300, height=600, bg='#12c4c0')
    #     menuFrame.place(x=0, y=0)

    #     def closeMenu():
    #         menuFrame.pack_forget()
    #         menuFrame.destroy()

    #     def createMenuBtn(x, y, text, cmd):

    #         myButton = Button(menuFrame,
    #                           text=text,
    #                           width=42,
    #                           height=2,
    #                           fg="#262626",
    #                           bg="#0f9d9a",
    #                           border=0,
    #                           activeforeground="#262626",
    #                           activebackground="#12c4c0",
    #                           command=cmd)

    #         myButton.place(x=x, y=y)

    #     Button(menuFrame, text="close", command=closeMenu, border=0,
    #            activebackground='#12c4c0', bg="#12c4c0").place(x=5, y=10)

    def renderHomeScreen(self):
        homeFrame = Frame(self.q, width=self.w, height=self.h)
        homeFrame.place(x=0, y=0)
        homeFrame.lower()

        bgImagePath = os.path.join(
            self.base_folder, '../medias/montagne.png')
        image = Image.open(bgImagePath)
        image = image.resize((self.w, self.h), Image.ANTIALIAS)
        bgImage = ImageTk.PhotoImage(image)

        gbCanvas = Canvas(homeFrame, width=self.w, height=self.h)
        gbCanvas.pack(fill="both", expand=True)
        gbCanvas.create_image(
            0, 0, image=bgImage, anchor="nw")
        gbCanvas.image = bgImage

        homeTitle = Label(homeFrame, text="Bienvenue dans Donjon et Dragon", fg='black',
                           bg="white")
        homeTitle.config(font=('Calibri (Body)', 36, 'bold'))
        homeTitle.place(x=self.w/2, y=100, anchor="center")

        for i, news in enumerate(self.news):
            if i > self.lastNewsCount - 1:
                break
            news.render(homeFrame, 70 + 300 * i, 200)

        def play():
            pygame.mixer.init()
            Sound.play(self.base_folder, "button_menu")
            homeFrame.pack_forget()
            homeFrame.destroy()

            character_selection_frame(self)

        def perso():
            new_character_frame(self)

        # Button to start the game
        PlayButton = Button(homeFrame, text="Jouer", command=play, border=0, activebackground='#12c4c0',
                            bg="#12c4c0")
        PlayButton.place(x=950, y=550)

        # TODO : This is not used and we're discussing about deleting it
        # Button(self.q, text='Menu',
        #        border=0, bg="#12c4c0").place(x=5, y=10)

        # Button to create a character 
        PersoButton = Button(homeFrame, text="Creation de perso", command=perso, border=0, activebackground='#12c4c0',
                            bg="#12c4c0")
        PersoButton.place(x=820, y=550)

        myButton = Button(homeFrame,
                              width=42,
                              height=2,
                              fg="#262626",
                              bg="#0f9d9a",
                              border=0,
                              activeforeground="#262626",
                              activebackground="#12c4c0",)


        Button(homeFrame, text="╳", command=self.q.destroy, border=0,
               activebackground='#12c4c0', bg="#12c4c0").place(x=5, y=10)