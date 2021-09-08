from tkinter import *
import os
from Utils.loadJson import LoadJson


class MainWindow:

    def toogle_win(self):
        f1 = Frame(self.q, width=300, height=768, bg='#12c4c0')
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
        self.q = Tk()
        self.q.title("Donjon & Dragon")
        self.q.geometry('1024x768')
        self.q.configure(bg='')
        # Add no size update

        base_folder = os.path.dirname(__file__)
        self.image_path = os.path.join(base_folder, '../medias/montagne.png')
        self.image2_path = os.path.join(base_folder, '../medias/montagne.png')

        Button(self.q, command=self.toogle_win, text='Menu', border=0, bg="#12c4c0").place(x=5, y=10)

        TextWelcomeFrame = Frame(self.q, width=1024, height=768)
        TextWelcomeFrame.place(x=0, y=0)
        TextWelcomeFrame.lower()

        bg = PhotoImage(file=self.image_path)
        canvas1 = Canvas(TextWelcomeFrame, width=1024, height=768)
        canvas1.pack(fill="both", expand=True)

        # Display image
        canvas1.create_image(0, 0, image=bg, anchor="nw")

        l1 = Label(TextWelcomeFrame, text="Bienvenue dans Donjon et Dragon", fg='dark grey', bg=None)
        l = ('Calirbi (Body)', 24, 'bold')
        l1.config(font=l)
        l1.place(x=200, y=200)

        def play():
            TextWelcomeFrame.pack_forget()
            TextWelcomeFrame.destroy()

            ChoicePersoFrame = Frame(self.q, width=1024, height=768)


            bg2 = PhotoImage(file=self.image2_path)
            canvas2 = Canvas(ChoicePersoFrame, width=1024, height=768)
            canvas2.pack(fill="both", expand=True)

            # Display image
            canvas2.create_image(0, 0, image=bg2, anchor="nw")

            # Get the welcome message
            json = LoadJson()
            quest = json.load(os.path.join(base_folder, '../../Datas/Story/initialQuest.json'))
            print(quest['welcome'])

            lwelcome = Label(ChoicePersoFrame, text=quest['welcome'], fg='dark grey')
            lwelcomefont = ('Calirbi (Body)', 24, 'bold')
            lwelcome.config(font=lwelcomefont)
            lwelcome.place(x=200, y=200)

            ChoicePersoFrame.place(x=0, y=0)
            ChoicePersoFrame.lower()

        PlayButton = Button(TextWelcomeFrame, text="Jouer", command=play, border=0, activebackground='#12c4c0', bg="#12c4c0").place(x=900, y=700)

        self.q.mainloop()

