"""
.read() goes through file and reads as one long string
.close() is always best to use or else python thinks it has to keep it open

.read() with 'r' is read mode
.read() with 'w' is write mode , this will overwrite whatever is in the file
"""


# Read file
file_location = r"C:\Development\my_python_bible\dealing_with_files\data.txt"
my_file = open(file_location, 'r') # 'r' is for read
file_content = my_file.read()
my_file.close()
print(file_content)

# Write to file 
username = input('Enter your name:')
my_file_writing = open(file_location, 'w') # 'w' is for writing
my_file_writing.write(username)
my_file_writing.close()



