import json
import csv

# Specify the file name
filename = "output.csv"

# Writing to a CSV file
file = open(filename, mode='w', newline='')
try:
    writer = csv.writer(file)

    # Opening JSON file
    f = open('data.json')

    # returns JSON object as
    data = json.load(f)

    # loop through signups, print name & pos then write to a .csv file
    for signup in data['signUps']:
        print("Name: " + signup['name'] + " Position: " + str(signup['position']))
        writer.writerow([signup['name'], signup['position']])

finally:
    file.close()
    f.close()