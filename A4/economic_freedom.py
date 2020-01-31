"""
Author: Zack Cochran
Date: 01/30/2020
Goal: To print data on economic freedom rankings by country.
"""

# importing the csv file: each row is a dictionary
# economic_freedom is a list of all the economic freedom rating dictionaries

import csv                  # import csv python module
import json                 # import JSON python module
economic_freedom = []       # create an empty list variable
row_count = 0               # count variable for if logic & to show row number on print screen


# open csv file so that it can be referenced from csvfile
with open('efw.csv', 'r') as csvfile:
    # use the csv.DictReader command to convert to a reader object
    reader = csv.DictReader(csvfile)

    # loop over the reader object
    for efw_row_dic in reader:
        row_count += 1
        economic_freedom.append(efw_row_dic)
        if row_count < 163:
            print('{0:>3}  Year: {1:<4}   Country: {2:<22}    Economic Freedom: {3:<4}   Rank: {4}'.format(
                row_count, efw_row_dic['year'],
                efw_row_dic['countries'],
                efw_row_dic['ECONOMIC FREEDOM'],
                efw_row_dic['rank']))

print('Found this many rows: ' + str(len(economic_freedom)))

# converts the CSV to a JSON file
with open('economic_freedom.json', 'w') as fp:
    json.dump(economic_freedom, fp, sort_keys=True, indent=4, separators=(',', ': '))

print('This CSV has been converted to a JSON file. ')
