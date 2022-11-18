class Item:
    def __init__(self, item):
        self.name = item["name"]

    def useItem(self):
        print("use item")
