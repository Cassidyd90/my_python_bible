from utils.database import books

"""
Functions to interact with database
"""

def books_add():

    name = input("Enter the book name: ")
    author = input("Enter the author: ")
    genre = input("Enter the genre: ")

    while True:
        input_finished = input('Have you finished the book? True or False? ')
        if input_finished == 'True':
            finished = True
            break
        elif input_finished == 'False':
            finished = False
            break
        else:
            print('Please enter True or False.')

    score = None
    if finished == True:
        while True:
            try:
                input_score = int(input("What score out of 10? "))
                if 0 <= input_score <= 10:
                    score = input_score
                    break
                else:
                    print("Score must be between 0 and 10.")
            except ValueError:
                print("Please enter a valid integer for the score.")


    books.append({
        'name': name,
        'author': author,
        'genre': genre,
        'score': score,
        'finished': finished
    })


def books_list():
    for book in books:
        print(f"Name: {book['name']}")
        print(f"Author: {book['author']}")
        print(f"Genre: {book['genre']}")
        print(f"Score: {book['score']}")
        print(f"Finished: {book['finished']}")


def books_names():
    for book in books:
        print(f"{book['name']}")



def book_finished():
    while True:
        select_book = input('Which book do you want to update? ')

        # Find the book in the list
        book_found = None
        for book in books:
            if book['name'] == select_book:
                book_found = book
                break

        if book_found:
            while True:
                book_finished = input('Have you finished the book? True or False? ')
                if book_finished == 'True':
                    book_found['finished'] = True
                    break
                elif book_finished == 'False':
                    book_found['finished'] = False
                    break
                else:
                    print('Please enter True or False.')

            print('Book status updated successfully.')
            break
        else:
            books_names()
            print('Book not found in the list.')      




def book_delete():
    while True:
        select_book = input('Which book do you want to delete? ')

        # Find the book in the list
        book_found = None
        for book in books:
            if book['name'] == select_book:
                book_found = book
                break

        if book_found:
            while True:
                book_to_delete = input('Are you sure you want to delete? y/n ')
                if book_to_delete == 'y':
                    books.remove(book_found)
                    print("Book has been deleted.")
                    break
                elif book_to_delete == 'n':
                    break
                else:
                    print('Please enter y/n.')
            break
        else:
            books_names()
            print('Book not found in the list.')