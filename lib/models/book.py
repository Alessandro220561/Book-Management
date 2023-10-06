from models.__init__ import CURSOR, CONN


class Book:

    all_books = {}

    def __init__(self, title, author_id, total_pages, rating, published_date):
        self.title = title
        self.author_id = author_id
        self.total_pages = total_pages
        self.rating = rating
        self.published_date = published_date

    def __repr__(self):
        return (
            f"<<<Book {self.id}: {self.title}, {self.total_pages}, {self.rating}, {self.published_date}, " +
            f"Author ID: {self.author_id} >>>"
        )
