import json
import os
import time
import tkinter as tk
from functools import partial
from random import *
from tkinter import *

import pygame
from Perso.person import Person
from Window.new_character import new_character_frame
from Window.city import cityFrame
from Utils.Sound import Sound
from Window.QuestScreen import Quest

from Window.city import cityFrame


def character_selection_frame(self):
    character_frame = Frame(self.q, width=1024, height=600)
    image2_path = os.path.join(self.base_folder, '../medias/forest.png')
    bg2 = PhotoImage(file=image2_path)
    canvas2 = Canvas(character_frame, width=1024, height=600)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bg2, anchor="nw")
    canvas2.image = bg2
    print(character_frame)
    # About character -------
    card = Canvas(character_frame, width=650, height=154)
    card.place(x=105, y=420)

    # Title of window -------
    lwelcome = Label(character_frame, text="Choisissez votre personnage", fg='white', bg='black')
    lwelcomefont = ('Calibri (Body)', 24, 'bold')
    lwelcome.config(font=lwelcomefont)
    lwelcome.place(x=105, y=30)


    # Play song
    Sound.background(self.base_folder, "epic.ogg")

    def choice() -> None:
        """
        The selected champion is sending in the city frame then the choice button is clicked
        """
        character_frame.pack_forget()
        character_frame.destroy()

        Quest(self)
        Sound.play(self.base_folder, "button_menu")


    ChoiceButton = Button(character_frame, text="Choisir", command=choice, state=DISABLED, border=0,
                          activebackground='#12c4c0', bg="#12c4c0", width=27, height=7)
    ChoiceButton.place(x=780, y=420)

    # select champion ------
    def selected(perso, count) -> None:
        Sound.play(self.base_folder, "clic_person", volume=1)

        card.delete('all')
        ChoiceButton['state'] = NORMAL
        self.perso = Person.perso_choose(perso)
        if 'description' in self.perso.keys():
            descr = self.descr = self.perso['description']
            card.create_text(199, 26, fill="black", font="Helvetica",
                             text=descr, width=400, justify=LEFT)

    selectButton = []
    persoJson = Person.list_person()
    tempPerso = []
    for person in persoJson:
        print(person)
        if person.split('.')[1] ==  "json":
            tempPerso.append(person)
            print(tempPerso)
    persoJson = tempPerso
    print(persoJson)
    
    x = 105
    y = 100
    count_character = 1

    for count, perso in enumerate(persoJson):
        if count == 4:
            x = 105
            y = 250

        file = os.path.join(os.path.dirname(__file__), "..", 'medias', 'characters',
                            f'{count_character}.png').replace("\\", '/')
        count_character += 1
        imageCharacter = PhotoImage(file=file)
        persoName = perso.split(".")[0]
        perso_button = Button(character_frame,
            image=imageCharacter,
            text=persoName,
            command=lambda perso=perso, count=count: selected(perso, count)
        )
        perso_button.image = imageCharacter

        selectButton.insert(count, perso_button)
        selectButton[count].place(x=x, y=y, width=110, height=110, )
        lName = Label(character_frame, text=persoName,
                      fg='white', bg='#0080FF')
        lNamefont = ('Calibri (Body)', 16, 'bold')
        lName.config(font=lNamefont)
        lName.place(x=x, y=y+100, width=110)
        x += 200

    def returnPage():
        character_frame.pack_forget()
        character_frame.destroy()

    # Button in choice PersoFrame window ChoiceButton = Button(choicePersoFrame, text="Choisir", command=choice,
    # border=0, activebackground='#12c4c0', bg="#12c4c0")
   
    


    #Button to return in the mainWindow
    character_frame.place(x=0, y=0)
    returnButton = Button(character_frame, text="Retour", command=returnPage, border=0,
                        activebackground='#12c4c0', bg="#12c4c0", width=27)
    # ChoiceButton.place(x=950, y=550)

    returnButton.place(x=780, y=550)

  
     