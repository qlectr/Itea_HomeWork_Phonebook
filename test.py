import pickle
import config
import csv

config.create_config()
file_format = config.read_config().upper()
file_name = config.read_config_file_name()

print(file_format)
print(file_name)

reader = csv.reader(open(file_name, 'r'))
d = {}
for row in reader:
    k, v = row
    d[k] = v