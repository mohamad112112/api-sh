
import json
import os

def load_food_data(path="app/foodnet_data.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)
