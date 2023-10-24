from home_task_two.book import Book
from home_task_two.library import Library
from home_task_two.user import User

if __name__ == '__main__':
    book_1 = Book("The Fellowship of the Ring", "J. R. R. Tolkien", 5)
    book_2 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 42)
    book_3 = Book("Hero's journey", "Joseph Campbell", 1)

    user_1 = User("Billy", 101)
    user_2 = User("Van", 505)
    user_3 = User("Chad", 808)

    library = Library()
    [library.add_book(book) for book in [book_1, book_2, book_3]]
    [library.add_user(user) for user in [user_1, user_2, user_3]]

    assert library.check_out_book(book_1.title, user_1) == True
    assert library.check_out_book(book_1.title, user_3) == True
    assert library.check_out_book(book_3.title, user_1) == True
    assert library.check_out_book(book_3.title, user_2) == False

    assert library.return_book(book_3.title, user_1) == True
    assert library.return_book(book_1.title, user_1) == True

    assert library.remove_user(user_1.user_id) == True
    assert library.remove_user(user_1.user_id) == False

    assert str(book_1) == "The Fellowship of the Ring by author: J. R. R. Tolkien"
    assert str(book_2) == "The Hitchhiker's Guide to the Galaxy by author: Douglas Adams"
    assert str(book_3) == "Hero's journey by author: Joseph Campbell"
