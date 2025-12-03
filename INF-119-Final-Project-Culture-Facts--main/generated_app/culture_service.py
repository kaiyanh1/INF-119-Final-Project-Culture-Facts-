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
        print(f"Error: Could not find {DATA_FILE}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {DATA_FILE}")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

data = load_data()

def list_cultures():
    global data
    if data:
        return [culture['name'] for culture in data]
    else:
        return None


def search_culture(name):
    global data
    if data:
        for culture in data:
            if culture['name'].lower() == name.lower():
                return culture
    return None


def get_random_fact():
    global data
    if data:
        all_facts = []
        for culture in data:
            all_facts.extend(culture['facts'])
        if all_facts:
            return random.choice(all_facts)
        else:
            return None
    else:
        return None

def get_details(culture_name):
    global data
    if data:
        for culture in data:
            if culture['name'].lower() == culture_name.lower():
                return culture
    return None