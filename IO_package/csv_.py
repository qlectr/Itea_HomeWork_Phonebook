import csv
import pandas

class csv_dumper:
    def __init__(self,filename):
        self.filename = filename

    def load(self):
        reader = csv.reader(open(self.filename, 'r'))
        phonebook = {}
        for row in reader:
            key, value = row
            phonebook[key] = value
        return phonebook

    def save(self, phonebook):
        with open(self.filename,'w') as f:
            w = csv.writer(f)
            w.writerows(phonebook.items())
