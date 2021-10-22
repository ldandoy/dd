from tkinter import *
import tkinter as tk
import os

from src.Perso.Person import Person
from src.Utils.loadJson import LoadJson


class MainWindow:

    def toogle_win(self):
        f1 = Frame(self.q, width=300, height=600, bg='#12c4c0')
        f1.place(x=0, y=0)

        def dele():
            f1.destroy()

        def bttn(x, y, text, bcolor, fcolor, cmd):
            def on_enter(e):
                myButton['background'] = bcolor #ffcc66
                myButton['foreground'] = '#262626' #000d33

            def on_leaves(e):
                myButton['background'] = fcolor
                myButton['foreground'] = '#262626'

            myButton = Button(f1,
                text=text,
                width=42,
                height=2,
                fg="#262626",
                bg=fcolor,
                border=0,
                activeforeground="#262626",
                activebackground=bcolor,
                command=cmd)

            myButton.bind("<Enter>", on_enter)
            myButton.bind("<Leave>", on_leaves)

            myButton.place(x=x, y=y)

        bttn(0, 80, 'A C E R', "#0f9d9a", "#12c4c0", None)
        bttn(0, 117, 'D E L L', "#0f9d9a", "#12c4c0", None)
        bttn(0, 154, 'A P P L E', "#0f9d9a", "#12c4c0", None)
        bttn(0, 191, 'A S U S', "#0f9d9a", "#12c4c0", None)
        bttn(0, 228, 'A C E R', "#0f9d9a", "#12c4c0", None)
        bttn(0, 265, 'S O N Y', "#0f9d9a", "#12c4c0", None)


        Button(f1, text="close", command=dele, border=0, activebackground='#12c4c0', bg="#12c4c0").place(x=5, y=10)

    def __init__(self):
        self.base_folder = os.path.dirname(__file__)
        self.q = Tk()
        self.q.title("Donjon & Dragon")
        self.q.geometry('1024x600')
        self.q.configure(bg='')
        # Add no size update

        Button(self.q, command=self.toogle_win, text='Menu', border=0, bg="#12c4c0").place(x=5, y=10)

        self.TextWelcomeFrame()

        self.q.mainloop()

    def TextWelcomeFrame(self):
        textwelcomeframe = Frame(self.q, width=1024, height=600)
        textwelcomeframe.place(x=0, y=0)
        textwelcomeframe.lower()

        image_path = os.path.join(self.base_folder, '../medias/montagne.png')
        bg = PhotoImage(file=r''+image_path)
        canvas1 = Canvas(textwelcomeframe, width=1024, height=600)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        canvas1.image=bg

        label_textwelcomeframe = Label(textwelcomeframe, text="Bienvenue dans Donjon et Dragon", fg='dark grey', bg=None)
        label_textwelcomeframe_config = ('Calirbi (Body)', 24, 'bold')
        label_textwelcomeframe.config(font=label_textwelcomeframe_config)
        label_textwelcomeframe.place(x=200, y=200)

        def play():
            textwelcomeframe.pack_forget()
            textwelcomeframe.destroy()

            self.ChoicePersoFrame()

        PlayButton = Button(textwelcomeframe, text="Jouer", command=play, border=0, activebackground='#12c4c0', bg="#12c4c0")
        PlayButton.place(x=950, y=550)


    def ChoicePersoFrame(self):
        choicepersoframe = Frame(self.q, width=1024, height=600)

        image2_path = os.path.join(self.base_folder, '../medias/village.png')
        bg2 = PhotoImage(file=image2_path)
        canvas2 = Canvas(choicepersoframe, width=1024, height=600)
        canvas2.pack(fill="both", expand=True)
        canvas2.create_image(0, 0, image=bg2, anchor="nw")
        canvas2.image = bg2

        lwelcome = Label(choicepersoframe, text="Choissez votre personnage", fg='dark grey')
        lwelcomefont = ('Calirbi (Body)', 24, 'bold')
        lwelcome.config(font=lwelcomefont)
        lwelcome.place(x=80, y=100)

        def choice():
            choicepersoframe.pack_forget()
            choicepersoframe.destroy()

            self.QuestFrame()

        def go_to_new_person() -> None:
            choicepersoframe.pack_forget()
            choicepersoframe.destroy()
            self.new_person_frame()

        ChoiceButton = Button(choicepersoframe, text="Choisir", command=choice, border=0, activebackground='#12c4c0', bg="#12c4c0")
        new_button = Button(choicepersoframe, text="Créer un nouveau personnage", command=go_to_new_person, border=0, activebackground='#12c4c0', bg="#12c4c0")
        ChoiceButton.place(x=950, y=550)
        new_button.place(x=775, y=550)

        choicepersoframe.place(x=0, y=0)
        choicepersoframe.lower()

    def QuestFrame(self):
        questframe = Frame(self.q, width=1024, height=600, bg="#FF0000")

        # Get the welcome message
        json = LoadJson()
        quest = json.load(os.path.join(self.base_folder, '../../Datas/Story/initialQuest.json'))

        lwelcome = Label(questframe, text=quest['welcome'], fg='dark grey')
        lwelcomefont = ('Calirbi (Body)', 24, 'bold')
        lwelcome.config(font=lwelcomefont)
        lwelcome.place(x=200, y=200)

        questframe.place(x=0, y=0)
        questframe.lower()

    def new_person_frame(self):
        """
        Create new person page
        """
        frame = Frame(self.q, width=1024, height=600, bg="#FFF")

        # main message
        Label(self.q,
              text="Créer votre personnage",
              bg="white",
              font=('Calibri (Body)', 24, 'bold')).pack()

        # main_message = tk.Text(self.q, text='Créer un personnage', fg='black')
        # main_message.config(font=('Calibri (Body)', 24, 'bold'))

        # name label
        name_label = tk.StringVar(self.q)
        name_label.set("Nom")
        Label(self.q, textvariable=name_label, bg="white").pack()

        # name entry
        name = tk.StringVar(self.q)
        Entry(self.q, textvariable=name, width=100, bd=3).pack()

        # age label
        age_label = tk.StringVar(self.q)
        age_label.set("Age")
        Label(self.q, textvariable=age_label, bg="white").pack()

        # age entry
        age = tk.IntVar(self.q)
        Entry(self.q, textvariable=age, width=100, bd=3).pack()

        # eyes label
        eyes_label = tk.StringVar(self.q)
        eyes_label.set("Yeux")
        Label(self.q, textvariable=eyes_label, bg="white").pack()

        # eyes entry
        eyes = tk.StringVar(self.q)
        Entry(self.q, textvariable=eyes, width=100, bd=3).pack()

        # height label
        height_label = tk.StringVar(self.q)
        height_label.set("Taille (en centimètres)")
        Label(self.q, textvariable=height_label, bg="white").pack()

        # height entry
        height = tk.IntVar(self.q)
        Entry(self.q, textvariable=height, width=100, bd=3).pack()

        # weight label
        weight_label = tk.StringVar(self.q)
        weight_label.set("Poids (en Kilogrammes)")
        Label(self.q, textvariable=weight_label, bg="white").pack()

        # weight entry
        weight = tk.IntVar(self.q)
        Entry(self.q, textvariable=weight, width=100, bd=3).pack()

        # skin label
        skin_label = tk.StringVar(self.q)
        skin_label.set("Couleur de peau")
        Label(self.q, textvariable=skin_label, bg="white").pack()

        # skin entry
        skin = tk.StringVar(self.q)
        Entry(self.q, textvariable=skin, width=100, bd=3).pack()

        # race label
        race_label = tk.StringVar(self.q)
        race_label.set("Origine ethnique")
        Label(self.q, textvariable=race_label, bg="white").pack()

        # race entry
        race = tk.StringVar(self.q)
        Entry(self.q, textvariable=race, width=100, bd=3).pack()

        # class label
        class_label = tk.StringVar(self.q)
        class_label.set("Classe")
        Label(self.q, textvariable=class_label, bg="white").pack()

        # class entry
        class_entry = tk.StringVar(self.q)
        Entry(self.q, textvariable=class_entry, width=100, bd=3).pack()

        # alignment label
        alignment_label = tk.StringVar(self.q)
        alignment_label.set("Alignement")
        Label(self.q, textvariable=alignment_label, bg="white").pack()

        # alignment entry
        alignment = tk.StringVar(self.q)
        Entry(self.q, textvariable=alignment, width=100, bd=3).pack()

        # pe label
        pe_label = tk.StringVar(self.q)
        pe_label.set("PE")
        Label(self.q, textvariable=pe_label, bg="white").pack()

        # pe entry
        pe = tk.IntVar(self.q)
        Entry(self.q, textvariable=pe, width=100, bd=3).pack()

        # strength label
        strength_label = tk.StringVar(self.q)
        strength_label.set("Force")
        Label(self.q, textvariable=pe_label, bg="white").pack()

        # strength entry
        strength = tk.IntVar(self.q)
        Entry(self.q, textvariable=strength, width=100, bd=3).pack()

        # dexterity label
        dexterity_label = tk.StringVar(self.q)
        dexterity_label.set("Dextérité")
        Label(self.q, textvariable=dexterity_label, bg="white").pack()

        # dexterity entry
        dexterity = tk.IntVar(self.q)
        Entry(self.q, textvariable=dexterity, width=100, bd=3).pack()

        # intelligence label
        intelligence_label = tk.StringVar(self.q)
        intelligence_label.set("Intelligence")
        Label(self.q, textvariable=intelligence_label, bg="white").pack()

        # intelligence entry
        intelligence = tk.IntVar(self.q)
        Entry(self.q, textvariable=intelligence, width=100, bd=3).pack()

        # charisma label
        charisma_label = tk.StringVar(self.q)
        charisma_label.set("Charisme")
        Label(self.q, textvariable=charisma_label, bg="white").pack()

        # charisma entry
        charisma = tk.IntVar(self.q)
        Entry(self.q, textvariable=charisma, width=100, bd=3).pack()

        # constitution label
        constitution_label = tk.StringVar(self.q)
        constitution_label.set("Constitution")
        Label(self.q, textvariable=constitution_label, bg="white").pack()

        # constitution entry
        constitution = tk.IntVar(self.q)
        Entry(self.q, textvariable=constitution, width=100, bd=3).pack()

        # wisdom label
        wisdom_label = tk.StringVar(self.q)
        wisdom_label.set("Sagesse")
        Label(self.q, textvariable=constitution_label, bg="white").pack()

        # wisdom entry
        wisdom = tk.IntVar(self.q)
        Entry(self.q, textvariable=wisdom, width=100, bd=3).pack()

        # speed label
        speed_label = tk.StringVar(self.q)
        speed_label.set("Vitesse")
        Label(self.q, textvariable=speed_label, bg="white").pack()

        # speed entry
        speed = tk.IntVar(self.q)
        Entry(self.q, textvariable=speed, width=100, bd=3).pack()

        # function executed when form submitted
        def create_person():
            person = Person(name,
                            age,
                            eyes,
                            height,
                            weight,
                            skin,
                            race,
                            class_entry,
                            alignment,
                            pe,
                            strength,
                            dexterity,
                            intelligence,
                            charisma,
                            constitution,
                            wisdom,
                            speed
                            )
            person.save()

        # submit button
        tk.Button(self.q,
                  text='Créer',
                  height=1,
                  width=10,
                  command=create_person).pack()

        frame.place(x=0, y=0)
        frame.lower()
