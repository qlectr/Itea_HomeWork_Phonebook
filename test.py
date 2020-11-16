import csv
import pandas

phonebook = {}



with open('phonebook.csv', 'r') as data: 
    for line in csv.DictReader(data): 
        print(line) 
