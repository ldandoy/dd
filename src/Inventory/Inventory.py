from tkinter import Button, Frame, Label


class Inventory:
    __items = None

    def __init__(self, perso):
        self.__items = perso

    def useItem(self, name, amount):
        print('NAME : ', name)
        print('AMOUNT : ', amount)
        if( name == 'potion'):
            amount -= 1
            print('x1 ' + name + ' utilisé')
            return amount

        elif( name == 'super-potion'):
            amount -= 1
            print('x1 ' + name + ' utilisé')
            return amount
            
        elif( name == 'mega-potion'):
            print('x1 ' + name + ' utilisé')
            amount -= 1
            return amount
    

        






    

