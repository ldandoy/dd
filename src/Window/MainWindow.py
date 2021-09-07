from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import *
import time
import os


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

        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, '../medias/montagne.png')

        bg = PhotoImage(file=image_path)
        canvas1 = Canvas(self.q, width=1024, height=768)
        canvas1.pack(fill="both", expand=True)

        # Display image
        canvas1.create_image(0, 0, image=bg, anchor="nw")

        Button(self.q, command=self.toogle_win, text='open', border=0, activebackground='#262626', bg="#262626").place(x=5, y=10)

        TextWelcomeFrame = Frame(self.q, width=624, height=35, bg='#12c4c0')
        TextWelcomeFrame.place(x=100, y=100)

        l1 = Label(TextWelcomeFrame, text="Bienvenue dans Donjon et Dragon", fg='dark grey', bg=None)
        l = ('Calirbi (Body)', 24, 'bold')
        l1.config(font=l)
        l1.place(x=0, y=0)

        def play():
            TextWelcomeFrame.destroy()

            ChoicePersoFrame = Frame(self.q, width=624, height=35, bg='#12c4c0')
            ChoicePersoFrame.place(x=0, y=0)
            ChoicePersoFrame.lower()

        PlayButton = Button(self.q, text="Jouer", command=play, border=0, activebackground='#12c4c0', bg="#12c4c0").place(x=900, y=700)

        self.q.mainloop()

