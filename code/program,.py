'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

# TODO: Write code
import json
from packaging import parse_packaging, calc_total_units, get_unit

input_file_path = 'data/packaging.txt'
output_file_path = 'data/packaging.json'

all_packages = []

with open(input_file_path, 'r') as f:

    for line in f:
        line = line.strip()
        if line:
            package = parse_packaging(line)
            total_units = calc_total_units(package)
            unit = get_unit(package)
            print(f"{line} => total units: {total_units} {unit}")

            all_packages.append(package)

        with open(output_file_path, 'w') as json_file:
            json.dump(all_packages, json_file, indent=4)

        print(f"Packaging data saved to {output_file_path}")