from tkinter import *
import pygame
import os
from random import *
from tkinter import *

from Utils.load_json import LoadJson
from Window.character_selection import character_selection_frame
from Window.new_character_info import new_character_info_frame
from Utils.load_json import LoadJson
from Utils.Sound import Sound
from News.News import NewsList

from Window.character_selection import character_selection_frame
from Utils.utils import imageTk

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
        self.newsList = NewsList(self.getAllNews(), self.q)
        self.q.attributes('-fullscreen', True)
        # Add no size update
        self.renderHomeScreen()

        self.q.mainloop()

    lastNewsCount = 4
    rooms = []
    perso = None

    donjonRoom = 0
    actualMonster = 0
    difficultFactor = 0

    def getAllNews(self):
        allNews = []
        json = LoadJson()
        filePath = os.path.join(self.base_folder, '../../Datas/News/news.json')
        newsJson = json.load(filePath)
        for news in newsJson:
            allNews.append(news)
        return allNews

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
        homeFrame = Frame(self.q, width=self.w, height=self.h, bg='blue')
        homeFrame.place(x=0, y=0)
        # homeFrame.lower()

        bgImage = imageTk(self, "montagne")

        bgCanvas = Canvas(homeFrame, width=self.w, height=self.h)
        bgCanvas.pack(fill="both", expand=True, )
        bgCanvas.create_image(
            0, 0, image=bgImage, anchor="nw")
        bgCanvas.image = bgImage

        homeTitle = Label(homeFrame, text="Bienvenue dans Donjon et Dragon", fg='black',
                           bg="white")
        homeTitle.config(font=('calibri (font)', 36, 'bold'))
        homeTitle.place(x=self.w/2, y=100, anchor="center")

        newsGridCanvas = Canvas(homeFrame, bg="black", width=self.w)
        newsGridCanvas.grid_columnconfigure(tuple(range(5)), weight=1)

        newsGridCanvas.place(x=self.w/2, y=250, anchor="center")

        for i, news in enumerate(self.newsList.newsList):
            if i > self.lastNewsCount - 1:
                break
            newsCard = news.render(newsGridCanvas)
            newsCard.grid(column=i % 5, row=i // 5, pady="20")

        def play():
            pygame.mixer.init()
            Sound.play(self.base_folder, "button_menu")
            # homeFrame.pack_forget()
            # homeFrame.destroy()

            character_selection_frame(self)

        def perso():
            new_character_info_frame(self)

        # Button to see more news
        ShowMoreNewsButton = Button(homeFrame, text="Voir plus d'actualités", command=self.newsList.renderNewsListPage, border=0, activebackground='#12c4c0',font=('calibri (font)', 28, 'bold'), 
                            padx=20, 
                            pady=0,
                            bg="#12c4c0")
        ShowMoreNewsButton.place(relx=.5, rely=.5,anchor= CENTER)

        # Button to start the game
        playButton = Button(homeFrame, text="Jouer", command=play, border=0, activebackground='#12c4c0',font=('calibri (font)', 58, 'bold'), 
                            bg="#12c4c0")
        playButton.place(relx=.5, rely=.70, anchor="center")

        # TODO : This is not used and we're discussing about deleting it
        # Button(self.q, text='Menu',
        #        border=0, bg="#12c4c0").place(x=5, y=10)

        # TODO : This is not used and we're discussing about deleting it
        # Button(self.q, text='Menu',
        #        border=0, bg="#12c4c0").place(x=5, y=10)

        # Button to create a character 
        PersoButton = Button(homeFrame, text="Creation de perso", command=perso, border=0, activebackground='#12c4c0',
                            font=('calibri (font)', 28, 'bold'),
                            bg="#12c4c0",

                            )
        PersoButton.place(relx=.5, rely=.85,anchor= CENTER)
