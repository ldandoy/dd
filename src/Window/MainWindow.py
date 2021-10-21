from tkinter import *
import os

from Utils.loadJson import LoadJson
from Rooms.rooms import Room
from Perso.PersoActions import submit_new_perso
from Combat.combat import *
from Utils.GetLastFeatures import GetLastFeatures
from functools import partial



class MainWindow:
    rooms = []
    
    donjonroom = 0

    def toogleWin(self):
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

        Button(self.q, command=self.toogleWin, text='Menu', border=0, bg="#12c4c0").place(x=5, y=10)

        self.textWelcomeFrame()

        self.q.mainloop()

    def textWelcomeFrame( self ):
        textwelcomeframe = Frame( self.q, width=1024, height=600 )
        textwelcomeframe.place( x=0, y=0 )
        textwelcomeframe.lower()

        image_path = os.path.join( self.base_folder, '../medias/montagne.png' )
        bg = PhotoImage( file=r'' + image_path )
        canvas1 = Canvas( textwelcomeframe, width=1024, height=600 )
        canvas1.pack( fill="both", expand=True )
        canvas1.create_image( 0, 0, image=bg, anchor="nw" )
        canvas1.image = bg

        label_textwelcomeframe = Label( textwelcomeframe, text="Bienvenue dans Donjon et Dragon", fg='dark grey',
                                        bg=None )
        label_textwelcomeframe_config = ('Calirbi (Body)', 36, 'bold')
        label_textwelcomeframe.config( font=label_textwelcomeframe_config )
        label_textwelcomeframe.place( x=250, y=100 )

        lastFeaturesObj = GetLastFeatures( 3 )

        label_textinfo_config = ('Calirbi (Body)', 24, 'bold')

        label_textinfo_x_position = 25
        label_showmore_y_position = 100

        def News_show_more_frame( self, feature ):
            news_show_more_frame = Frame( self.q, width=1024, height=600 )

            image2_path = os.path.join( self.base_folder, '../medias/newsBg/' + feature[ 'picture' ] )
            bg2 = PhotoImage( file=image2_path )
            canvas2 = Canvas( news_show_more_frame, width=1024, height=600 )
            canvas2.pack( fill="both", expand=True )
            canvas2.create_image( 0, 0, image=bg2, anchor="nw" )
            canvas2.image = bg2

            for i, info in enumerate( feature ):
                if(info != 'picture' ):
                    label_textinfo = Label( news_show_more_frame, text=feature[info], fg='white', bg='#0483d1' )
                    label_textinfo.config( font=label_textinfo_config )
                    label_textinfo.place( x=25, y= label_showmore_y_position + (i * 40))


            def choice():
                news_show_more_frame.pack_forget()
                news_show_more_frame.destroy()

                self.TextWelcomeFrame()

            ChoiceButton = Button( news_show_more_frame, text="retour", command=choice, border=0,
                                   activebackground='#12c4c0', bg="#12c4c0" )
            ChoiceButton.place( x=950, y=550 )

            news_show_more_frame.place( x=0, y=0 )
            news_show_more_frame.lower()

        def show_more( feature ):
            textwelcomeframe.pack_forget()
            textwelcomeframe.destroy()
            News_show_more_frame( self, feature )

        for i, feature in enumerate( lastFeaturesObj ):
            label_textinfo = Label( textwelcomeframe, text=feature[ 'title' ][ 0:50 ], fg='white',
                                    bg='#0483d1', )
            label_textinfo.config( font=label_textinfo_config )
            label_textinfo.place( x=label_textinfo_x_position + (i * 350), y=250 )
            news_Button = Button( textwelcomeframe, text="En savoir plus", command=partial( show_more, feature ),
                                  border=0,
                                  activebackground='#12c4c0',
                                  bg="#12c4c0" )
            news_Button.place( x=label_textinfo_x_position + (i * 350), y=300 )

        def play():
            textwelcomeframe.pack_forget()
            textwelcomeframe.destroy()

            self.choicePersoFrame()

        PlayButton = Button(textwelcomeframe, text="Jouer", command=play, border=0, activebackground='#12c4c0', bg="#12c4c0")
        PlayButton.place(x=950, y=550)

    def choicePersoFrame(self):
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

            self.questFrame()

        def go_to_new_perso() -> None:
            choicepersoframe.pack_forget()
            choicepersoframe.destroy()

            self.newPersoFrame()

        ChoiceButton = Button(choicepersoframe, text="Choisir", command=choice, border=0, activebackground='#12c4c0', bg="#12c4c0")
        new_button = Button(choicepersoframe, text="Créer un nouveau personnage", command=go_to_new_perso, border=0, activebackground='#12c4c0', bg="#12c4c0")
        ChoiceButton.place(x=950, y=550)
        new_button.place(x=775, y=550)

        choicepersoframe.place(x=0, y=0)
        choicepersoframe.lower()

    def questFrame(self):
        questframe = Frame(self.q, width=1024, height=600, bg="#FF0000")

        # Get the welcome message
        json = LoadJson()
        quest = json.load(os.path.join(self.base_folder, '../../Datas/Story/initialQuest.json'))

        def choice():
            questframe.pack_forget()
            questframe.destroy()
            self.rooms = Room()

            self.questStartedFrame()

        label_textquestframe = Label(questframe, text="Bienvenue 'INSERER NOM JOUEUR', que souhaitez-vous faire ?",
                                     fg='dark grey', bg=None)
        label_textquestframe_config = ('Calibri (Body)', 20, 'bold')
        label_textquestframe.config(font=label_textquestframe_config)
        label_textquestframe.place(x=100, y=200)

        questButton = Button(questframe, text="Démarrer une quête", command=choice, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
        questButton.place(x=490, y=300)

        questframe.place(x=0, y=0)
        questframe.lower()

    def questStartedFrame(self):

        queststartedframe = Frame(self.q, width=1024, height=600, bg="#FF0000")

        def fight():
            self.donjonroom += 1
            queststartedframe.pack_forget()
            queststartedframe.destroy()
            self.combatFrame()
        def bossfight():
            queststartedframe.pack_forget()
            queststartedframe.destroy()
            self.combatFrame()
        def runaway():
            queststartedframe.pack_forget()
            queststartedframe.destroy()
            self.QuestFrame()
        def exitroom():
            queststartedframe.pack_forget()
            queststartedframe.destroy()
            self.QuestFrame()
        def nextroom():
            self.donjonroom += 1
            queststartedframe.pack_forget()
            queststartedframe.destroy()
            self.questStartedFrame()

        tqueststarted = Label(queststartedframe, text=self.rooms.donjon[self.donjonroom]["name"], fg='dark grey')
        tqueststartedfont = ('Calibri (Body)', 24, 'bold')
        tqueststarted.config(font=tqueststartedfont)
        tqueststarted.place(x=50, y=70)

        lqueststarted = Label(queststartedframe, text=self.rooms.donjon[self.donjonroom]["description"], fg='dark grey')
        lqueststartedfont = ('Calibri (Body)', 18, 'bold')
        lqueststarted.config(font=lqueststartedfont)
        lqueststarted.place(x=50, y=120)

        if self.rooms.donjon[self.donjonroom]["name"] == "Rencontre":
            fightButton = Button(queststartedframe, text="Combattre !", command=fight, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
            fightButton.place(x=750, y=200)

            runButton = Button(queststartedframe, text="Fuir !", command=runaway, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
            runButton.place(x=750, y=250)
        elif self.rooms.donjon[self.donjonroom]["name"] == "Boss":
            fightButton = Button(queststartedframe, text="Combattre !", command=bossfight, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
            fightButton.place(x=750, y=200)

            runButton = Button(queststartedframe, text="Fuir !", command=runaway, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
            runButton.place(x=750, y=250)
        else:
            continueButton = Button(queststartedframe, text="Continuer", command=nextroom, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
            continueButton.place(x=750, y=200)

            exitButton = Button(queststartedframe, text="Sortir", command=exitroom, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
            exitButton.place(x=750, y=250)

        queststartedframe.place(x=0, y=0)
        queststartedframe.lower()

    def newPersoFrame(self):
        frame = Frame(self.q, width=1024, height=600, bg="#FFF")

        # main message
        main_message = Label(frame, text='Créer un personnage', fg='dark grey')
        main_message.config(font=('Calibri (Body)', 24, 'bold'))
        main_message.place(x=200, y=200)

        # new perso form
        Label(frame, text="Name").grid(row=0, column=0)
        Label(frame, text="Age").grid(row=1, column=0)
        name = Entry(frame).grid(row=0, column=1)
        age = Entry(frame).grid(row=1, column=1)

        def makeform(root, fields):
            entries = {}
            for field in fields:
                row = Frame(root)
                lab = Label(row, width=22, text=field + ": ", anchor='w')
                ent = Entry(row)
                ent.insert(0, "0")
                row.pack(side=TOP, fill=X, padx=5, pady=5)
                lab.pack(side=LEFT)
                ent.pack(side=RIGHT, expand=YES, fill=X)
                entries[field] = ent
            return entries

        fields = ('Name', 'Age')
        ents = makeform(self.q, fields)
        print(name)

        def trigger_submit_new_form():
            submit_new_perso(ents.get('Name'))

        btn = Button(frame, text="Submit", command=submit_new_perso).grid(row=4, column=0)

        frame.place(x=0, y=0)
        frame.lower()

    def combatFrame(self):
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