import spotipy
import os
import sys
import json
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

def json_dissect(filename):
    with open(filename) as data_file:
        data = json.load(data_file)

    results = []
    for i in range(20):
        results.append(data['items'][i]['track']['id'])
    return results

trackList = json_dissect('savedTracks.json')

# Username: joelmartinez625
username = sys.argv[1]

# Erase cache and prompt for user permission
try:
    token = util.prompt_for_user_token(username, scope="user-library-read")

except:
    os.remove(f'.cache-{username}')
    token = util.prompt_for_user_token(username, scope="user-library-read")

spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()
print(json.dumps(user, sort_keys=True, indent=4))

while True:
    print("\n Enter 1 to exit")

    choice = input("Exit? ")

    if choice == "1":
        break
    else:
        audioFeatures = spotifyObject.audio_features(trackList)
        print(json.dumps(audioFeatures, sort_keys=True, indent=4))
        print(type(audioFeatures))
        '''
        # Maximum of 50 returned at a time
        savedTracks = spotifyObject.current_user_saved_tracks()
        # track1features = spotifyObject.audio_features(savedTracks.track.album.artists.id)
        # print(json.dumps(savedTracks['items'][0]['track']['id'], sort_keys=True, indent=4))
        print(json.dumps(savedTracks, sort_keys=True, indent=4))
        
        with open('savedTracks.json', 'w') as outfile:
            json.dump(savedTracks, outfile)
        '''

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))


