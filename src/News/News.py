import os
from tkinter import *

from PIL import Image, ImageTk


class News:
    newsSpacing = 70
    newsW = 256
    newsH = 144

    def __init__(self, infos, q):
        self.infos = infos
        self.q = q
        self.w = self.q.winfo_screenwidth()
        self.h = self.q.winfo_screenheight()

    def __str__(self) -> str:
        print("News :", self.infos["date"], self.infos["title"])

    def render(self, frame) -> Canvas:
        imagePath = os.path.join(
            os.path.dirname(__file__), f'../medias/news/{self.infos["picture"]}')
        image = Image.open(imagePath)
        image = image.resize((self.newsW, self.newsH), Image.ANTIALIAS)
        imageTk = ImageTk.PhotoImage(image)

        canvas = Canvas(frame, width=self.newsW, height=self.newsH, bd=0,
                        highlightthickness=1,highlightbackground="white",bg="white", relief='ridge')
        canvas.create_image(0, 0, image=imageTk, anchor="nw")
        canvas.image = imageTk

        canvas.create_text(
            128, 50, text=self.infos["title"] + "\n" + self.infos["date"], fill="white", justify="center", font=("Arial", 18))

        newsButton = Button(canvas, text="En savoir plus",
                            border=0,
                            activebackground='#12c4c0',
                            bg="#12c4c0", command=self.renderNewsDetailsPage)
        newsButton.place(relx=0.5, rely=0.7, anchor="center")

        return canvas

    def renderNewsDetailsPage(self):
        NewsDetailsFrame = Frame(self.q, width=self.w, height=self.h)

        imagePath = os.path.join(
            os.path.dirname(__file__), f'../medias/news/{self.infos["picture"]}')
        image = Image.open(imagePath)
        image = image.resize((self.w, self.h), Image.ANTIALIAS)
        imageTk = ImageTk.PhotoImage(image)

        canvas = Canvas(NewsDetailsFrame, width=self.w, height=self.h)
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

        returnButton = Button(canvas, text="Retour",
                              border=0,
                              activebackground='#12c4c0',
                              bg="#12c4c0", command=lambda frame=NewsDetailsFrame: News.closeFrame(frame))
        returnButton.place(relx=0.5, rely=0.8, anchor="center")

        NewsDetailsFrame.place(x=0, y=0)

    @staticmethod
    def closeFrame(frame):
        frame.pack_forget()
        frame.destroy()


class NewsList:
    newsList = []
    title: str = "News List"

    def __init__(self, newslist, q):
        self.q = q
        self.w = self.q.winfo_screenwidth()
        self.h = self.q.winfo_screenheight()
        for newsInfos in newslist:
            self.newsList.append(News(newsInfos, q))

    def __str__(self) -> str:
        print("NewsList :")
        for news in self.newsList:
            news.__str__()

    def renderNewsListPage(self):
        newsListFrame = Frame(self.q, bg="black")

        titleLabel = Label(newsListFrame, text=self.title,
                           bg="black", fg="white", font=("Arial", 24))
        titleLabel.pack(side=TOP, ipady=20)

        scrollbar = Scrollbar(newsListFrame)

        newsGridCanvas = Canvas(
            newsListFrame, bg="black", yscrollcommand=scrollbar.set)

        scrollbar.config(command=newsGridCanvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        newsGridFrame = Frame(newsGridCanvas, bg="black")
        newsGridFrame.grid_columnconfigure(tuple(range(5)), weight=1)

        newsGridCanvas.pack(fill=BOTH, expand=True)
        newsGridCanvas.create_window(0, 0, window=newsGridFrame, anchor="nw", width=self.w)

        for i, news in enumerate(self.newsList):
            newsCard = news.render(newsGridFrame)
            newsCard.grid(column=i % 5, row=i // 5, pady="20")

        self.q.update()
        newsGridCanvas.config(scrollregion=newsGridCanvas.bbox("all"))
        newsListFrame.pack()

        returnButton = Button(newsListFrame, text="Retour",
                              border=0,
                              activebackground='#12c4c0',
                              bg="#12c4c0", command=lambda frame=newsListFrame: News.closeFrame(frame))
        returnButton.pack(side=BOTTOM, ipady=10, pady=20)

        newsListFrame.pack(fill="both", expand=True)
