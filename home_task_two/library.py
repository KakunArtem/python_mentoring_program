from typing import Dict

from home_task_two.book import Book
from home_task_two.user import User


class Library:
    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.users: Dict[str, User] = {}

    def add_book(self, book: Book):
        self.books[book.title] = book
        print(f"{book.title} has been added to the library.")

    def remove_book(self, title: str):
        if title in self.books:
            self.books.pop(title)
            print(f"{title} has been removed from the library.")
            return True
        else:
            print(f"Sorry, {title} is not in the library.")
            return False

    def add_user(self, user: User):
        self.users[user.user_id] = user
        print(f"User {user.user_id} has been added to the library.")

    def remove_user(self, user_id: str):
        if user_id in self.users:
            user = self.users.pop(user_id)
            print(f"User {user.user_id} has been removed from the library.")
            return True
        else:
            print(f"Sorry, user ID {user_id} is not in the library.")
            return False

    def check_out_book(self, title, user: User):
        if title in self.books and user.user_id in self.users:
            book = self.books[title]
            user = self.users[user.user_id]
            if book.number_of_copies > 0 and user.borrow_book(book):
                book.number_of_copies -= 1
                print(f"User {user.user_id} borrows {title}.")
                return True
            else:
                print(f"User {user.user_id} tries to borrow {title} but book is not in stock.")
                return False

    def return_book(self, title, user: User):
        if title in self.books and user.user_id in self.users:
            book = self.books[title]
            user = self.users[user.user_id]
            if user.return_book(book):
                book.number_of_copies += 1
                print(f"Book {title} returned to library by user {user.user_id}.")
                return True
            else:
                return False
