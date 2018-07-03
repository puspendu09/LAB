import csv
import time

all_lines = []
with open('websites.csv') as f:
    reader = csv.reader(f)
    print(reader)


for row in reader:
    print (row)

