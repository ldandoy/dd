from tkinter import *
import sqlite3

class InventoryManage:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.frame.pack()

        self.inventory_label = Label(self.frame, text="Inventaire")
        self.inventory_label.pack()

        self.inventory_listbox = Listbox(self.frame, width=50, height=20)
        self.inventory_listbox.pack()

        self.inventory_scrollbar = Scrollbar(self.frame, orient=VERTICAL)
        self.inventory_scrollbar.config(command=self.inventory_listbox.yview)
        self.inventory_scrollbar.pack(side=RIGHT, fill=Y)

        self.use_item_button = Button(
            self.frame, text="Utiliser", command=self.use_item)
        self.use_item_button.pack()

        self.drop_item_button = Button(
            self.frame, text="Jeter l'objet", command=self.drop_item)
        self.drop_item_button.pack()

        self.equip_item_button = Button(self.frame, text="Equiper", command=self.equip_item)
        self.equip_item_button.pack()


        self.unequip_item_button=Button(
            self.frame, text = "Enlever l'objet", command = self.unequip_item)
        self.unequip_item_button.pack()


        self.sell_item_button=Button(self.frame, text = "Vendre", command = self.sell_item)
        self.sell_item_button.pack()


        self.buy_item_button=Button(self.frame, text="Acheter", command=self.buy_item)
        self.buy_item_button.pack()


        self.exit_inventory_button=Button(self.frame, text="Quitter l'inventaire", command=self.exit_inventory)
        self.exit_inventory_button.pack()



    def stock_item(self):

        self.conn=sqlite3.connect('inventory.db')
        self.c=self.conn.cursor()
        self.c.execute("""CREATE TABLE inventory (
            name text,
            type text,
            quantity integer
        )""")

        self.conn.commit()
        self.conn.close()

    def add_item(self, name, type, quantity):

        self.conn=sqlite3.connect('inventory.db')
        self.c=self.conn.cursor()
        self.c.execute("INSERT INTO inventory VALUES (:name, :type, :quantity)", {
            'name': name,
            'type': type,
            'quantity': quantity
        })

        self.conn.commit()
        self.conn.close()

    def remove_item(self, name):

        self.conn=sqlite3.connect('inventory.db')
        self.c=self.conn.cursor()
        self.c.execute("DELETE from inventory WHERE name = :name", {
            'name': name
        })

        self.conn.commit()
        self.conn.close()

    def update_item(self, name, quantity):

        self.conn=sqlite3.connect('inventory.db')
        self.c=self.conn.cursor()
        self.c.execute("UPDATE inventory SET quantity = :quantity WHERE name = :name", {
            'name': name,
            'quantity': quantity
        })

        self.conn.commit()
        self.conn.close()

    def query_item(self):

        self.conn=sqlite3.connect('inventory.db')
        self.c=self.conn.cursor()
        self.c.execute("SELECT *, oid FROM inventory")
        self.records=self.c.fetchall()

        self.conn.commit()
        self.conn.close()


        print(self.records)


        for record in self.records:
            print(record)