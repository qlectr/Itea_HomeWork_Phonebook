import json

def load_json(filename):
    with open(filename, "r") as f:
        return json.load(f)

def save_json(phonebook, filename):
    with open(filename, "w") as f:
        json.dump(phonebook,f)        