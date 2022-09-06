from tkinter import *
import pygame
import os
from random import *

from Utils.load_json import LoadJson
from Window.character_selection import character_selection_frame
from Window.new_character import new_character_frame
from Utils.Sound import Sound
from src.News.news import News


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
        self.news = self.setNews()
        self.q.attributes('-fullscreen', True)
        # Add no size update

        Button(self.q, command=self.displayMenu, text='Menu',
               border=0, bg="#12c4c0").place(x=5, y=10)

        self.renderHomeScreen()

        self.q.mainloop()

    lastNewsCount = 3
    rooms = []
    perso = None

    donjonRoom = 0
    actualMonster = 0
    difficultFactor = 0

    def setNews(self):
        newsList = []
        json = LoadJson()
        filePath = os.path.join(self.base_folder, '../../Datas/News/news.json')
        newsJson = json.load(filePath)
        for news in newsJson:
            newsList.append(News(news))
        return newsList

    # def newsToggle(self):
    #     self.newsToggleFrameOpen = True
    #     self.newsToggleFrame = Frame(self.q, width=764, height=600, bg='#FFFFFF')
    #     self.newsToggleFrame.place(x=300, y=0)
    #     label_textinfo_config = ('Calibri (Body)', 24, 'bold')

    #     label_textinfo_x_position = 25
    #     label_showmore_y_position = 100
    #     lastFeaturesObj = GetLastFeatures()
    #     label_textinfo_config = ('Calibri (Body)', 24, 'bold')

    #     for i, feature in enumerate(lastFeaturesObj):
    #         label_textinfo = Label(self.newsToggleFrame, text=feature['title'][0:50], fg='white',
    #                                bg='#000000', )
    #         label_textinfo.config(font=label_textinfo_config)
    #         label_textinfo.place(x=100, y=50 + (i * 40))
    #         news_Button = Button(self.newsToggleFrame, text="En savoir plus",
    #                              border=0,
    #                              activebackground='#12c4c0',
    #                              bg="#12c4c0")
    #         news_Button.place(x=5, y=50 + (i * 40))

    #     def newsToggleClose():
    #         self.newsToggleFrame.pack_forget()
    #         self.newsToggleFrame.destroy()

    #     Button(self.newsToggleFrame, text="close", command=newsToggleClose, border=0, activebackground='#12c4c0',
    #            bg="#12c4c0").place(x=650, y=10)

    def displayMenu(self):
        menuFrame = Frame(self.q, width=300, height=600, bg='#12c4c0')
        menuFrame.place(x=0, y=0)

        def closeMenu():
            menuFrame.pack_forget()
            menuFrame.destroy()

        def createMenuBtn(x, y, text, cmd):

            myButton = Button(menuFrame,
                              text=text,
                              width=42,
                              height=2,
                              fg="#262626",
                              bg="#0f9d9a",
                              border=0,
                              activeforeground="#262626",
                              activebackground="#12c4c0",
                              command=cmd)

            myButton.place(x=x, y=y)

        # CRITICAL : this is a fake func
        def newsAction():
            print('News')

        createMenuBtn(0, 80, 'News', newsAction)

        Button(menuFrame, text="close", command=closeMenu, border=0,
               activebackground='#12c4c0', bg="#12c4c0").place(x=5, y=10)

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
            if i > self.lastNewsCount - 1 : break
            news.render(homeFrame, 150 + 300 * i, 200)

        # lastFeaturesObj = GetLastFeatures(3)

        # label_textinfo_config = ('Calibri (Body)', 24, 'bold')

        # label_textinfo_x_position = 25
        # label_showmore_y_position = 100

        # def newsShowMoreFrame(self, feature):
        #     news_show_more_frame = Frame(self.q, width=1024, height=600)

        #     image2_path = os.path.join(self.base_folder, '../medias/news/' + feature['picture'])
        #     bg2 = PhotoImage(file=image2_path)
        #     canvas2 = Canvas(news_show_more_frame, width=1024, height=600)
        #     canvas2.pack(fill="both", expand=True)
        #     canvas2.create_image(0, 0, image=bg2, anchor="nw")
        #     canvas2.image = bg2

        #     for i, info in enumerate(feature):
        #         if (info != 'picture'):
        #             label_textinfo = Label(news_show_more_frame, text=feature[info], fg='white', bg='#0483d1')
        #             label_textinfo.config(font=label_textinfo_config)
        #             label_textinfo.place(x=25, y=label_showmore_y_position + (i * 40))

        #     def choice():
        #         news_show_more_frame.pack_forget()
        #         news_show_more_frame.destroy()

        #         self.textWelcomeFrame()

        #     ChoiceButton = Button(news_show_more_frame, text="retour", command=choice, border=0,
        #                           activebackground='#12c4c0', bg="#12c4c0")
        #     ChoiceButton.place(x=950, y=550)

        #     news_show_more_frame.place(x=0, y=0)
        #     news_show_more_frame.lower()

        # def showMore(feature):
        #     self.newsShowMoreFrameOpen = True
        #     textwelcomeframe.pack_forget()
        #     textwelcomeframe.destroy()
        #     newsShowMoreFrame(self, feature, label_textinfo_config, label_showmore_y_position)

        # for i, feature in enumerate(lastFeaturesObj):
        #     label_textinfo = Label(textwelcomeframe, text=feature['title'][0:50], fg='white',
        #                            bg='#0483d1', )
        #     label_textinfo.config(font=label_textinfo_config)
        #     label_textinfo.place(x=label_textinfo_x_position + (i * 350), y=250)
        #     news_Button = Button(textwelcomeframe, text="En savoir plus", command=partial(showMore, feature),
        #                          border=0,
        #                          activebackground='#12c4c0',
        #                          bg="#12c4c0")
        #     news_Button.place(x=label_textinfo_x_position + (i * 350), y=300)

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

        # Button to create a character 
        PersoButton = Button(textwelcomeframe, text="Creation de perso", command=perso, border=0, activebackground='#12c4c0',
                            bg="#12c4c0")
        PersoButton.place(x=820, y=550)
