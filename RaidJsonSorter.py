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
        print("Name: " + signup['name'] + " | Position: " + str(signup['position']) + " | Class: " + signup['className'] + " | Role: " + signup['roleName'])
        writer.writerow([signup['name'], signup['position'], signup['className'], signup['roleName']])
    print('')
    print('Make sure you deleted \'output.csv\' before running this file')
    print('Names, Signup Positions,Classes and roles have been added to output.csv. Have a good day and have it for the Horde.')
finally:
    file.close()
    f.close()