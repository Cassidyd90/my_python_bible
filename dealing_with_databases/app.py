"""
This is core script for creating a book store app
User menu
"""

from utils.database import books
from utils.crud_functions import books_add, books_list, book_finished, book_delete



USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice:
"""




def user_menu():
    
    selection = input(USER_CHOICE)
    while selection != 'q':
        if selection == "a":
            books_add()

        elif selection == "l":
            books_list()

        elif selection == "f":
            book_finished()

        elif selection == 'd':
            book_delete()

        else:
            print('Unknown command. Please try again.')

        selection = input(USER_CHOICE)


user_menu()

