#virtualna biblioteka
#CRUD
#dodaj knjigu
#izlistaj knjigu
#obrisi knjigu

books = []

def add_book(name,author):
    books.append({'name':name,'author':author})

def find_book_by_name(name):
    for book in books:
        if book['name'] == name:
            return book

def delete_book_by_name(name):
    found_book = find_book_by_name(name)
    if found_book is None:
        print("Knjiga ne postoji")
    else:
        books.remove(found_book)
        print("Knjiga je obrisana")



add_book('Harry Potter','J K Rowling')
add_book('Harry Potter 3','J K Rowling')

find_book_by_name('Harry Potter')

delete_book_by_name('Harry Potter 3')

print(books)
