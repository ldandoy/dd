class Item:

    def __init__(self, name, description, amount):
        self.name = name
        self.description = description
        self.amount = amount
        print(f'{name}')

    def add_item_to_inventory(self, inventory):
            inventory.items.append(self)
            print(f'x{self.amount} {self.name} ajouter à l\'inventaire.')
    
    def remove_item_from_inventory(self, inventory):
        inventory.items.remove(self)
        print(f'{self.name} supprimer de l\'inventaire.')

