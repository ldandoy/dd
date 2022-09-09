from Utils.load_json import LoadJson
from itertools import islice
import os


def GetInventoryItems( features_count = None ):
    print(features_count)
    features_array = list()
    json = LoadJson()
    features_json = json.load( os.path.join( os.path.dirname( __file__ ), '../../Datas/Inventaire/items.json' ) )
    if(features_count != None):
        last_messages = list( islice( reversed( features_json ), 0, features_count ) )
    else:
        last_messages = list(features_json)
    last_messages.reverse()

    for x in last_messages:
        features_array.append( x )


    return features_array

