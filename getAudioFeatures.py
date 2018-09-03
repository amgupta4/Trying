import spotipy
import os
import sys
import json
import webbrowser
import time
import spotipy.util as util
import math
from json.decoder import JSONDecodeError
import pickle

# Read in a pickle of audio features
with open('allTracks.pkl', 'rb') as f:
    allTracks = pickle.load(f)

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
        allFeatures = []
        for i in range(len(allTracks)//50 + 1):
            features = spotifyObject.audio_features(allTracks[50*i:50*(i+1)])
            allFeatures.extend(features)
            time.sleep(1)
            print('wait..')

        print(len(allFeatures))
        # Save all features to a pickle file
        with open('allFeatures.pkl', 'wb') as f:
            pickle.dump(allFeatures, f)
        # print(json.dumps(savedTracks['items'][0]['track']['id'], sort_keys=True, indent=4))
        # print(json.dumps(savedTracks, sort_keys=True, indent=4))
        # print(type(savedTracks))

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))


