from ctypes import resize
import json
import time
from tkinter import *
from tkinter.ttk import Combobox
from turtle import width
import pygame
import os
import tkinter as tk
from random import *
from functools import partial

from Rooms.rooms import Room
from Utils.load_json import LoadJson
from Window.quest import start_quest_frame

def QuestChoice():
    print("hello world")



def Quest(self):


    w = self.q.winfo_screenwidth()
    h = self.q.winfo_screenheight()

    def choice():
        questFrame.pack_forget()
        questFrame.destroy()
        self.rooms = Room()
        
        start_quest_frame(self)

    def Playsound(event):
    # Play song
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.Sound(os.path.join(self.base_folder, '../medias/audio/selection.wav')).play()

    questFrame = Frame(self.q, width=1920, height=1080)
    
    image_path = os.path.join(self.base_folder, '../medias/city4.png')
    bg = PhotoImage(file=r'' + image_path, width=w, height=h)

    canvas = Canvas(questFrame, width=w, height=h, bd=0, highlightthickness=0)
    canvas.pack(fill="both",expand=TRUE)
    canvas.create_image(0, 0, image=bg, anchor="nw")
    canvas.image = bg


    labelTextcityFrame_config = ('Calibri (Body)', 30, 'bold')
    canvas.create_text(w/2,50,fill='white', anchor='c',text="Bienvenue à Erthilia " + self.perso.get('name') + ",\n Quel destin veux-tu choisir ?", font=labelTextcityFrame_config,justify='center')

    imagePath = os.path.join(self.base_folder, '../medias/questGiverChar.png')
    image = PhotoImage(file=imagePath)
    canvas2 = Canvas(questFrame, width=256, height=144, bd=0, highlightthickness=0)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=image, anchor="nw")
    canvas2.image = image
    canvas2.place(x=200, y=200)
    canvas2.bind('<Enter>',Playsound)

    canvas2.create_text(128, 50, text="Find the exile of the lake" + "\n" + "Easy", fill="white", justify="center")

    news_Button = Button(canvas2, text="Commencer",
                            border=0,
                            activebackground='#12c4c0',
                            bg="#12c4c0")
    news_Button.place(relx=0.5, rely=0.6, anchor="center")



    ###

    imagePath2 = os.path.join(self.base_folder, '../medias/forgottenTown.png')
    image2 = PhotoImage(file=imagePath2)
    canvas3 = Canvas(questFrame, width=256, height=144,bd=0, highlightthickness=0)
    canvas3.pack(fill="both", expand=True)
    canvas3.create_image(0, 0, image=image2, anchor="nw")
    canvas3.image = image2
    canvas3.place(x=1200, y=200)
    canvas3.bind('<Enter>',Playsound)

    canvas3.create_text(128, 50, text="The forgotten town" + "\n" + "Hard", fill="white", justify="center")

    news_Button2 = Button(canvas3, text="Commencer",
                            border=0,
                            command=choice,
                            activebackground='#12c4c0',
                            bg="#12c4c0")
    news_Button2.place(relx=0.5, rely=0.6, anchor="center")



    questFrame.pack(expand=TRUE)
