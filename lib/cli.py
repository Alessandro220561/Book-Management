from models.author import Author
from models.book import Book
import os


from helpers import (
    space_separator,
    print_blank_spaces,
    update_book_info,
    delete_book_info,
    create_new_author,
    create_new_book,
    view_author_info,
    update_author_info,
    delete_author_info,
    view_books_by_author,
    get_all_authors,
    get_all_books
)


def main_menu():
    while True:
        space_separator()
        print_blank_spaces(2)
        print("               Welcome!")
        print_blank_spaces(2)
        print("•Press A for list of all authors")
        print_blank_spaces(2)
        print("•Press B for a list of all books")
        print_blank_spaces(2)
        print("•Press Q to quit the program")
        print_blank_spaces(2)
        space_separator()
        choice = input("> ")

        if choice.lower() == "q":
            exit_program()
        elif choice.lower() == "a":
            authors_menu()
        elif choice.lower() == "b":
            books_menu()
        else:
            print("Invalid choice")


def authors_menu():
    while True:
        space_separator()
        print_blank_spaces(2)
        print("This is a list of all authors")
        print_blank_spaces()
        get_all_authors()
        space_separator("><", lenght=20)
        print("•Enter the number (or press Enter to return to the main menu): ")
        print_blank_spaces()
        print("•Press A to add new author")
        space_separator("><", lenght=20)
        choice = input("> ")
        if choice.lower() == "a":
            create_new_author()
        elif choice.strip() == "":
            os.system('clear')
            break
        else:
            authors = Author.get_all()
            try:
                author_number = int(choice)
                if 1 <= author_number <= len(authors):
                    selected_author = authors[author_number - 1]
                    author_action_menu(selected_author)
                else:
                    print(
                        "Invalid author number. Please choose an author from the list.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        print_blank_spaces(2)
        space_separator()


def author_action_menu(author):
    while True:
        space_separator()
        print_blank_spaces(2)
        print(f"You selected author: {author.name}")
        print_blank_spaces(2)
        space_separator("><", lenght=20)
        print("Author Actions:")
        print_blank_spaces()
        print("1. Update author info")
        print_blank_spaces()
        print("2. Delete author info")
        print_blank_spaces()
        print("3. View all books by this author")
        print_blank_spaces()
        print("4. Return to the previous menu")
        space_separator("><", lenght=20)
        choice = input("> ")
        if choice == "1":
            update_author_info(author)
        elif choice == "2":
            delete_author_info(author)
            break
        elif choice == "3":
            view_books_by_author(author)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")


def books_menu():
    while True:
        space_separator()
        print_blank_spaces(2)
        print("This is a list of all books")
        print_blank_spaces()
        get_all_books()
        print_blank_spaces()
        space_separator("><", lenght=20)
        print("•Enter the number (or press Enter to return to the main menu): ")
        print_blank_spaces()
        print("•Press B to add a new book")
        space_separator("><", lenght=20)
        choice = input("> ")
        if choice.lower() == "b":
            create_new_book()
        elif choice.strip() == "":
            os.system('clear')
            break
        else:
            books = Book.get_all()
            try:
                book_number = int(choice)
                if 1 <= book_number <= len(books):
                    selected_book = books[book_number - 1]
                    book_action_menu(selected_book)
                else:
                    print("Invalid book number. Please choose a book from the list.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        print_blank_spaces(2)
        space_separator()


def book_action_menu(book):
    while True:
        space_separator()
        print_blank_spaces(2)
        print(f"You selected book: {book.title}")
        print(f"Number of pages: {book.pages}")
        print(f"Rating: {book.rating}")
        print(f"Date published: {book.published_date}")
        print(f"Author ID: {book.author_id}")
        print_blank_spaces(2)
        space_separator("><", lenght=20)
        print("Book Actions:")
        print_blank_spaces()
        print("1. Update book info")
        print_blank_spaces()
        print("2. Delete book info")
        print_blank_spaces()
        print("3. View this book's author information")
        print_blank_spaces()
        print("4. Return to previous menu")
        space_separator("><", lenght=20)
        choice = input("> ")
        if choice == "1":
            update_book_info(book)
        elif choice == "2":
            delete_book_info(book)
        elif choice == "3":
            view_author_info(book.author_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")


def exit_program():
    print("Exiting the program")
    exit()


def main():
    main_menu()


if __name__ == "__main__":
    main()
