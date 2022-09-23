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

races = {
    "human": {"force": 3, "dexterite": 2, "intelligence": 3, "charisme": 2, "constitution": 3, "sagesse": 0, "vitesse": 5},
    "orc": {"force": 5,"dexterite": 2,"intelligence": 1,"charisme": 0,"constitution": 3,"sagesse": 0,"vitesse": 3}
}
def isDigit(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False


def drawBarStats(frame, gridRow=0, label="Force", pointStats=None, who="strenght"):
    def increment():
        print("hello conayaro")
        if pointStats.increment(who):
            drawBarStats(frame, gridRow, label, pointStats, who)

    def decrement():
        print("hello body")
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
    for key in race.keys():
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

    # main_message = tk.Text(self.q, text='Créer un personnage', fg='black')
    # main_message.config(font=('Calibri (Body)', 24, 'bold'))

    lbl = Label(self.q, text="Point restants 5")

    lbl.grid(column=0, row=2)
    
    orcButton = Button(self.q, text="orc", command=lambda: reloadPointStats(self.q, lbl, races["orc"]))
    orcButton.grid(column=0, row=3)
    
    humanButton = Button(self.q, text="human", command=lambda: reloadPointStats(self.q, lbl, races["human"]))
    humanButton.grid(column=1, row=3)
    
    stats = reloadPointStats(self.q, lbl, races["orc"])
        # pe,           à changer
        # strength,     à changer
        # dexterity,    à changer
        # intelligence, à changer
        # charisma,     à changer
        # constitution, à changer
        # wisdom,       à changer
        # speed         à changer
    # # name label
    # name_label = tk.StringVar(self.q)
    # name_label.set("Nom")
    # Label(self.q, textvariable=name_label, bg="black", fg='white').pack()

    # # name entry
    # name = tk.StringVar(self.q)
    # Entry(self.q, textvariable=name, width=100, bd=0).pack()

    # # age label
    # age_label = tk.StringVar(self.q)
    # age_label.set("Age")
    # Label(self.q, textvariable=age_label, bg="black", fg='white').pack()
    # # age entry
    # age = tk.IntVar(self.q)
    # Entry(self.q, textvariable=age, width=100, bd=0, validate='all', validatecommand=(vcmd, '%P')).pack()

    # # eyes label
    # eyes_label = tk.StringVar(self.q)
    # eyes_label.set("Yeux")
    # Label(self.q, textvariable=eyes_label, bg="black", fg='white').pack()

    # # eyes entry
    # eyes = tk.StringVar(self.q)
    # Entry(self.q, textvariable=eyes, width=100, bd=0).pack()

    # # height label
    # height_label = tk.StringVar(self.q)
    # height_label.set("Taille (en centimètres)")
    # Label(self.q, textvariable=height_label, bg="black", fg='white').pack()

    # # height entry
    # height = tk.IntVar(self.q)
    # Entry(self.q, textvariable=height, width=100, bd=0, validate='all', validatecommand=(vcmd, '%P')).pack()

    # # weight label
    # weight_label = tk.StringVar(self.q)
    # weight_label.set("Poids (en Kilogrammes)")
    # Label(self.q, textvariable=weight_label, bg="black", fg='white').pack()

    # # weight entry
    # weight = tk.IntVar(self.q)
    # Entry(self.q, textvariable=weight, width=100, bd=0, validate='all', validatecommand=(vcmd, '%P')).pack()

    # # skin label
    # skin_label = tk.StringVar(self.q)
    # skin_label.set("Couleur de peau")
    # Label(self.q, textvariable=skin_label, bg="black", fg='white').pack()

    # # skin entry
    # skin = tk.StringVar(self.q)
    # Entry(self.q, textvariable=skin, width=100, bd=0).pack()

    # # race label
    # race_label = tk.StringVar(self.q)
    # race_label.set("Origine ethnique")
    # Label(self.q, textvariable=race_label, bg="black", fg='white').pack()

    # # race entry
    # race = tk.StringVar(self.q)
    # Entry(self.q, textvariable=race, width=100, bd=0).pack()

    # # class label
    # class_label = tk.StringVar(self.q)
    # class_label.set("Classe")
    # Label(self.q, textvariable=class_label, bg="black", fg='white').pack()

    # # class entry
    # class_entry = tk.StringVar(self.q)
    # Entry(self.q, textvariable=class_entry, width=100, bd=0).pack()

    # # alignment label
    # alignment_label = tk.StringVar(self.q)
    # alignment_label.set("Alignement")
    # Label(self.q, textvariable=alignment_label, bg="black", fg='white').pack()

    # # alignment entry
    # alignment = tk.StringVar(self.q)
    # Entry(self.q, textvariable=alignment, width=100, bd=0).pack()

    # # pe label
    # pe_label = tk.StringVar(self.q)
    # pe_label.set("PE")
    # Label(self.q, textvariable=pe_label, bg="black", fg='white').pack()

    # # pe entry
    # pe = tk.IntVar(self.q)
    # Entry(self.q, textvariable=pe, width=100, bd=0).pack()

    # # strength label
    # strength_label = tk.StringVar(self.q)
    # strength_label.set("Force")
    # Label(self.q, textvariable=strength_label, bg="black", fg='white').pack()

    # # strength entry
    # strength = tk.IntVar(self.q)
    # Entry(self.q, textvariable=strength, width=100, bd=0, validate='all', validatecommand=(vcmd, '%P')).pack()

    # # dexterity label
    # dexterity_label = tk.StringVar(self.q)
    # dexterity_label.set("Dextérité")
    # Label(self.q, textvariable=dexterity_label, bg="black", fg='white').pack()

    # # dexterity entry
    # dexterity = tk.IntVar(self.q)
    # Entry(self.q, textvariable=dexterity, width=100, bd=0, validate='all', validatecommand=(vcmd, '%P')).pack()

    # # intelligence label
    # intelligence_label = tk.StringVar(self.q)
    # intelligence_label.set("Intelligence")
    # Label(self.q, textvariable=intelligence_label, bg="black", fg='white').pack()

    # # intelligence entry
    # intelligence = tk.IntVar(self.q)
    # Entry(self.q, textvariable=intelligence, width=100, bd=0, validate='all', validatecommand=(vcmd, '%P')).pack()

    # # charisma label
    # charisma_label = tk.StringVar(self.q)
    # charisma_label.set("Charisme")
    # Label(self.q, textvariable=charisma_label, bg="black", fg='white').pack()

    # # charisma entry
    # charisma = tk.IntVar(self.q)
    # Entry(self.q, textvariable=charisma, width=100, bd=0, validate='all', validatecommand=(vcmd, '%P')).pack()

    # # constitution label
    # constitution_label = tk.StringVar(self.q)
    # constitution_label.set("Constitution")
    # Label(self.q, textvariable=constitution_label, bg="black", fg='white').pack()

    # # constitution entry
    # constitution = tk.IntVar(self.q)
    # Entry(self.q, textvariable=constitution, width=100, bd=0, validate='all', validatecommand=(vcmd, '%P')).pack()

    # # wisdom label
    # wisdom_label = tk.StringVar(self.q)
    # wisdom_label.set("Sagesse")
    # Label(self.q, textvariable=wisdom_label, bg="black", fg='white').pack()

    # # wisdom entry
    # wisdom = tk.IntVar(self.q)
    # Entry(self.q, textvariable=wisdom, width=100, bd=0, validate='all', validatecommand=(vcmd, '%P')).pack()

    # # speed label
    # speed_label = tk.StringVar(self.q)
    # speed_label.set("Vitesse")
    # Label(self.q, textvariable=speed_label, bg="black", fg='white').pack()

    # # speed entry
    # speed = tk.IntVar(self.q)
    # Entry(self.q, textvariable=speed, width=100, bd=0, validate='all', validatecommand=(vcmd, '%P')).pack()

    # # for display errors
    # scrollbar = Scrollbar(self.q)
    # scrollbar.pack_forget()
    # scrollbar.pack(side=RIGHT, fill=Y)
    # errors_list = Listbox(self.q, yscrollcommand=scrollbar.set, width=65)

    # # function executed when form submitted
    # def create_person():
    #     person = Person(name,
    #                     age,
    #                     eyes,
    #                     height,
    #                     weight,
    #                     skin,
    #                     race,
    #                     class_entry,
    #                     alignment,
    #                     pe,
    #                     strength,
    #                     dexterity,
    #                     intelligence,
    #                     charisma,
    #                     constitution,
    #                     wisdom,
    #                     speed
    #                     )
    #     # verify inputs
    #     errors_messages = person.verify_inputs()

    #     # if there are errors, then display them in a list box
    #     if len(errors_messages) > 0:
    #         errors_list.delete(0, END)
    #         errors_list.insert(END, "ERREUR DE FORMULAIRE:")

    #         for msg in errors_messages:
    #             errors_list.insert(END, msg)

    #         errors_list.pack(side=LEFT, fill=BOTH)
    #         scrollbar.config(command=errors_list.yview)

    #     else:
    #         person.save()
    #         Sound.play(self.base_folder, "perso_created")
    #     # pygame.mixer.init()
            

    # # submit button
    # tk.Button(self.q,
    #           text='Créer',
    #           height=1,
    #           width=10,
    #           command=create_person).pack()

    frame.place(x=0, y=0)


# name,
# age,          à changer fait
# eyes,
# height,       à changer fait
# weight,       à changer fait
# skin,
# # race,       à changer
# class_entry,  à changer
# alignment,
# pe,           à changer
# strength,     à changer
# dexterity,    à changer
# intelligence, à changer
# charisma,     à changer
# constitution, à changer
# wisdom,       à changer
# speed         à changer
