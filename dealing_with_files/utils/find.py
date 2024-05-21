
def find_in(iterable, finder, expected):
    for i in iterable:
        if finder(i) == expected:
            return i 
    raise NotFoundError(f'{expected} not found in provided iterable.')


class NotFoundError(Exception):
    pass


"""
Only run this as script
Using __name__ is __main__ runs directly here but won't execute when find_in called in other scripts
"""
if __name__ == '__main__':
    print(find_in(['Dylan', 'Mina', 'Lilie'], lambda x: x, 'Mina'))