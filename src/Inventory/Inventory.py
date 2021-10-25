class Inventory:

    def __init__(self):
        self.items = []

    def show(self):
        index = 1
        for item in self.items:
            print(str(f'{index} -> [x{item.amount}] {item.name}'))
            index += 1

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




