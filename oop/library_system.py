# library_system.py

class Book:
    """Base class for all books"""
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    """Derived class for electronic books"""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in KB

class PrintBook(Book):
    """Derived class for printed books"""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

class Library:
    """Library class demonstrating composition"""
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library"""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library"""
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
