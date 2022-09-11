from ctypes import resize
import json
import logging
import time
from tkinter import *
from tkinter.ttk import Combobox
from turtle import width
from xxlimited import new
import pygame
import os
import tkinter as tk
from random import *
from functools import partial
from PIL import Image, ImageTk


from Rooms.rooms import Room
from    Utils.load_json import LoadJson
from    Utils.load_json import LoadJson
from Window.quest import start_quest_frame
from Utils.Sound import Sound


def renderReward(self,frame,item, x,y,Playsound):
    
    def onEnterMouse(event):
        frame.itemconfigure(NameItem, text=item["NameItem"])
        frame.itemconfigure(DescriptionItem, text=item["DescriptionItem"])
        Playsound('button_menu')


    def onExitMouse(event):
        frame.itemconfigure(NameItem, text="")
        frame.itemconfigure(DescriptionItem, text="")


    # logging.getLogger('PIL').setLevel(logging.WARNING)
    img=(Image.open(os.path.join(self.base_folder, '../medias/'+item["ImageItem"]+'.png')))
    resized_image= img.resize((100,100), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)
    # frame.create_image(10,10, anchor=NW, image=new_image)



    itemImagePath = os.path.join(self.base_folder, '../medias/'+item["ImageItem"]+'.png')
    # image = PhotoImage(file=itemImagePath)
    itemContainer = Canvas(frame, width=100,height=100, bd=1, highlightthickness=0, bg="black")
    itemContainer.pack()
    itemContainer.create_image(0,0,anchor="nw", image=new_image)
    itemContainer.image = new_image
    itemContainer.place(x=x,y=y)
    itemContainer.bind('<Enter>',onEnterMouse)
    itemContainer.bind('<Leave>',onExitMouse)

    nameItemFont = ('Calibri (Body)', 16, 'bold','italic','underline')
    descriptionItemFont =  ('Calibri (Body)', 14, 'bold','italic')

    NameItem = frame.create_text(512/2, 540, text="",fill="white", justify="center",font=nameItemFont)
    DescriptionItem = frame.create_text(512/2, 580, text="",fill="white", justify="center",font=descriptionItemFont)


    

def renderQuest(self, frame, Playsound, quest,x,y,choice):

    def onEnterMouse(event):
        Playsound('selection')
        questContainer["bg"] ="white"

    def onExitMouse(event):
        questContainer["bg"] ="black"



    img=(Image.open(os.path.join(self.base_folder, '../medias/'+quest["Image"]+'.png')))
    resized_image= img.resize((512,700), Image.ANTIALIAS)
    new_image= ImageTk.PhotoImage(resized_image)

    # questImagePath = os.path.join(self.base_folder, '../medias/'+quest["Image"]+'.png')
    # new_image = PhotoImage(file=questImagePath)
    questContainer = Canvas(frame, width=512, height=700, bd=2, highlightthickness=0, bg="black")
    questContainer.pack(fill="both", expand=True)
    questContainer.create_image(0, 0, image=new_image, anchor="nw")
    questContainer.image = new_image
    questContainer.place(x=x, y=y)
    questContainer.bind('<Enter>',onEnterMouse)
    questContainer.bind('<Leave>',onExitMouse)

    questLabelFont = ('Calibri (Body)', 24, 'bold','italic','underline')
    difficultyFont =  ('Calibri (Body)', 16, 'bold','italic')
    descriptionFont = ('Calibri (Body)', 20, 'bold')
    rewardLabelFont =  ('Calibri (Body)', 18,'bold', 'italic')

    questContainer.create_text(512/2, 50, text=quest["Name"],fill="white", justify="center",font=questLabelFont)
    questContainer.create_text(512/2, 150, text="Description :" + "\n" + quest["Description"], fill="white", justify="center",font=descriptionFont)
    questContainer.create_text(512/2, 250, text="Difficulty :" + quest["Difficulty"], fill="white", justify="center",font=difficultyFont)
    questContainer.create_text(512/2, 340, text='Rewards Available' ,fill="white", justify="center",font=rewardLabelFont)

    for i, reward in enumerate(quest["Rewards"]):
        renderReward(self, questContainer, reward,60 + 240 * i, 400,Playsound)

    startButton = Button(questContainer, text="Commencer", command=choice,border=0,activebackground='#12c4c0',bg="#12c4c0")
    startButton.place(relx=0.5, rely=0.9, anchor="center")

def Quest(self):

    json = LoadJson()
    questJson = json.load(os.path.join(self.base_folder, '../../Datas/Story/quest.json'))
    
    w = self.q.winfo_screenwidth()
    h = self.q.winfo_screenheight()

    def Playsound(nameSound):
        Sound.play(self.base_folder, nameSound + ".wav")

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
        renderQuest(self,questFrame, Playsound,quest, 150 + 550 * i, 200,choice)
