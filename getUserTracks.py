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


def track_dissect(tracks):
    results = []
    for i in range(len(tracks['items'])):
        results.append(tracks['items'][i]['track']['id'])
    return results

while True:
    print("\n Enter 1 to exit")

    choice = input("Exit? ")

    if choice == "1":
        break
    else:
        # Maximum of 50 returned at a time

        # Do/While LOOP get length to expect first then fill it all up...

        tracks = spotifyObject.current_user_saved_tracks(limit=50)
        totalTracks = track_dissect(tracks)

        runs = math.ceil(tracks['total']/50) - 1
        for i in range(runs):
            time.sleep(1)
            print('wait...')
            offset_i = 50 * (i + 1)
            tracks = spotifyObject.current_user_saved_tracks(limit=50, offset=offset_i)
            totalTracks.extend(track_dissect(tracks))

        # print(totalTracks, len(totalTracks))
        with open('allTracks.pkl', 'wb') as f:
            pickle.dump(totalTracks, f)

        # track1features = spotifyObject.audio_features(savedTracks.track.album.artists.id)
        # print(json.dumps(savedTracks['items'][0]['track']['id'], sort_keys=True, indent=4))
        # print(json.dumps(savedTracks, sort_keys=True, indent=4))
        # print(type(savedTracks))

# print(json.dumps(VARIABLE, sort_keys=True, indent=4))


