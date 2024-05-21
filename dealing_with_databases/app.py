"""
This is core script for creating a book store app
User menu
"""

from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:
"""


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        pass



"""
def prompt_add_book()
def list_books()
def prompt_book_read()
def prompt_delete_book()
"""