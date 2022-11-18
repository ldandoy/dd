from operator import index
from tkinter import Canvas, Frame, Button, Label, StringVar
from Inventory.Consumable import Consumable
from Perso.person import Person


class Inventory:

    def __init__(self, perso, q):
        self.w = q.winfo_screenwidth()
        self.h = q.winfo_screenheight()
        self.q = q
        self.perso = perso
        self.items = []
        self.inventoryTitle = "Inventaire"
        self.inventoryFrame = Frame(self.q, width=self.w, height=self.h)
        self.formatInventory(perso, self.items)

    def addItem(self, itemsToAdd):
        for item in itemsToAdd:
            if item['type'] == 'consumable':
                itemToUpdate = self.findItemByName(
                    itemsToAdd, self.perso["inventaire"])
                if len(itemToUpdate) == 1:
                    self.incrementConsumableQuantity(
                        itemToUpdate, self.perso["inventaire"])
                    print(itemToUpdate)
                else:
                    self.perso["inventaire"].append(item)
            if item['type'] == 'weapon':
                self.perso["inventaire"].append(item)
        print(self.perso["inventaire"])
        Person.update(self.perso)

    def findItemByName(self, itemsToAdd, inventory):
        for item in itemsToAdd:
            print(list(filter(lambda i: item['name'] == i['name'], inventory)))

    def incrementConsumableQuantity(self, itemToUpdate, item):
        print('Update consumable quantity')
        itemToUpdate[0]['qty'] += item['qty']

    def formatInventory(self, perso, items):
        for item in perso["inventaire"]:
            items.append(Consumable(item))
        return items

    def removeItem(self,# TODO: create Weapon and Consumable class
 i):
        self.items.pop(i)

    def updateInventory(self):
        Person.update(self.perso)

    def selectItem(self, item):
        print("select item")

    def deleteItem(self, item):
        items = self.perso["inventaire"]
        updatedList = list(filter(lambda i: i['name'] != item.name, items))
        self.perso["inventaire"] = updatedList
        Person.update(self.perso)
        self.closeInventory()
        # TODO: create reloadFrame function
        # self.renderInventory(self.formatInventory(self.perso, []))

    def closeInventory(self):
        print('close')
        self.inventoryFrame.pack_forget()
        self.inventoryFrame.destroy()

    def renderInventory(self, items):
        self.inventoryFrame.place(x=0, y=0)

        backButton = Button(self.inventoryFrame, text="Retour", command=self.closeInventory, border=0,
                            activebackground='#12c4c0', bg="#12c4c0")
        backButton.place(x=750, y=350)

        canvas = Canvas(self.inventoryFrame, width=500, height=500)

        canvas.place(x=750, y=200)

        for index, item in enumerate(items):
            selectButton = Button(canvas, text="Select item", command=lambda item=item: self.selectItem(item), border=0,
                                  activebackground='#12c4c0', bg="#12c4c0")
            selectButton.grid(column=0, row=index)
            stringVarLabelName = StringVar(canvas)
            stringVarLabelName.set(item.name)
            stringVarLabelQty = StringVar(canvas)
            stringVarLabelQty.set(item.qty)
            labelName = Label(canvas, textvariable=stringVarLabelName)
            labelQty = Label(canvas, textvariable=stringVarLabelQty)
            labelName.grid(column=1, row=index)
            labelQty.grid(column=2, row=index)
            deleteButton = Button(canvas, text="Delete item", command=lambda item=item: self.deleteItem(item), border=0,
                                  activebackground='#12c4c0', bg="#12c4c0")
            deleteButton.grid(column=3, row=index)

        addButton = Button(canvas, text="Add Item", command=lambda items=[{
            "name": "mega-potion",
            "qty_max": 30,
            "qty": 1,
            "type": "consumable",
            "heal": 200
        },
            {
            "type": "weapon",
            "name": "Epee en or",
            "degat": "1d10",
            "test": "force"
        }]: self.addItem(items), border=0,
            activebackground='#12c4c0', bg="#12c4c0")
        addButton.grid(column=3, row=index+1)
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
