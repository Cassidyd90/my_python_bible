from utils.file_operations import save_to_file, read_file
from utils.find import find_in
"""
Import functions
Save and Read using imported functions
"""

app_output = r"C:\Development\my_python_bible\dealing_with_files\app_output.txt"

save_to_file('test', app_output)

read_file(app_output)