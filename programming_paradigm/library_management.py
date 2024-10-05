class Book:
    def __init__(self, title, author, _is_checked_out  = False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    def Check_out(self):
        self._is_checked_out = True

    def Return(self):
        self._is_checked_out = False

class Library:   
    _books = []
    def __init__(self):
        pass
        


    def add_book(cls, book):
        cls._books.append(book)
    def check_out_book(cls, title):
        for book in cls._books:
            if book.title == title:
                book._is_checked_out = True

    def return_book(cls, title):    
        for book in cls._books:
            if book == title:
                book._is_checked_out = False

    def list_available_books(cls):
        for book in cls._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
