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
from News.News import NewsList

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

        bgImagePath = os.path.join(
            self.base_folder, '../medias/montagne.png')
        image = Image.open(bgImagePath)
        image = image.resize((self.w, self.h), Image.ANTIALIAS)
        bgImage = ImageTk.PhotoImage(image)

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
            homeFrame.pack_forget()
            homeFrame.destroy()

            character_selection_frame(self)

        def perso():
            new_character_frame(self)

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

        # Button to create a character 
        PersoButton = Button(homeFrame, text="Creation de perso", command=perso, border=0, activebackground='#12c4c0',
<<<<<<< HEAD
                            font=('calibri (font)', 28, 'bold'),
                            bg="#12c4c0",

                            )
        PersoButton.place(relx=.5, rely=.85,anchor= CENTER)
=======
                            bg="#12c4c0")
        PersoButton.place(x=820, y=550)


    def inventoryToggle(self):
        self.inventoryToggleFrameOpen = True
        self.inventoryToggleFrame = Frame(self.q, width=764, height=600, bg='#FFFFFF')
        self.inventoryToggleFrame.place(x=300, y=0)
        label_textinfo_config = ('Calibri (Body)', 24, 'bold')

        label_textinfo_x_position = 25
        label_showmore_y_position = 100
        lastFeaturesObj = GetLastFeatures()
        label_textinfo_config = ('Calibri (Body)', 24, 'bold')

        for i, feature in enumerate(lastFeaturesObj):
            label_textinfo = Label(self.inventoryToggleFrame, text=feature['title'][0:50], fg='white',
                                   bg='#000000', )
            label_textinfo.config(font=label_textinfo_config)
            label_textinfo.place(x=100, y=50 + (i * 40))
            news_Button = Button(self.inventoryToggleFrame, text="En savoir plus",
                                 border=0,
                                 activebackground='#12c4c0',
                                 bg="#12c4c0")
            news_Button.place(x=5, y=50 + (i * 40))

        def inventoryToggleClose():
            self.inventoryToggleFrame.pack_forget()
            self.inventoryToggleFrame.destroy()

        Button(self.inventoryToggleFrame, text="close", command=inventoryToggleClose, border=0, activebackground='#12c4c0',
               bg="#12c4c0").place(x=650, y=10)

    def inventoryToggleWin(self):
        f1 = Frame(self.q, width=300, height=600, bg='#12c4c0')
        f1.place(x=0, y=0)

        def dele():
            f1.pack_forget()
            f1.destroy()
            if (self.inventoryToggleFrameOpen):
                self.inventoryFrame.pack_forget()
                self.inventoryFrame.destroy()

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
>>>>>>> 6f18642 (inventory button added + inventory page created (in progress))
