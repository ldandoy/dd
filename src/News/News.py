import os
from tkinter import *

from PIL import Image, ImageTk


class News:
    def __init__(self, infos, q):
        self.infos = infos
        self.q = q
        self.w = self.q.winfo_screenwidth()
        self.h = self.q.winfo_screenheight()

    def render(self, frame, x, y):
        imagePath = os.path.join(
            os.path.dirname(__file__), f'../medias/news/{self.infos["picture"]}')
        image = Image.open(imagePath)
        image = image.resize((256, 144), Image.ANTIALIAS)
        imageTk = ImageTk.PhotoImage(image)

        canvas = Canvas(frame, width=256, height=144, bd=0,
                        highlightthickness=0, relief='ridge')
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=imageTk, anchor="nw")
        canvas.image = imageTk
        canvas.place(x=x, y=y)

        canvas.create_text(
            128, 50, text=self.infos["title"] + "\n" + self.infos["date"], fill="white", justify="center", font=("Arial", 18))

        news_Button = Button(canvas, text="En savoir plus",
                             border=0,
                             activebackground='#12c4c0',
                             bg="#12c4c0", command=self.renderShowMoreNewsScreen)
        news_Button.place(relx=0.5, rely=0.7, anchor="center")

    def renderShowMoreNewsScreen(self):
        showMoreNewsFrame = Frame(self.q, width=self.w, height=self.h)

        imagePath = os.path.join(
            os.path.dirname(__file__), f'../medias/news/{self.infos["picture"]}')
        image = Image.open(imagePath)
        image = image.resize((self.w, self.h), Image.ANTIALIAS)
        imageTk = ImageTk.PhotoImage(image)

        canvas = Canvas(showMoreNewsFrame, width=self.w, height=self.h)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=imageTk, anchor="nw")
        canvas.image = imageTk
        canvas.place(x=0, y=0)

        canvas.create_text(
            self.w/2, 150, text=self.infos["title"], fill="white", justify="center", font=("Arial", 24))
        canvas.create_text(
            self.w/2, 200, text=self.infos["date"], fill="white", justify="center", font=("Arial", 18))
        canvas.create_text(
            self.w/2, 250, text=self.infos["content"], fill="white", justify="center", font=("Arial", 12))
        canvas.create_text(
            self.w/2, 400, text=self.infos["author"], fill="white", justify="center", font=("Arial", 14))

        news_Button = Button(canvas, text="Retour",
                             border=0,
                             activebackground='#12c4c0',
                             bg="#12c4c0", command=lambda frame=showMoreNewsFrame:self.closeFrame(frame))
        news_Button.place(relx=0.5, rely=0.8, anchor="center")

        showMoreNewsFrame.place(x=0, y=0)
    
    def closeFrame(self, frame):
        frame.pack_forget()
        frame.destroy()
