import json

with open('savedTracks.json') as data_file:
    savedTracks = json.load(data_file)

print(savedTracks['items'][0]['track']['id'])

results = []
for i in range(20):
    results.append(savedTracks['items'][i]['track']['id'])

print(results, sep='\n')
