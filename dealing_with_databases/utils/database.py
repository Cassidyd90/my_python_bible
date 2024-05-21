"""
Used for storing and retrieving books from a list
In memory database
"""


books = []


def add_book(name, author):
    books.append({'name':name, 'author':author, 'read':False})

