import json
import csv
f = open("employees.json")
data = json.load(f)
name = data['name']
with open('data.csv','w') as csvFile:
    csv_writer = csv.writer(csvFile)
    for skill in data['skills']:
        csv_writer.writerow([name,skill])

with open('data.csv','r') as csvFile:
    csv_reader = csv.reader(csvFile)
    for row in csv_reader:
        print(','.join(row))
