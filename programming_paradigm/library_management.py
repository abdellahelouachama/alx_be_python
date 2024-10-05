class Book:
    def __init__(self, title, author, _is_checked_out  = False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out
    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

class Library:   
    
    def __init__(self):
       self._books = []
        


    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                # book._is_checked_out = True
                book.check_out()

    def return_book(self, title):    
        for book in self._books:
            if book.title == title:
                # book._is_checked_out = False
                book.return_book()

    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                print(f"{book.title} by {book.author}")
