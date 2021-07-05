import json


class LoadJson:
    def __init__(self):
        pass

    def load(self, file):
        f = open(file)
        data = json.load(f)
        f.close()
        return data
