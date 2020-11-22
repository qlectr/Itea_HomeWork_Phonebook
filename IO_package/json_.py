import json

class json_dumper:
    def __init__(self,filename):
        self.filename = filename

    def load(self):
        with open(self.filename, "r") as f:
            return json.load(f)

    def save(self, phonebook):
        with open(self.filename, "w") as f:
            json.dump(phonebook,f)        