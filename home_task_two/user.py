from typing import Union

from home_task_two.book import Book


class User:
    def __init__(self, user_name: str, user_id: Union[str, int]):
        # user_id can be used as a key/identifier, so it safe to work with it as a string by default
        if type(user_id) == int:
            user_id = str(user_id)

        self.user_name = user_name
        self.user_id = user_id
        self.borrowed_books = []
        self.borrow_limit = 5

    def __str__(self):
        return f"User: {self.user_name} ({self.user_id})"

    def borrow_book(self, book: Book):
        if len(self.borrowed_books) == self.borrow_limit:
            print(f"Sorry, {self.user_name}, you have reached a limit. "
                  f"You must return the book before you can borrow a new one.")
            return False
        else:
            self.borrowed_books.append(book)
            print(f"Book '{book.title}' has been borrowed by {self.user_name}.")
            return True

    def return_book(self, book: Book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"Book '{book.title}' has been returned by {self.user_name}.")
            return True
        else:
            print(f"Sorry, '{book.title}' has not been borrowed by you, so it cannot be returned.")
            return False
