from Utils.loadJson import LoadJson
from itertools import islice
import os

#Retrive lasts features from info.json file as string, call it with a number and a key
#exemple : Last 3 features - GetLastFeatures(3, "content")

def GetLastFeatures(features_count, key):
    json = LoadJson()
    features_json = json.load( os.path.join( os.path.dirname(__file__), '../../Datas/News/info.json' ) )

    last_messages = list( islice( reversed( features_json ), 0, features_count ) )
    last_messages.reverse()

    for x in last_messages:
        print( str(x[ key ]) )


        # last_messages = self.JSON.load(os.path.join(self.base_folder, '../../Datas/News/info.json'))
        #
        # label_textwelcomeframe = Label( textwelcomeframe, text=last_messages[0]['content'], fg='dark grey', bg=None )
        # label_textwelcomeframe_config = ('Calirbi (Body)', 24, 'bold')
        # label_textwelcomeframe.config( font=label_textwelcomeframe_config )
        # label_textwelcomeframe.place( x=400, y=400 )