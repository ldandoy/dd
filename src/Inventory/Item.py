class Item:
    name: str
    description: str
    amount: int

    def __init__(self, itemInfos):
        self.name = itemInfos.name
        self.description = itemInfos.description | "No description available."
        self.amount = itemInfos.amount

    def useItem(self):
        print(f"use item : {self.name}")

    def renderItem(self):
        print('Render items')