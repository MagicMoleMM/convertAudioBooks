import json
import pandas as pd

dt = pd.read_csv('./love_fantasy.csv') 

dt.to_json('db.json', orient="index")

with open('./db.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)