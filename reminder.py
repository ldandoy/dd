from tkinter import Canvas, Frame, Button, Label, StringVar
import os
from Inventory.Consumable import Consumable
from Inventory.Weapon import Weapon
from Inventory.Item import Item
from Perso.person import Person
from Utils.resized_image import ResizedImage


class Inventory:

    def __init__(self, perso, q):
        self.base_folder = os.path.dirname(__file__)
        self.w = q.winfo_screenwidth()
        self.h = q.winfo_screenheight()
        self.q = q
        self.perso = perso
        self.items = []
        self.inventoryTitle = "Inventaire"
        self.inventoryFrame = Frame(
            self.q, width=self.w, height=self.h, background="red")
        self.initInventory(perso, self.items)

    def addItem(self, itemsToAdd):
        for item in itemsToAdd:
            if item['type'] == 'consumable':
                itemToUpdate = self.findItemByName(
                    itemsToAdd, self.perso["inventaire"])
                if itemToUpdate:
                    self.incrementConsumableQuantity(
                        itemToUpdate, self.perso["inventaire"])
                else:
                    self.perso["inventaire"].append(item)
            if item['type'] == 'weapon':
                self.perso["inventaire"].append(item)
        print(self.perso["inventaire"])
        Person.update(self.perso)
        self.closeInventory()
        self.items = []
        self.initInventory(self.perso, self.items)

    def findItemByName(self, itemsToAdd, inventory):
        for item in itemsToAdd:
            print(list(filter(lambda i: item['name'] == i['name'], inventory)))

    def incrementConsumableQuantity(self, itemToUpdate, item):
        print('Update consumable quantity')
        itemToUpdate[0]['qty'] += item['qty']

    def initInventory(self, perso, items):
        for item in perso["inventaire"]:
            if item["type"] == "consumable":
                consumable = Consumable(item)
                items.append(consumable)
            if item["type"] == "weapon":
                weapon = Weapon(item)
                items.append(weapon)
            if item["type"] != "weapon" and item["type"] != "consumable":
                itm = Item(item)
                items.append(itm)

    def updateInventory(self):
        Person.update(self.perso)

    def selectItem(self, item):
        print(item)

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

        resized_image = ResizedImage.resize(self, '../medias/entrance.png')
        canvas = Canvas(self.inventoryFrame, width=self.w, height=self.h)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=resized_image, anchor="nw")
        canvas.image = resized_image

        backButton = Button(canvas, text="Retour", command=self.closeInventory, border=0,
                            activebackground='#12c4c0', bg="#12c4c0")
        backButton.place(x=self.w * 0.5, y=self.h * 0.9, anchor="center")


        for index, item in enumerate(items):
            if item.type == "consumable":
                selectButton = Button(canvas, text="Select item", command=lambda item=item: self.selectItem(item), border=0,
                                      activebackground='#12c4c0', bg="#12c4c0")
                selectButton.place(x=self.w * 0.2, y=self.h * 0.1 * index, anchor="center")
                stringVarLabelName = StringVar(canvas)
                stringVarLabelName.set(item.name)
                stringVarLabelQty = StringVar(canvas)
                stringVarLabelQty.set(item.qty)
                labelName = Label(canvas, textvariable=stringVarLabelName)
                labelQty = Label(canvas, textvariable=stringVarLabelQty)
                labelName.place(x=self.w * 0.4, y=self.h * 0.1 * index, anchor="center")
                labelQty.place(x=self.w * 0.7, y=self.h * 0.1 * index, anchor="center")
                deleteButton = Button(canvas, text="Delete item", command=lambda item=item: self.deleteItem(item), border=0,
                                      activebackground='#12c4c0', bg="#12c4c0")
                deleteButton.place(x=self.w * 0.8, y=self.h * 0.1 * index, anchor="center")
            else:
                selectWeapon = Button(canvas, text="Select weapon", command=lambda item=item: self.selectItem(item), border=0,
                                      activebackground='#12c4c0', bg="#12c4c0")
                selectWeapon.place(x=self.w * 0.3, y=self.h * 0.1 * index, anchor="center")
                stringVarWeaponName = StringVar(canvas)
                stringVarWeaponName.set(item.name)
                waponLabelName = Label(
                    canvas, textvariable=stringVarWeaponName)
                waponLabelName.place(x=self.w * 0.5, y=self.h * 0.1* index, anchor="center")
                deleteButton = Button(canvas, text="Delete item", command=lambda item=item: self.deleteItem(item), border=0,
                                      activebackground='#12c4c0', bg="#12c4c0")
                deleteButton.place(x=self.w * 0.8, y=self.h * 0.1* index , anchor="center")

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
        addButton.place(x=self.w * 0.5, y=self.h * 0.9, anchor="center")
        
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
