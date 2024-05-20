"""
Good to use 'with' because don't have to worry about remembering to close files.
"""

friends_txt = r"C:\Development\my_python_bible\dealing_with_files\friends.txt"

with open(friends_txt, 'r') as file:
    file_contents = file.read()
    print(file_contents)