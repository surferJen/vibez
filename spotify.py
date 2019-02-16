#how to grab information from spotify
import requests
import json
import base64
from config import client_id, client_secret




####IMPORTANT IF REQUEST TIMES OUT THAT IS DUE TO VAGRANT DESYNC.RELOAD VAGRANT SERVER AND TRY AGAIN###

#THIS IS THE FLOW FOR TESTING ENDPOINTS
#USE SPOTIFY API CONSOLE AND TEST SEARCH RESULTS
#TAKE CURL COMMAND STRIP OUT ACCESS TOKEN AND ADD FRESH TOKEN
#TAKE MODIFIED SPOTIFY CURL COMMAND AND CONVERT IT TO PYTHON REQUEST

def generate_token():
        #Generate token this generates a client token to be used in your spotify api request
        #This must be performed server side as spotify will block any post requests via client ajax request
        #This token must be generated to use spotify webapi
        
        base64encoded = base64.b64encode("{}:{}".format(client_id, client_secret).encode('ascii'))
        
        headers = {
            'Authorization': 'Basic {}'.format(base64encoded.decode('ascii')),
        }

        data = {
        'grant_type': 'client_credentials'
        }

        response = requests.post(
        'https://accounts.spotify.com/api/token', headers=headers, data=data)

        tokenJSON = response.json()
        ##TESTING PRINT TO VERIFY GENERATED SPOTIFY TOKEN
        print('this is your access token---> '+ tokenJSON["access_token"])
        ##Returning our token for consumption throughout program
        return tokenJSON["access_token"]

##AT = ACCESS TOKEN
def base_playlist(at, genre, min_danceability, max_danceability):
        #Ok this is the meat an potatoes we will now generate a list of hiphop music based on parameters
        #Note that this would probably be set from the client,but an initial state would need to be accounted for
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+ at,
        }


        params = (
        ##BEGINNING OF URL QUERY PARAMS 4 SPOTIFY
        #all of these parameters can be changed to the parameters being passed through the function
        #this can make the function constimizable
            ('limit', '50'),
            ('market', 'US'),
            ('seed_genres', genre),
            ('min_danceability', min_danceability),
            ('max_danceability', max_danceability),
            ('min_popularity', '50'),

        )

        response = requests.get('https://api.spotify.com/v1/recommendations',
                                headers=headers, params=params)

        songsJSON = response.json()
        ##Reformatting print statement for readibility
        return songsJSON

##Fresh token generates whenever query function is run this may not be performant
# print(base_playlist(generate_token(), 'bluegrass' ,'0', '0.35 '))


#available genres in Spotify(typing must be exact): acoustic, afrobeat,
    # alt-rock, alternative, ambient, anime, black-metal, bluegrass,
    # blues, bossanova, brazil, breakbeat, british, cantopop, chicago-house,
    # children, chill, classical, club, comedy, country, dance, dancehall,
    # death-metal, deep-house, detroit-techno, disco, disney, drum-and-bass,
    # dub, dubstep, edm, electro, electronic, emo, folk, forro, french,
    # funk, garage, german, gospel, goth, grindcore, groove, grunge, guitar,
    # happy, hard-rock, hardcore, hardstyle, heavy-metal, hip-hop, holidays,
    # honky-tonk, house, idm, indian, indie, indie-pop, industrial, iranian,
    # j-dance, j-idol, j-pop, j-rock, jazz, k-pop, kids, latin, latino,
    # malay, mandopop, metal, metal-misc, metalcore, minimal-techno, movies,
    # mpb, new-age, new-release, opera, pagode, party, philippines-opm, piano,
    # pop, pop-film, post-dubstep, power-pop, progressive-house, psych-rock,
    # punk, punk-rock, r-n-b, rainy-day, reggae, reggaeton, road-trip, rock,
    # rock-n-roll, rockabilly, romance, sad, salsa, samba, sertanejo,
    # show-tunes, singer-songwriter, ska, sleep, songwriter, soul,
    # soundtracks, spanish, study, summer, swedish, synth-pop, tango,
    # techno, trance, trip-hop, turkish, work-out, world-music

def saved_songs(at, track_id):
        #Ok this is the meat an potatoes we will now generate a list of hiphop music based on parameters
        #Note that this would probably be set from the client,but an initial state would need to be accounted for
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + at,
        }

        params = (
            ##BEGINNING OF URL QUERY PARAMS 4 SPOTIFY
            #all of these parameters can be changed to the parameters being passed through the function
            #this can make the function constimizable
            ('ids', track_id),
        )

        response = requests.get("https://api.spotify.com/v1/tracks",
                                headers=headers, params=params)

        songsJSON = response.json()
        ##Reformatting print statement for readibility
        return songsJSON


print(saved_songs(generate_token(), "45XhKYRRkyeqoW3teSOkCM,7hsulgRNgbyczeAg8tChCB,608a1wIsSd5KzMEqm1O7w3"))




##TODO MOODPLAYLIST

##TODO DATA MAPPING
##SPOTIFY DATA MODEL SHOULD BE IN PARODY WITH PROJECT TABLES FOR CRUD FUNCTIONALITY
