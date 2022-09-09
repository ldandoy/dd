from tkinter import Button, Frame, Label


class Inventory:
    __items = None

    def __init__(self, perso):
        self.__items = perso

    def useItem(self, name, amount, hp):
        if( name == 'potion'):
            if (hp + 5 > 20):
                hp = 20
                return hp
            else: return hp + 5
            

        elif( name == 'super-potion'):
            if (hp + 10 > 20):
                hp = 20
                return hp
            else: return hp + 10
            
        elif( name == 'mega-potion'):
            hp = 20
            return hp

    def add_item(self):
        print("add item")

    def remove_item(self):
        print("remove item")

    def edit_item(self):
        print("edit item")






    

