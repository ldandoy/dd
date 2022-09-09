from tkinter import *
import pygame
import os
from random import *
from tkinter import *

from Utils.load_json import LoadJson
from Window.character_selection import character_selection_frame
from Window.new_character import new_character_frame
from Utils.load_json import LoadJson
from Utils.Sound import Sound
from News.News import News

from Window.character_selection import character_selection_frame


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
        self.news = News.getAllNews(self.base_folder)
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
        homeFrame = Frame(self.q, width=1024, height=600)
        homeFrame.place(x=0, y=0)
        homeFrame.lower()
        textwelcomeframe = Frame(self.q)

        bg_image_path = os.path.join(
            self.base_folder, '../medias/montagne.png')
        background_image = PhotoImage(file=r'' + bg_image_path)
        background_canvas = Canvas(homeFrame, width=1024, height=600)
        background_canvas.pack(fill="both", expand=True)
        background_canvas.create_image(
            0, 0, image=background_image, anchor="nw")
        background_canvas.image = background_image

        home_title = Label(homeFrame, text="Bienvenue dans Donjon et Dragon", fg='black',
                           bg="white")
        home_title.config(font=('Calibri (Body)', 36, 'bold'))
        home_title.place(x=250, y=100)

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
        PlayButton = Button(textwelcomeframe, text="Jouer", command=play, border=0, activebackground='#12c4c0',
                            bg="#12c4c0")
        PlayButton.place(x=950, y=550)

        # TODO : This is not used and we're discussing about deleting it
        # Button(self.q, text='Menu',
        #        border=0, bg="#12c4c0").place(x=5, y=10)

        # Button to create a character 
        PersoButton = Button(textwelcomeframe, text="Creation de perso", command=perso, border=0, activebackground='#12c4c0',
                            bg="#12c4c0")
        PersoButton.place(x=820, y=550)
