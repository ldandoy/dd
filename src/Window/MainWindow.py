from tkinter import *
import os
from Utils.loadJson import LoadJson
from Utils.GetLastFeatures import GetLastFeatures

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

        lastFeaturesObj = GetLastFeatures( 3 )

        print( lastFeaturesObj[ 1 ][ 'content' ] )

        label_textinfo1 = Label(textwelcomeframe, text="Bienvenue dans Donjon\n et Dragoooooooonnnnnn", fg='dark grey', bg='cyan')
        label_textinfo1.config(font=label_textwelcomeframe_config)
        label_textinfo1.place(x=50, y=400)

        label_textinfo2 = Label(textwelcomeframe, text="Bienvenue dans Donjon\n et Dragoooooooonnnnnn", fg='dark grey',bg='cyan')
        label_textinfo2.config(font=label_textwelcomeframe_config)
        label_textinfo2.place(x=350, y=400)

        label_textinfo3 = Label(textwelcomeframe, text="Bienvenue dans Donjon\n et Dragoooooooonnnnnn", fg='dark grey',bg='cyan')
        label_textinfo3.config(font=label_textwelcomeframe_config)
        label_textinfo3.place(x=650, y=400)

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
