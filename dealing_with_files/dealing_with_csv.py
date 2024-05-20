"""
Get code from csv and dealing with this through code
"""

students_csv = r"C:\Development\my_python_bible\dealing_with_files\csv_students.txt"

file_open = open(students_csv, 'r')
file_read = file_open.readlines()

file_read = [x.strip() for x in file_read[1:]]

for x in file_read:
    person_data = x.split(',')
    name = person_data[0].title()
    age = person_data[1]
    school = person_data[2].title()
    course = person_data[3].capitalize()

    print(f"{name} is {age}, studying {course} at {school}")



# Example of how to prepare data to put into csv
sample_csv_value = ','.join(['Lilie','34','Toulouse','Languages'])
