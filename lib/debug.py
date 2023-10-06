#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.book import Book
import ipdb


def reset_database():
    Book.drop_table()
    Author.drop_table()
    Book.create_table()
    Author.create_table()

    stephen_king = Author.create("Stephen King")
    Book.create("IT", stephen_king.id, 698, 8, "12/13/1991")


ipdb.set_trace()
