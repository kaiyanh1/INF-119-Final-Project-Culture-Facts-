import json
import random
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'cultures.json')


def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: Data file not found at {DATA_FILE}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in data file {DATA_FILE}")
        return {}


DATA = load_data()


def list_cultures():
    return list(DATA.keys())



def search_culture(name):
    for culture_name, details in DATA.items():
        if culture_name.lower() == name.lower():
            return details
    return None



def get_random_fact():
    all_facts = []
    for culture in DATA.values():
        all_facts.extend(culture['facts'])
    if all_facts:
        return random.choice(all_facts)
    else:
        return None



def get_details(culture_name):
    if culture_name in DATA:
        return DATA[culture_name]
    else:
        return None