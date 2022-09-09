from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess


def open_inventory_management():
    subprocess.Popen(['python3', 'inventory_manage.py'])

def inventoryFrame(self, master):
    self.master = master
    self.master.title("Inventory Management")
    self.button = Button(self.frame, text = 'Gestion de l\'inventaire', command = open_inventory_management)
    self.button.pack()
    self.frame.pack()

def main():
    root = Tk()
    root.title('Inventory Management')
    root.geometry('400x400')
    inventoryFrame(root)
    root.mainloop()

if __name__ == '__main__':
    root = Tk()
    main_window = main_window(root)
    root.mainloop()