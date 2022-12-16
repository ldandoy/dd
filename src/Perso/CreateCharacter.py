
from functools import partial
from tkinter import *
from xmlrpc.client import Boolean


class CreateCharacter():
    raceList = ["human", "orc", "elfe", "troll"]
    classList = ["paladin", "warrior", "mage", "thief"]
    keysString = {
        "name": "Name",
        "eyes": "Eyes Color",
        "skin": "Skin Color",
        # "class_entry": "Classe",
        # "alignment": "Alignement",
    }
    keysInt = {
        "age": "Age",
        "height": "Height",
        "weight": "Weight",
    }

    def __init__(self, frame):
        self.frame = frame
        self.race: str = self.raceList[0]
        self.name: str = "fares"
        self.eyes: str = "black"
        self.skin: str = "black"
        self.class_entry: str = self.classList[0]
        self.alignment: int = 60
        self.age: int = 5
        self.height: int = 5
        self.weight: int = 5
        
        self.errors = {}
        self.initErrors()

        colPaddingY = 50
        paddingWidth = 30

        # RACE
        self.frameRace = Frame(frame, bg="red", pady=colPaddingY)
        self.frameRace.grid_columnconfigure(index=0, weight=1)
        self.frameRace.pack(fill=Y, side=LEFT, ipadx=paddingWidth)
        self.renderRace()


        self.frameClass = Frame(frame, bg="blue", pady=colPaddingY)
        self.frameClass.grid_columnconfigure(index=0, weight=1)
        self.frameClass.pack(fill=Y, side=RIGHT, ipadx=paddingWidth)
        self.renderClass()

    def toString(self) -> str:
        return f"""
            name: {self.name}
            eyes: {self.eyes}
            skin: {self.skin}
            class_entry: {self.class_entry}
            alignment: {self.alignment}
            age: {self.age}
            height: {self.height}
            weight: {self.weight}
        """



    def renderRace(self) -> None:
        def setRace(race) -> None:
            self.race = race
            self.renderRace()

        index = 0
        for r in self.raceList:
            bgColor = "pink"
            if self.race == r:
                bgColor = "orange"
            self.frameRace.grid_rowconfigure(index=index, weight=1)
            buttonRace = Button(self.frameRace, text=r, bg=bgColor, command=partial(setRace, r))
            buttonRace.grid(column=0, row=index, sticky="nwse", pady=5)
            index += 1

    def renderClass(self) -> None:
        def setClassEntry(class_entry):
            self.class_entry = class_entry
            self.renderClass()

        index = 0
        for c in self.classList:
            bgColor = "pink"
            if self.class_entry == c:
                bgColor = "orange"
            self.frameClass.grid_rowconfigure(index=index, weight=1)
            buttonClass = Button(self.frameClass, text=c, bg=bgColor, command=partial(setClassEntry, c))
            buttonClass.grid(column=0, row=index, sticky="nwse", pady=5)
            index += 1

    def setValues(self, person) -> None:
        """
        Set values from form to person
        """
        for key in self.keysString:
            self.__dict__[key] = person[key].get()
        for key in self.keysInt:
            self.__dict__[key] = int(person[key].get())

    def initErrors(self) -> None:
        """
        Remove errors from form
        """
        for key in self.keysString:
            self.errors[key] = ""
        for key in self.keysInt:
            self.errors[key] = ""

    def validateForm(self, errorsTk: dict) -> bool:
        """
        Verify input before save
        Returns list contains errors message or empty list
        """
        self.initErrors()
        isError = False
        for key in self.keysString:
            if self.__dict__[key] == "":
                isError = True
                errorsTk[key].set(f"Le champ {self.keysString[key]} est vide")
                # self.errors[key] = f"Le champ {self.keysString[key]} est vide"
        for key in self.keysInt:
            if self.__dict__[key] == 0:
                isError = True
                errorsTk[key].set(f"Le champ {self.keysString[key]} est vide")
                # self.errors[key] = f"Le champ {self.keysInt[key]} doit etre supérieur à 0"
        return isError