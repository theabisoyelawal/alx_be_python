# book_class.py

class Book:
    def __init__(self, title, author, year):
        """Constructor: Initialize title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Print message when the object is deleted."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation: user-friendly output."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation: recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
