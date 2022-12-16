from tkinter import *
import tkinter as tk
from random import *
from Perso.person import Person
from Utils.Sound import Sound
from Perso.PointCharacter import PointCharacter
from Utils.utils import imageTk
from Perso.CreateCharacter import CreateCharacter


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


def new_character_stats_frame(self, person: CreateCharacter, destroyParent):

    """
    Create new person page
    """
    containerFrame = Canvas(self.q)
    containerFrame.place(x=0, y=0, width=self.w, height=self.h)

    frame = Frame(containerFrame, width=self.w, height=self.h )
    vcmd = (frame.register(isDigit))

    # background
    bg = imageTk(self, "new_person")
    background_label = tk.Label(frame, image=bg)
    background_label.place(x=0, y=0, width=self.w, height=self.h)
    background_label.image = bg

    scrollbar = Scrollbar(frame)
    # main message
    Label(frame,
        text="Créer votre personnage",
        bg='black',
        fg='white',
        font=('Calibri (Body)', 24, 'bold')).grid(column=0, row=1)

    lbl = Label(frame, text="Point restants 5")

    lbl.grid(column=0, row=2)
    
    stats = reloadPointStats(frame, lbl, person.race)

    indexRow = 2

    # detroy actual frame
    def returnPage():
        containerFrame.pack_forget()
        containerFrame.destroy()

    # function executed when form submitted
    def create_person():
        personSaved = Person(
            person.name,
            person.age,
            person.eyes,
            person.height,
            person.weight,
            person.skin,
            person.race,
            person.class_entry,
            person.alignment,
            stats.getPointsFor("force"),
            stats.getPointsFor("dexterite"),
            stats.getPointsFor("intelligence"),
            stats.getPointsFor("charisme"),
            stats.getPointsFor("constitution"),
            stats.getPointsFor("sagesse"),
            stats.getPointsFor("vitesse")
        )
        # verify inputs
        errors_messages = personSaved.verify_inputs()

        # if there are errors, then display them in a list box
        if len(errors_messages) > 0:
            errors_list.delete(0, END)
            errors_list.insert(END, "ERREUR DE FORMULAIRE:")
            for msg in errors_messages:
                errors_list.insert(END, msg)

            errors_list.grid(column=0, row=20, columnspan=5)
            scrollbar.config(command=errors_list.yview)

        else:
            personSaved.save()
            Sound.play(self.base_folder, "perso_created")
            destroyParent()
            returnPage()

    # submit button
    indexRow = 7 + 4
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

    # for display errors
    # scrollbar.pack_forget()
    indexRow += 1
    scrollbar.grid(column=0, row=indexRow, columnspan=3)
    errors_list = Listbox(frame, width=65)


    frame.pack(fill="both", expand=TRUE)
