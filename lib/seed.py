from models.__init__ import CONN, CURSOR
from models.author import Author
from models.book import Book


def seed_database():
    Book.drop_table()
    Author.drop_table()
    Book.create_table()
    Author.create_table()

    stephen_king = Author.create("Stephen King")
    Book.create("IT", 698, 8, "12/13/1991", stephen_king.id)


seed_database()
print("Seeded database")
