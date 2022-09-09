from tkinter import *
from PIL import ImageTk, Image
import os

from Utils.load_json import LoadJson


class News:
    def __init__(self, infos):
        self.infos = infos

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
                             bg="#12c4c0")
        news_Button.place(relx=0.5, rely=0.7, anchor="center")

    @staticmethod
    def getAllNews(baseFolder):
        newsList = []
        json = LoadJson()
        filePath = os.path.join(baseFolder, '../../Datas/News/news.json')
        newsJson = json.load(filePath)
        for news in newsJson:
            newsList.append(News(news))
        return newsList
