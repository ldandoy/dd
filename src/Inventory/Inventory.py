from operator import index
from tkinter import Canvas, Frame, Button, Label, StringVar
from Inventory.Item import Item
from Perso.person import Person


class Inventory:

    def __init__(self, perso, q):
        self.w = q.winfo_screenwidth()
        self.h = q.winfo_screenheight()
        self.q = q
        self.perso = perso
        self.items = []
        self.inventoryTitle = "Inventaire"
        for item in perso["inventaire"]:
            self.items.append(Item(item))

    def add_item(self, item):
        self.items.append(Item(item))

    def remove_item(self, i):
        self.items.pop(i)

    def updateInventory(self):
        Person.update(self.perso)

    def selectItem(self, item):
        print("select item")

    def deleteItem(self, item):
        print(item.name)
        # items = self.perso["inventaire"]
        # updatedList = list(filter(lambda i: i['name'] != item.name, items))
    
    def renderInventory(self):
        inventoryFrame = Frame(self.q, width=self.w, height=self.h)
        inventoryFrame.place(x=0, y=0)

        def closeInventory():
            inventoryFrame.pack_forget()
            inventoryFrame.destroy()

        backButton = Button(inventoryFrame, text="Retour", command=closeInventory, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
        backButton.place(x=750, y=350)

        canvas = Canvas(inventoryFrame, width=500, height=500)

        canvas.place(x=750, y=200)

        for index, item in enumerate(self.items):
            selectButton = Button(canvas, text="Select item", command=lambda item=item: self.selectItem(item), border=0,
                                activebackground='#12c4c0', bg="#12c4c0")
            selectButton.grid(column=0, row=index)
            stringVarLabelName = StringVar(canvas)
            stringVarLabelName.set(item.name)
            stringVarLabelAmount = StringVar(canvas)
            stringVarLabelAmount.set(item.amount)
            labelName = Label(canvas, textvariable=stringVarLabelName)
            labelAmount = Label(canvas, textvariable=stringVarLabelAmount)
            labelName.grid(column=1, row=index)
            labelAmount.grid(column=2, row=index)
            deleteButton = Button(canvas, text="Delete item", command=lambda item=item: self.deleteItem(item), border=0,
                                activebackground='#12c4c0', bg="#12c4c0")
            deleteButton.grid(column=3, row=index)
           

        # imagePath = os.path.join(
        #     os.path.dirname(__file__), f'../medias/news/{self.infos["picture"]}')
        # image = Image.open(imagePath)
        # image = image.resize((self.w, self.h), Image.ANTIALIAS)
        # imageTk = ImageTk.PhotoImage(image)

       
        # canvas.create_image(0, 0, image=imageTk, anchor="nw")
        # canvas.image = imageTk
        # canvas.place(x=0, y=0)

        # canvas.create_text(
        #     self.w/2, 150, text=self.inventoryTitle, fill="white", justify="center", font=("Arial", 24))

        # returnButton = Button(canvas, text="Retour",
        #                      border=0,
        #                      activebackground='#12c4c0',
        #                      bg="#12c4c0", command=lambda frame=inventoryFrame:self.closeFrame(frame))
        # returnButton.place(relx=0.5, rely=0.8, anchor="center")

