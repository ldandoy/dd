import json


class LoadJson:
    def __init__(self):
        pass

    def load(self, file):
        f = open(file, encoding='utf-8')
        data = json.load(f)
        f.close()
        return data

    def save(self, file, data):
        with open(file, 'w') as f:
            json.dump(data, f)
