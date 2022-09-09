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
from Utils.Sound import Sound


def render(self, frame, Playsound, quest,x,y,choice):
        questImagePath = os.path.join(self.base_folder, '../medias/'+quest["Image"]+'.png')
        image = PhotoImage(file=questImagePath)
        questContainer = Canvas(frame, width=512, height=512, bd=2, highlightthickness=0, bg="black")
        questContainer.pack(fill="both", expand=True)
        questContainer.create_image(0, 0, image=image, anchor="nw")
        questContainer.image = image
        questContainer.place(x=x, y=y)
        questContainer.bind('<Enter>',Playsound)
        textFont = ('Calibri (Body)', 24, 'bold','italic','underline')

        questContainer.create_text(512/2, 100, text=quest["Name"] + "\n\n" + quest["Difficulty"], fill="white", justify="center",font=textFont)
        # questContainer.create_text(512/2, 150, text='Rewards Available' ,fill="red", justify="center",font=textFont)

        startButton = Button(questContainer, text="Commencer",
                                command=choice,
                                border=0,
                                activebackground='#12c4c0',
                                bg="#12c4c0")
        startButton.place(relx=0.5, rely=0.8, anchor="center")

def Quest(self):


    json = LoadJson()
    questJson = json.load(os.path.join(self.base_folder, '../../Datas/Story/quest.json'))
    
    w = self.q.winfo_screenwidth()
    h = self.q.winfo_screenheight()

    def Playsound(event):
        Sound.play(self.base_folder, "selection.wav")



    def choice():
        questFrame.pack_forget()
        questFrame.destroy()
        self.rooms = Room()
        
        start_quest_frame(self)

    questFrame = Frame(self.q, width=1920, height=1080)
    backgroundImagePath = os.path.join(self.base_folder, '../medias/city4.png')
    bgImage = PhotoImage(file=r'' + backgroundImagePath, width=w, height=h)
    mainCanvas = Canvas(questFrame, width=w, height=h, bd=0, highlightthickness=0)
    mainCanvas.pack(fill="both",expand=TRUE)
    mainCanvas.create_image(0, 0, image=bgImage, anchor="nw")
    mainCanvas.image = bgImage
    labelTextcityFrame_config = ('Calibri (Body)', 30, 'bold')
    mainCanvas.create_text(w/2,100,fill='white', anchor='c',text="Bienvenue à Erthilia " + self.perso.get('name') + ",\n Quel destin veux-tu choisir ?", font=labelTextcityFrame_config,justify='center')
    questFrame.pack(expand=TRUE)


    for i, quest in enumerate(questJson):
        render(self,questFrame, Playsound,quest, 150 + 550 * i, 200,choice)
