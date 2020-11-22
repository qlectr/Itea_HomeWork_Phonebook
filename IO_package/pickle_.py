import pickle

class pickle_dumper:
    def __init__(self,filename):
        self.filename = filename
        
    def load(self):
        with open(self.filename, "rb") as f:
            return pickle.load(f)

    def save(self, phonebook):
        with open(self.filename, "wb") as f:
            pickle.dump(phonebook,f)   