import argparse
import csv
import os
from termcolor import cprint


parser = argparse.ArgumentParser(description='Transforms a csv-file according to the rules defined within this script')
parser.add_argument('--file', dest='input_file', required=True, help='The input csv file')
args = parser.parse_args()

# map arguments
input_file = args.input_file

if not os.path.isfile(input_file):
    cprint('Error specified file could not be found. Aborting', 'white', 'on_red')
    exit()

def get_basepath(filepath):
    return os.path.splitext(filepath)[0]


output_file = get_basepath(input_file) + '_output.csv'
fieldnames = None

result = []
with open(input_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='{')
    fieldnames = reader.fieldnames
    for row in reader:
        edited_row = row
        edited_row['wine-name'] = edited_row['Weingut'] + ' ' + edited_row['wine-name']
        result.append(edited_row)

#[print(row['wine-name']) for row in result[:20]]

with open(output_file, 'w', newline='') as output:
    writer = csv.DictWriter(output, fieldnames, delimiter='{', quoting=csv.QUOTE_ALL)
    writer.writeheader()
    for row in result:
        writer.writerow(row)
