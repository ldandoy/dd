class Weapon:
    def __init__(self, item):
        self.name = item["name"]
        self.type = item["type"]
        self.degat = item["degat"]
        self.test = item["test"]

    def useWeapon(self):
        print("use consumable")
