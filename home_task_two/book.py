class Book:
    def __init__(self, title: str, author: str, number_of_copies: int):
        self.title = title
        self.author = author
        self.number_of_copies = number_of_copies

    def __str__(self):
        return f"Book: {self.title} by author: {self.author}"

    def info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Number of copies: {self.number_of_copies}")

    def borrow_books(self, n: int):
        if n <= self.number_of_copies:
            self.number_of_copies -= n
            print(f"{n} copies of the book have been borrowed. {self.number_of_copies} still in stock.")
        else:
            print(f"Sorry, only {self.number_of_copies} is available in stock.")

    def return_books(self, n: int):
        self.number_of_copies += n
        print(f"{n} books was returned to stock. {self.number_of_copies} copies are available")
