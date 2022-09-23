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

    """
    Create new person page
    """

    w = self.q.winfo_screenwidth()
    h = self.q.winfo_screenheight()

    frame = Frame(self.q, width=w, height=h)
    vcmd = (frame.register(isDigit))

    # background
    bg_path = os.path.join('src', 'medias', 'new_person.png')
    bg = PhotoImage(file=bg_path)
    background_label = tk.Label(frame, image=bg)
    background_label.place(x=0, y=0, width=w, height=h)
    background_label.image = bg

    # main message
    Label(frame,
        text="Créer votre personnage",
        bg='black',
        fg='white',
        font=('Calibri (Body)', 24, 'bold')).grid(column=0, row=1)

    lbl = Label(frame, text="Point restants 5")

    lbl.grid(column=0, row=2)
    
    orcButton = Button(frame, text="orc", command=lambda: reloadPointStats(frame, lbl, "orc"))
    orcButton.grid(column=0, row=3)
    
    humanButton = Button(frame, text="human", command=lambda: reloadPointStats(frame, lbl, "human"))
    humanButton.grid(column=1, row=3)
    
    stats = reloadPointStats(frame, lbl, "orc")
    indexRow = 11
    values = {}

    for key in keysString:
        label = tk.StringVar(frame)
        label.set(keysString[key])
        Label(frame, textvariable=label).grid(column=0, row=indexRow)
        # name entry
        value = tk.StringVar(frame)
        Entry(frame, textvariable=value, bd=0).grid(column=1, row=indexRow)
        values[key] = value
        indexRow += 1
    for key in keysInt:
        label = tk.StringVar(frame)
        label.set(keysInt[key])
        Label(frame, textvariable=label).grid(column=0, row=indexRow)
        # name entry
        value = tk.IntVar(frame)
        Entry(frame, textvariable=value, bd=0, validate='all',
              validatecommand=(vcmd, '%P')).grid(column=1, row=indexRow)
        values[key] = value
        indexRow += 1

    # for display errors
    scrollbar = Scrollbar(frame)
    scrollbar.pack_forget()
    indexRow += 1
    scrollbar.grid(column=0, row=indexRow, columnspan=3)
    errors_list = Listbox(frame, yscrollcommand=scrollbar.set, width=65)
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
            
    def returnPage():
        frame.pack_forget()
        frame.destroy()

    # submit button
    indexRow += 1
    tk.Button(frame,
        text='Retour',
        height=1,
        width=10,
        command=returnPage
    ).grid(column=0, row=indexRow)
    tk.Button(frame,
        text='Créer',
        height=1,
        width=10,
        command=create_person
    ).grid(column=1, row=indexRow)
    frame.pack(fill="both", expand=TRUE)
