class Item:
    def __init__(self, item):
        self.name = item["name"]
        self.qty = item["qty"]

    def useItem(self):
        print(f"use item : {self.name}")

