import json

csv_file = r"C:\Development\my_python_bible\dealing_with_files\csv_file.txt"
json_file_txt = r"C:\Development\my_python_bible\dealing_with_files\json_file.txt"

json_list = []      # store the converted json data for each line
csv_file = open(csv_file, 'r')
 
for line in csv_file.readlines():
    club, city, country = line.strip().split(',')   # first get rid of the \n and then split with ','
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)
 
csv_file.close()
 
json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)     # write json data to a file
json_file.close()
