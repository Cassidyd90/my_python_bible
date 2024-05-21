"""
Some functions for dealing with files
Don't need to worry about close() because using 'with'
"""

def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)



def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()
