from src.Utils.load_json import LoadJson
from itertools import islice
import os

# Retrieve lasts features from info.json file as string, call it with a number and a key
# example : Last 3 features - GetLastFeaturesByCount(3, "content")
def GetLastFeatures( features_count = None ):
    print(features_count)
    features_array = list()
    json = LoadJson()
    features_json = json.load( os.path.join( os.path.dirname( __file__ ), '../../Datas/News/info.json' ) )

    if(features_count != None):
        last_messages = list( islice( reversed( features_json ), 0, features_count ) )
    else:
        last_messages = list(features_json )
    last_messages.reverse()

    for x in last_messages:
        features_array.append( x )

    return features_array
