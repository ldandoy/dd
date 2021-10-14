class Inventory:

    def __init__(self):
        self.items = []

    def show(self):
        index = 1
        for item in self.items:
            print(str(f'{index} -> [x{item.amount}] {item.name}'))
            index += 1

    def inventory(self):
        print('\nCeci est votre inventaire,\nVeuillez sélectionner un objet : ["0" - Quitter]')
        self.show()
        i = int(input('\nNº > '))
        if i == 0:
            print('\nFermeture de l\'inventaire...')
            quit()
        
        item = self.items[i - 1]
        print(f'Objet {item.name}[x{item.amount}] : ["1" - Utiliser / "2" - Jeter / "0" - Quitter]')
        cmd = int(input('\nNº > '))
        if cmd == 1:
            item.amount = self.use_item(item.name, item.amount, i )
        elif cmd == 2: 
            item.amount = self.drop_item(item.name, item.amount, i )

        self.inventory()
        

    def drop_item(self, name, amount, i):
        if amount == 1:
            amt = 1
            self.items.pop(i - 1)
            print(f'Objet {name}[x{amt}] Jeter!\nVotre nouvelle inventaire:')

        else:
            print(f'Vous avez {amount} cet objet, combien voulez-vous en jeter?')
            amt = int(input('amt > '))
            if amount <= 0:
                amt = 0
                self.items.pop(i - 1)
                print(f'Objet {name}[x{amt}] Jeter!\nVotre nouvelle inventaire est:')
            amount -= amt
            print(f'Objet {name}[x{amt}] Jeter!\nVotre nouvelle inventaire est:')
            return amount
    
    def use_item(self, name, amount, i):
        print(f'\nVoulez-vous utiliser une {name}? ["1" - Oui / "0" - Non]')
        cmd = int(input('\nNº > '))
        if cmd == 0:
            print('\nFermeture de l\'inventaire...')
            self.inventory()
            
        elif cmd == 1:
            amt = 1
            amount -= amt
            print(f'Objet {name}[x{amt}] Utiliser!\n')
            # Ajouter x HP au personnage
            return amount




