# lib/helpers.py
from models.author import Author
from models.book import Book


def space_separator(character="*", lenght=40):
    print(character * lenght)


def print_blank_spaces(lines=1):
    for _ in range(lines):
        print()


def get_all_authors():
    breakpoint
    authors = Author.get_all()
    for author in authors:
        print(author)
