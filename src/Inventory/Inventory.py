from tkinter import Canvas, Frame, Button
from Inventory.Item import Item
from Perso.person import Person


class Inventory:
    items: list[Item]

    def __init__(self, perso, q):
        print('INVENTORY INSTANCE')
        self.w = q.winfo_screenwidth()
        self.h = q.winfo_screenheight()
        self.q = q
        self.inventoryTitle = "Inventaire"
        # for item in perso["inventaire"]:
        #     self.items.append(Item(item))

    def add_item(self, item):
        self.items.append(Item(item))

    def remove_item(self, i):
        self.items.pop(i)

    def updateInventory(self):
        Person.update(self.perso)

    def renderInventory(self):
        inventoryFrame = Frame(self.q, width=self.w, height=self.h)
        inventoryFrame.place(x=0, y=0)

        def close_inventory():
            inventoryFrame.pack_forget()
            inventoryFrame.destroy()

        backButton = Button(inventoryFrame, text="Retour", command=close_inventory, border=0,
                             activebackground='#12c4c0', bg="#12c4c0")
        backButton.place(x=750, y=200)


        # imagePath = os.path.join(
        #     os.path.dirname(__file__), f'../medias/news/{self.infos["picture"]}')
        # image = Image.open(imagePath)
        # image = image.resize((self.w, self.h), Image.ANTIALIAS)
        # imageTk = ImageTk.PhotoImage(image)

        # canvas = Canvas(inventoryFrame, width=self.w, height=self.h)
        # canvas.pack(fill="both", expand=True)
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

