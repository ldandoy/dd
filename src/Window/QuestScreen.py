import os
from random import *
from tkinter import *
from PIL import Image, ImageTk
from Rooms.rooms import Room
from Utils.load_json import LoadJson
from Utils.Sound import Sound
from Window.quest import start_quest_frame
from Inventory import Inventory


def renderReward(self, frame, item, x, y, Playsound):


    questContainerWidth = self.w /4
    questContainerHeight = self.h/1.5

    def onMouseEnter(event):
        frame.itemconfigure(ItemName, text=item["NameItem"])
        frame.itemconfigure(descriptionItem, text=item["DescriptionItem"])
        Playsound('button_menu')

    def onMouseExit(event):
        frame.itemconfigure(ItemName, text="")
        frame.itemconfigure(descriptionItem, text="")

    rewardImageDimension = int(questContainerWidth / 5)

    imageItem = (Image.open(os.path.join(self.base_folder,
                 '../medias/'+item["ImageItem"]+'.png')))
    resizedImage = imageItem.resize((rewardImageDimension, rewardImageDimension), Image.ANTIALIAS)
    imageItemResized = ImageTk.PhotoImage(resizedImage)
    itemContainer = Canvas(frame, width=rewardImageDimension, height=rewardImageDimension,
                           bd=1, highlightthickness=0, bg="green")
    itemContainer.pack()
    itemContainer.create_image(0, 0, anchor="nw", image=imageItemResized)
    itemContainer.image = imageItemResized
    itemContainer.place(x=x, y=y)
    itemContainer.bind('<Enter>', onMouseEnter)
    itemContainer.bind('<Leave>', onMouseExit)
    itemNameFont = ('Calibri (Body)', 16, 'bold', 'italic', 'underline')
    itemDescriptionFontF = ('Calibri (Body)', 14, 'bold', 'italic')
    ItemName = frame.create_text(
        questContainerWidth / 2, questContainerHeight /1.7, text="", fill="white", justify="center", font=itemNameFont)
    descriptionItem = frame.create_text(
        questContainerWidth / 2, questContainerHeight /1.5, text="", fill="white", justify="center", font=itemDescriptionFontF)


def renderQuest(self, frame, Playsound, quest, x, y, choice):

    def onMouseEnter(event):
        Playsound('selection')
        questContainer["bg"] = "white"

    def onMouseExit(event):
        questContainer["bg"] = "black"


    questContainerWidth = self.w /4
    questContainerHeight = self.h/1.5



    img = (Image.open(os.path.join(self.base_folder,
           '../medias/'+quest["Image"]+'.png')))
    resizedImage = img.resize((512, 700), Image.ANTIALIAS)
    newImage = ImageTk.PhotoImage(resizedImage)
    questContainer = Canvas(frame, width=questContainerWidth, height=questContainerHeight,
                            bd=2, highlightthickness=0)
    questContainer.pack(fill="both", expand=True)
    questContainer.create_image(0, 0, image=newImage, anchor="nw")
    questContainer.image = newImage
    questContainer.place(x=x, y=y)
    questContainer.bind('<Enter>', onMouseEnter)
    questContainer.bind('<Leave>', onMouseExit)

    questLabelFont = ('Calibri (Body)', 24, 'bold', 'italic', 'underline')
    difficultyFont = ('Calibri (Body)', 16, 'bold', 'italic')
    descriptionFont = ('Calibri (Body)', 20, 'bold')
    rewardLabelFont = ('Calibri (Body)', 18, 'bold', 'italic')

    questContainer.create_text(
        (questContainerWidth) / 2, questContainerHeight /15, text=quest["Name"], fill="white", justify="center", font=questLabelFont)
    questContainer.create_text((questContainerWidth) / 2, questContainerHeight / 3, text="Description :" + "\n" +
                               quest["Description"], fill="white", justify="center", font=descriptionFont)
    questContainer.create_text((questContainerWidth) / 2, questContainerHeight / 6, text="Difficulty :" +
                               quest["Difficulty"], fill="white", justify="center", font=difficultyFont)
    questContainer.create_text((questContainerWidth) / 2, questContainerHeight / 2, text='Rewards Available',
                               fill="white", justify="center", font=rewardLabelFont)

    for i, reward in enumerate(quest["Rewards"]):
        renderReward(self, questContainer, reward,
        (self.w / 24) + self.w/ 10 * i , self.h/2.1, Playsound)

    startButton = Button(questContainer, text="Commencer", command=choice,
                         border=0, activebackground='#12c4c0', bg="#12c4c0")
    startButton.place(relx=0.5, rely=0.9, anchor="center")

def Quest(self):

    json = LoadJson()
    questJson = json.load(os.path.join(
        self.base_folder, '../../Datas/Story/quest.json'))

    w = self.q.winfo_screenwidth()
    h = self.q.winfo_screenheight()

    def Playsound(nameSound):
        Sound.play(self.base_folder, nameSound + ".wav")

    def choice():
        questFrame.pack_forget()
        questFrame.destroy()
        self.rooms = Room()
        start_quest_frame(self)

    questFrame = Frame(self.q, width=w, height=h)
    backgroundImagePath = os.path.join(self.base_folder, '../medias/city4.png')
    bgImage = PhotoImage(file=r'' + backgroundImagePath, width=w, height=h)
    mainCanvas = Canvas(questFrame, width=w, height=h,
                        bd=0, highlightthickness=0)
    mainCanvas.pack(fill="both", expand=TRUE)
    mainCanvas.create_image(0, 0, image=bgImage, anchor="nw")
    mainCanvas.image = bgImage
    labelTextcityFrame_config = ('Calibri (Body)', 30, 'bold')
    mainCanvas.create_text(w/2, h/10, fill='white', anchor='c', text="Bienvenue à Erthilia " + self.perso.get(
        'name') + ",\n Quel destin veux-tu choisir ?", font=labelTextcityFrame_config, justify='center')
    questFrame.pack(expand=TRUE)

    for i, quest in enumerate(questJson):
        renderQuest(self, questFrame, Playsound,
                    quest, w/20+ w/3 * i, h/5, choice)
    