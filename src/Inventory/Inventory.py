from tkinter import Button, Frame, Label


class Inventory:
    __frame = None
    __items = None

    def inventoryFrame( self, q ):
        inventoryFrame = Frame( q, width=1024, height=600, bg="#b9deff" )
        inventoryFrame.place( x=0, y=0 )

        def back():
            inventoryFrame.destroy()
            q.textWelcomeFrame()

        itemButton = Button( self.__frame, text="Retour", command=back, border=0,
                                activebackground='#12c4c0', bg="#12c4c0" )
        itemButton.place( x=400, y=200 )

    def __init__(self, perso, q):
        self.__items = perso
        self.__frame = self.inventoryFrame(q)

    def itemChoice( self ):
        print( "item ajoute" )

    

    def show(self):
        # index = 1
        # for item in self.items:
        #     print(str(f'{index} -> [x{item.amount}] {item.name}'))
        #     index += 1


        for i, item in enumerate(self.__items):
            itemLabel = Label( self.__frame, text=item, fg='white', bg='#0483d1' )
            itemLabelConfig = ('Calirbi (Body)', 36, 'bold')
            itemLabel.config( font=itemLabelConfig )
            itemLabel.place( x=25, y=200 + (i * 80) )
            itemButton = Button( self.__frame, text="Utiliser", command=self.itemChoice, border=0,
                                activebackground='#12c4c0', bg="#12c4c0" )
            itemButton.place( x=225, y=200 + (i * 80) )








    def inventory(self, slot):
        print('\nCeci est votre inventaire,\nVeuillez sélectionner un objet : ["0" - Quitter]')
        self.show()
        i = slot
        if i == 0:
            print('\nFermeture de l\'inventaire...')
            quit()
        
        item = self.items[i - 1]
        item.amount = self.use_item(item.name, item.amount)

        self.inventory()
    
    def use_item(self, name, amount):
            amt = 1
            amount -= amt
            print(f'Objet {name}[x{amt}] Utiliser!\n')
            # Ajouter x HP au personnage
            return amount


    

