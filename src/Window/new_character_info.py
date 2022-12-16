from tkinter import *
import tkinter as tk
from random import *
from turtle import color
from Utils.Sound import Sound
from Utils.utils import imageTk
from Window.new_character_stats import new_character_stats_frame
from Perso.CreateCharacter import CreateCharacter



def isDigit(P):
    if str.isdigit(P) or P == "":
        return True
    else:
        return False

    
def new_character_info_frame(self):

    """
    Create new person page
    """
    
    # CONTAINER
    frameContainer = Frame(self.q, bg="yellow")

    # background
    bg = imageTk(self, "new_person")
    background_label = tk.Label(frameContainer, image=bg)
    background_label.place(x=0, y=0, width=self.w, height=self.h)
    background_label.image = bg

    # Create new character
    character = CreateCharacter(frameContainer)    

    # INFO
    frameInfo = Frame(frameContainer, bg="green")
    frameInfo.pack(fill="both", expand=True)
    frameContainer.pack(fill="both", expand=TRUE)

    vcmd = (frameInfo.register(isDigit))

    # main message
    Label(
        frameInfo,
        text="Créer votre personnage",
        bg='black',
        fg='white',
        font=('Calibri (Body)', 24, 'bold')
    ).pack()
    
    pady=10
    labelWidth = 20
    values = {}
    errors = {}

    for key in character.keysString:
        frame = Frame(frameInfo)
        frame.pack()
        Label(frame, text=character.keysString[key], width=labelWidth).grid(
            column=0, row=0)
        value = tk.StringVar(frame)
        Entry(frame, textvariable=value, bd=0).grid(column=1, row=0, pady=pady)
        values[key] = value
        error = tk.StringVar(frame)
        Label(frame, text=error, width=labelWidth).grid(
            column=2, row=0)
        errors[key] = error

    frame = Frame(frameInfo)
    frame.pack()
    Label(frame, text="Alignement", width=20).grid(column=0, row=0)

    frameAlignment = Frame(frame)
    frameAlignment.grid(column=1, row=0, pady=10)

    Label(frameAlignment, text="Méchant").grid(column=0, row=0)
    value = tk.IntVar(frameAlignment)
    w2 = Scale(frameAlignment, variable=value, from_=0, to=100, orient=HORIZONTAL)
    w2.set(50)
    values["alignment"] = value
    w2.grid(column=1, row=0)
    Label(frameAlignment, text="Gentille").grid(
        column=2, row=0)
    
    for key in character.keysInt:
        frame = Frame(frameInfo)
        frame.pack()
        Label(frame, text=character.keysInt[key], width=20).grid(column=0, row=0)
        value = tk.IntVar(frame)
        Entry(frame, textvariable=value, bd=0, validate='all',
              validatecommand=(vcmd, '%P')).grid(column=1, row=0, pady=pady)
        values[key] = value
        error = StringVar(frame, value=0)
        Label(frame, text=error, width=labelWidth).grid(column=2, row=0)
        errors[key] = error
    
    def destroyFrame():
        frameContainer.pack_forget()
        frameContainer.destroy()

    # function executed when form submitted
    def next():
        # verify inputs
        character.setValues(values)
        isError = character.validateForm(errors)

        # if there are errors, then display them in a list box
        if isError:
            print("ERRORS FORM")
            print(character.errors)
        else:
            Sound.play(self.base_folder, "clic_person")
            destroyFrame()
            new_character_stats_frame(self, values)

    # return and submit button    
    frameActions = Frame(frameInfo)
    frameActions.pack(pady=10, side=BOTTOM, fill=X)

    tk.Button(frameActions,
        text='Retour',
        height=1,
        width=10,
        command=destroyFrame
    ).pack(side=LEFT, pady=10)

    tk.Button(frameActions,
        text='Suivant',
        height=1,
        width=10,
        command=next
    ).pack(side=RIGHT, pady=10)
