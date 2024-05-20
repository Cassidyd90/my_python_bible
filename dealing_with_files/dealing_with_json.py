import json
"""
Read in JSON files
Reads JSON to dictionary
"""
friends_json = r"C:\Development\my_python_bible\dealing_with_files\friends_json.txt"

file = open(friends_json, 'r')

file_contents = json.load(file)

file.close()




"""
Export in JSON format
Dictionary to JSON
"""
cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]


cars_json = r"C:\Development\my_python_bible\dealing_with_files\cars_json.txt"

export_json_file = open(cars_json, 'w')

json.dump(cars, export_json_file, indent=6)

export_json_file.close()



