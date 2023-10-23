# lib/helpers.py
from models.author import Author
from models.book import Book


def space_separator(character="=", lenght=40):
    print(character * lenght)


def print_blank_spaces(lines=1):
    for _ in range(lines):
        print()


def get_all_authors():
    authors = Author.get_all()
    for i in range(len(authors)):
        author = authors[i]
        print(f"{i + 1}: {author.name}")
        print_blank_spaces()


def create_new_author():
    space_separator()
    print_blank_spaces(2)
    name = str(input("Enter the author's name: "))
    print_blank_spaces(2)
    try:
        author = Author.create(name)
        print(f'Success : {author}')
        return author
    except Exception as exc:
        print("Error creating new author ", exc)


def update_author_info(author):
    try:
        name = input(
            "Fix author's name (or press Enter to keep it unchanged): ")
        if name:
            author.name = name

        author.update()
    except Exception as exc:
        print("Error updating author >>> ", exc)


def delete_author_info(author):
    author.delete()
    print_blank_spaces(2)
    print(f"{author} deleted")


def view_books_by_author(author):
    books = Book.get_books_by_author(author.id)

    if not books:
        print(f"No books found for author {author.name}.")
        return

    while True:
        space_separator()
        print(f"Books by {author.name}:")
        print_blank_spaces(2)

        for book in books:
            space_separator("-", lenght=28)
            print(f"Title: {book.title}")
            print(f"Pages: {book.pages}")
            print(f"Rating: {book.rating}")
            print(f"Published Date: {book.published_date}")
            space_separator("-", lenght=28)
            print_blank_spaces(2)

        input("\nPress Enter to return to the previous menu")
        break


def select_author():
    authors = Author.get_all()
    print("Select an author:")
    for idx, author in enumerate(authors, start=1):
        print(f"{idx}: {author.name}")

    while True:
        choice = input(
            "Enter the number of the author (or press A to add a new author): ").strip()
        if choice.lower() == 'a':
            return create_new_author()
        try:
            choice = int(choice)
            if 1 <= choice <= len(authors):
                return authors[choice - 1]
            else:
                print("Invalid choice. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def view_author_info(author_id):
    author = Author.find_by_id(author_id)
    if author:
        print(f"Author Name: {author.name}")
        print(f"Author ID: {author.id}")
        input("Press Enter to return to the previous menu...")
    else:
        print("Author not found")


def get_all_books():
    books = Book.get_all()
    for i in range(len(books)):
        book = books[i]
        print(f"{i + 1}: {book.title}")
        print_blank_spaces()


def create_new_book():
    title = input("Enter the book's title: ")
    pages_str = input("Enter the book's number of pages: ")
    rating_str = input("Enter the book's rating from 0 - 10: ")
    published_date = input(
        "Enter the book's date of publishing in mm/dd/yyy format: ")
    author = select_author()
    if author:
        try:
            pages = int(pages_str)
            rating = int(rating_str)
            book = Book.create(title, pages, rating, published_date, author.id)
            print(f"Success: {book}")
        except Exception as exc:
            print("Error creating new book ", exc)


def update_book_info(book):
    try:
        title = input(
            "Enter the book's updated title (or press Enter to keep it unchanged): ")
        if title:
            book.title = title
        pages = input(
            "Enter the book's updated page count (or press Enter to keep it unchanged): ")
        if pages:
            book.pages = int(pages)
        rating = input(
            "Enter the book's updated rating (or press Enter to keep it unchanged): ")
        if rating:
            book.rating = int(rating)
        published_date = input(
            "Enter the book's updated published date in mm/dd/yyy format (or press Enter to keep it unchanged): ")
        if published_date:
            book.published_date = published_date
        author_id = input(
            "Enter the book's updated author id (or press Enter to keep it unchanged): ")
        if author_id:
            book.author_id = int(author_id)

        book.update()
    except Exception as exc:
        print("Error updating book: ", exc)


def delete_book_info(book):
    book.delete()
    print(f"{book.title} deleted")
