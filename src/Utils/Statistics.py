from Utils.loadJson import LoadJson
import os


class Stats:
    @staticmethod
    def get_stat(achievement):
        stat = LoadJson().load(os.path.join('Datas', 'Stats', 'global.json'))
        return stat[achievement]

    @staticmethod
    def add_achievement(achievement):
        path = os.path.join('Datas', 'Stats', 'global.json')
        stat = LoadJson().load(path)
        print(stat[achievement])
        stat[achievement] += 1 if stat[achievement] >= 0 else 0
        LoadJson().save(path, stat)
