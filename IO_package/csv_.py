import csv

"""
def load_csv(filename):
    with open(filename, "r") as f:
        return csv.load(f)
"""
def load_csv(filename):
    reader = csv.reader(open(filename, 'r'))
    d = {}
    for row in reader:
        k, v = row
        d[k] = v
    return d

def save_csv(phonebook, filename):
    with open(filename,'w') as f:
        w = csv.writer(f)
        w.writerows(phonebook.items())
