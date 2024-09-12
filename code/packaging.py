'''
This is a module for parsing packging data
'''

def parse_packaging(packaging_data: str) -> list[dict]:
    '''
    This function parses a string of packaging data and returns a list of dictionaries.
    The order of the list implies the order of the packaging data.

    Examples:

    input: "12 eggs in 1 carton" 
    ouput: [{ 'eggs' : 12}, {'carton' : 1}]

    input: "6 bars in 1 pack / 12 packs in 1 carton"
    output: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]

    input: "20 pieces in 1 pack / 10 packs in 1 carton / 4 cartons in 1 box"
    output: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    '''
    result = []
    
    packaging_data = packaging_data.replace(' ', '')
    packaging_parts = packaging_data.split('/')
    
    for part in packaging_parts:
        parts = part.split('in')
        

        if len(parts) < 2:
            print(f"Warning: invalid part '{part}' detected!")
            continue  
        
        quantity_item = parts[0]  
        unit = parts[1]  
        
        quantity_item_split = quantity_item.split(maxsplit=1)
        if len(quantity_item_split) < 2:
            print(f"Warning: invalid quantity_item '{quantity_item}' detected!")
            continue  
        
        quantity = quantity_item_split[0]
        item = quantity_item_split[1]
        result.append({item: int(quantity)})
        
        unit_split = unit.split(maxsplit=1)
        if len(unit_split) < 2:
            print(f"Warning: invalid unit '{unit}' detected!")
            continue  
        
        unit_quantity = unit_split[0]
        unit_name = unit_split[1]
        result.append({unit_name: int(unit_quantity)})
    
    return result


def calc_total_units(package: list[dict]) -> int:
    '''
    This function calculates the total number of items in a package

    Example:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output 72 (e.g. 6*12*1)

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: 800 (e.g. 20*10*4*1)
    '''
    total_units = 1

    for item in package:
        for quantity in item.values():
            total_units *= quantity 
    
    return total_units

def get_unit(package: list[dict]) -> str:
    '''
    This function returns the items in the packaging (this is the first item in the list)

    Examples:

    input: [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}]
    output: bars

    input: [{ 'pieces' : 20}, {'packs' : 10}, {'carton' : 4}, {'box' : 1}]
    output: pieces

    '''
    
    return list(package[0].keys())[0]

# This will only run from here, not when imported
# # Use this for testing / debugging cases with the debugger
# if __name__ == '__main__':
text = "25 balls in 1 bucket / 4 buckets in 1 bin"
package = parse_packaging(text)
print(package)

package_total = calc_total_units(package)
unit = get_unit(package)
print(f"{package_total} {unit} total")