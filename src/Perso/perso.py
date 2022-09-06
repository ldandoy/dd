import json
import os

from Utils.load_json import LoadJson


class Perso:
    __fileName = None
    __perso = None
    __inventory = None

    def __init__(self, filename):
        self.base_folder = os.path.dirname(__file__)
        json = LoadJson()
        self.__fileName = filename
        self.__perso = json.load( os.path.join( self.base_folder, '../../Datas/Perso', filename ) )
        self.__inventory = self.__perso['inventaire']

    def getPerso( self ):
        return self.__perso

    def getInventaire( self ):
       return self.__inventory

    def save( self ):
        path = os.path.join( self.base_folder, '../../Datas/Perso/' )
        print(path)
        if os.path.exists(path + self.__fileName  ):
            os.remove(path + self.__fileName )
            with open(path + self.__fileName, "w") as outfile:
                json.dump(self.__perso, outfile)
        else:
            print( "The file does not exist" )