# main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    library = Library()

    book1 = Book("Pride and Prejudice", "Jane Austen")
    book2 = EBook("Snow Crash", "Neal Stephenson", 500)
    book3 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    library.list_books()

if __name__ == "__main__":
    main()
