from tkinter import *
import os


class News:
    def __init__(self, infos):
        self.infos = infos

    def render(self, frame, x, y):
        imagePath = os.path.join(
            os.path.dirname(__file__), f'../medias/news/{self.infos["picture"]}')
        image = PhotoImage(file=imagePath)
        canvas = Canvas(frame, width=256, height=144)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(
            0, 0, image=image, anchor="nw")
        canvas.image = image
        canvas.place(x=x, y=y)

        # newsTitle = Label(frame, text=self.infos['title'], fg='white',
        #                   bg='#0483d1', )
        # # newsTitle.config()
        # newsTitle.place(x=x+2, y=y+2)

        # newsDate = Label(frame, text=self.infos['date'], fg='white',
        #                  bg='#0483d1', )
        # newsDate.place(x=x+2, y=y+30)
        canvas.create_text(
            128, 50, text=self.infos["title"] + "\n" + self.infos["date"], fill="white", justify="center")

        news_Button = Button(canvas, text="En savoir plus",
                             border=0,
                             activebackground='#12c4c0',
                             bg="#12c4c0")
        news_Button.place(relx=0.5, rely=0.6, anchor="center")
