import pickle
import json
import pandas as pd

with open('allFeatures.pkl', 'rb') as f:
    features = pickle.load(f)

print(json.dumps(features, sort_keys=True, indent=4))

df = pd.DataFrame(features)
print(df.head())