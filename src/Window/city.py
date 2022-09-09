import json
import time
from tkinter import *
import pygame
import os
import tkinter as tk
from random import *
from functools import partial

from Rooms.rooms import Room
from Utils.load_json import LoadJson
from Window.quest import start_quest_frame


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
        start_quest_frame(self)

    def SellerChoice():
        cityFrame.pack_forget()
        cityFrame.destroy()
        SellerFrame(self)

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
        cityFrame(self)

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
