from tkinter import *
import os
from Utils.loadJson import LoadJson
from Combat.combat import Combat

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

        def combat():
            textwelcomeframe.pack_forget()
            textwelcomeframe.destroy()

            self.CombatFrame()

        PlayButton = Button(textwelcomeframe, text="Jouer", command=play, border=0, activebackground='#12c4c0', bg="#12c4c0")
        PlayButton.place(x=950, y=550)
        CombatButton = Button(textwelcomeframe, text="Combat", command=combat, border=0, activebackground='#12c4c0',
                            bg="#12c4c0")
        CombatButton.place(x=850, y=550)



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

        ChoiceButton = Button(choicepersoframe, text="Choisir", command=choice, border=0, activebackground='#12c4c0', bg="#12c4c0")
        ChoiceButton.place(x=950, y=550)

        choicepersoframe.place(x=0, y=0)
        choicepersoframe.lower()

    def QuestFrame(self):
        questframe = Frame(self.q, width=1024, height=600, bg="#FF0000")

        # Get the welcome message
        json = LoadJson()
        quest = json.load(os.path.join(self.base_folder, '../../Datas/Story/initialQuest.json'))
        print(quest['welcome'])

        lwelcome = Label(questframe, text=quest['welcome'], fg='dark grey')
        lwelcomefont = ('Calirbi (Body)', 24, 'bold')
        lwelcome.config(font=lwelcomefont)
        lwelcome.place(x=200, y=200)

        questframe.place(x=0, y=0)
        questframe.lower()

    def CombatFrame(self):
        hero = '{"name":"test","hp":20,"attaque":"2d10+0","vit":"5"}'
        monstre = '{"name": "chauve souris","hp": "30","attaque": "1d5+0","vit":"7"}'
        Combatframe = Frame(self.q, width=1024, height=600)
        Combatframe.place(x=0, y=0)
        Combatframe.lower()

        image_path = os.path.join(self.base_folder, '../medias/combat.png')
        bg = PhotoImage(file=r'' + image_path)
        canvas1 = Canvas(Combatframe, width=1024, height=600)
        canvas1.pack(fill="both", expand=True)
        canvas1.create_image(0, 0, image=bg, anchor="nw")
        canvas1.image = bg
        combat = Combat(hero, monstre)
        combat.initiative()

        def Attack():
            combat.monster_get_damaged()
            combat.monster_is_dead()
            if combat.monster_is_dead() == 0:
                print("monster is dead")
                Combatframe.destroy()
            else:
                combat.hero_get_damaged()
                if combat.hero_is_dead() == 0:
                    print("hero is dead")
                    Combatframe.destroy()

        def Inventaire():
            print("ceci est une ouverture d'inventaire")

        def Fuite():
            print("Vous tentez de prendre la fuite")

        AttackButton = Button(Combatframe, text="Attack", command=Attack, border=0, activebackground='#12c4c0',
                              bg="#12c4c0")
        AttackButton.place(x=750, y=500)

        InventaireButton = Button(Combatframe, text="Inventaire", command=Inventaire, border=0, activebackground='#12c4c0',
                              bg="#12c4c0")
        InventaireButton.place(x=850, y=500)

        FuiteButton = Button(Combatframe, text="Fuite", command=Fuite, border=0, activebackground='#12c4c0',
                              bg="#12c4c0")
        FuiteButton.place(x=850, y=550)