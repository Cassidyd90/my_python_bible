import json


books_file = 'books.json'

def create_book_table():
    with open(books_file, 'w') as file:
        json.dump([], file)

    
def add_book(title, author):
    books = get_all_books()
    books.append({'title':title, 'author':author, 'finished':False})
    save_all_books(books)


def get_all_books():
    with open(books_file, 'r') as file:
        return json.load(file)
    

def save_all_books(books):
    with open(books_file, 'w') as file:
        json.dump(books, file)



def mark_book_finished(title):
    books = get_all_books()
    for book in books:
        if book['title'] == title:
            book['finished'] = True
    save_all_books(books)


def delete_book(title):
    books = get_all_books()
    books = [book for book in books if book['title'] != title]
    save_all_books(books)