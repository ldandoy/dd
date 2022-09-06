from tkinter import *
import os

import inventory_frame as im 

#create a window who's using the tkinter module for the GUI of inventory
class InventoryWindow:
    def __init__(self):
        self.base_folder = os.path.dirname(__file__)
        self.q = Tk()
        self.q.title("Donjon & Dragon")
        self.q.geometry('1024x600')
        self.q.configure(bg='')
        self.inventoryFrame = im.InventoryManage(self.q)
        self.q.mainloop()
        
if __name__ == '__main__':
    InventoryWindow()