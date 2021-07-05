from Utils.loadJson import LoadJson


class InitialQuest:
    data = []

    def __init__(self):
        j = LoadJson()
        self.data = j.load('Datas/Story/initialQuest.json')

    def welcome(self):
        print(self.data['welcome'])
