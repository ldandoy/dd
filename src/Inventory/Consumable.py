class Consumable:
    def __init__(self, item):
        self.name = item["name"]
        self.qty = item["qty"]
        self.qty_max = item["qty_max"]
        self.type = item["type"]
        self.heal = item["heal"]

    def useConsumable(self):
        print("use consumable")
