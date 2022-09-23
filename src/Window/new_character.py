import json
from logging import root
import time
from tkinter import *
import pygame
import os, glob
import tkinter as tk
from random import *
from functools import partial
from Perso.person import Person
from Utils.Sound import Sound
from Perso.PointCharacter import PointCharacter


keysString = {
    "name": "Nom",
    "eyes": "Yeux",
    "skin": "Peau",
    "class_entry": "Classe",
    "alignment": "Alignement",
}
keysInt = {
    "age": "Age",
    "height": "Taille",
    "weight": "Poids",
}

def isDigit(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False


def drawBarStats(frame, gridRow=0, label="Force", pointStats=None, who="strenght"):
    def increment():
        if pointStats.increment(who):
            drawBarStats(frame, gridRow, label, pointStats, who)

    def decrement():
        if pointStats.decrement(who):
            drawBarStats(frame, gridRow, label, pointStats, who)

    w = Canvas(frame, width=100, height=10)
    width = 10
    height = 10
    sepratorWidth = 2

    indexAdded = 0
    for index in range(0, pointStats.max):
        color = "green"
        if index < pointStats.points[who]:
            color = "blue"
        elif indexAdded < pointStats.addedPoints[who]:
            indexAdded += 1
            color = "red"
        w.create_rectangle(width*index+sepratorWidth, 0,
                           width*index+width, height, fill=color, outline=color)

    w.grid(column=1, row=gridRow)

    username_label = Label(frame, text=label)
    username_label.grid(column=0, row=gridRow)

    buttonRemovePoint = Button(frame, width=5, text="-", command=decrement)
    buttonRemovePoint.grid(column=2, row=gridRow)

    buttonAddPoint = Button(frame, width=5, text="+", command=increment)
    buttonAddPoint.grid(column=3, row=gridRow)


def reloadPointStats(frame, label, race):
    pointStats = PointCharacter(label, race)
    indexRow = 4
    for key in pointStats.points.keys():
        drawBarStats(frame, indexRow, key, pointStats=pointStats, who=key)
        indexRow += 1
    return pointStats


def new_character_frame(self):
    vcmd = (self.q.register(isDigit))
    """
    Create new person page
    """
    frame = Frame(self.q, width=1024, height=600)
    print(frame)

    # background
    bg_path = os.path.join('src', 'medias', 'new_person.png')
    bg = PhotoImage(file=bg_path)
    background_label = tk.Label(self.q, image=bg)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.image = bg

    # main message
    Label(self.q,
          text="Créer votre personnage",
          bg='black',
          fg='white',
          font=('Calibri (Body)', 24, 'bold')).grid(column=0, row=1)

    lbl = Label(self.q, text="Point restants 5")

    lbl.grid(column=0, row=2)
    
    orcButton = Button(self.q, text="orc", command=lambda: reloadPointStats(self.q, lbl, "orc"))
    orcButton.grid(column=0, row=3)
    
    humanButton = Button(self.q, text="human", command=lambda: reloadPointStats(self.q, lbl, "human"))
    humanButton.grid(column=1, row=3)
    
    stats = reloadPointStats(self.q, lbl, "orc")
    indexRow = 11
    values = {}

    for key in keysString:
        label = tk.StringVar(self.q)
        label.set(keysString[key])
        Label(self.q, textvariable=label).grid(column=0, row=indexRow)
        # name entry
        value = tk.StringVar(self.q)
        Entry(self.q, textvariable=value, bd=0).grid(column=1, row=indexRow)
        values[key] = value
        indexRow += 1
    for key in keysInt:
        label = tk.StringVar(self.q)
        label.set(keysInt[key])
        Label(self.q, textvariable=label).grid(column=0, row=indexRow)
        # name entry
        value = tk.IntVar(self.q)
        Entry(self.q, textvariable=value, bd=0, validate='all',
              validatecommand=(vcmd, '%P')).grid(column=1, row=indexRow)
        values[key] = value
        indexRow += 1

    # for display errors
    scrollbar = Scrollbar(self.q)
    scrollbar.pack_forget()
    indexRow += 1
    scrollbar.grid(column=0, row=indexRow, columnspan=3)
    errors_list = Listbox(self.q, yscrollcommand=scrollbar.set, width=65)
    # function executed when form submitted
    def create_person():
        person = Person(values["name"],
            values["age"],
            values["eyes"],
            values["height"],
            values["weight"],
            values["skin"],
            stats.race,
            values["class_entry"],
            values["alignment"],
            stats.getPointsFor("force"),
            stats.getPointsFor("dexterite"),
            stats.getPointsFor("intelligence"),
            stats.getPointsFor("charisme"),
            stats.getPointsFor("constitution"),
            stats.getPointsFor("sagesse"),
            stats.getPointsFor("vitesse")
        )
        # verify inputs
        errors_messages = person.verify_inputs()

        # if there are errors, then display them in a list box
        if len(errors_messages) > 0:
            errors_list.delete(0, END)
            errors_list.insert(END, "ERREUR DE FORMULAIRE:")
            for msg in errors_messages:
                errors_list.insert(END, msg)

            errors_list.grid(column=0, row=20, columnspan=5)
            scrollbar.config(command=errors_list.yview)

        else:
            person.save()
            Sound.play(self.base_folder, "perso_created")
        # pygame.mixer.init()
            

    # submit button
    indexRow += 1
    tk.Button(self.q,
        text='Créer',
        height=1,
        width=10,
        command=create_person
    ).grid(column=0, row=indexRow)

    frame.place(x=0, y=0)
