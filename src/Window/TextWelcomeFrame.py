from tkinter import Frame, Label, PhotoImage, Canvas, Button
import os

try:
    from Window.NewsFrame import lastNews
except ImportError:
    print("Error")


def textWelcomeFrame(q):
    textwelcomeframe = Frame(q, width=1024, height=600)
    textwelcomeframe.place(x=0, y=0)
    textwelcomeframe.lower()

    image_path = os.path.join(os.path.dirname(__file__), '../medias/montagne.png')
    bg = PhotoImage(file=r'' + image_path)
    canvas1 = Canvas(textwelcomeframe, width=1024, height=600)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bg, anchor="nw")
    canvas1.image = bg

    label_textwelcomeframe = Label(textwelcomeframe, text="Bienvenue dans Donjon et Dragon", fg='dark grey',
                                   bg=None)
    label_textwelcomeframe_config = ('Calirbi (Body)', 36, 'bold')
    label_textwelcomeframe.config(font=label_textwelcomeframe_config)
    label_textwelcomeframe.place(x=250, y=100)

    lastNews(q, textwelcomeframe)

    def play():
        textwelcomeframe.pack_forget()
        textwelcomeframe.destroy()

        # choicePersoFrame()

    PlayButton = Button(textwelcomeframe, text="Jouer", command=play, border=0, activebackground='#12c4c0',
                        bg="#12c4c0")
    PlayButton.place(x=950, y=550)