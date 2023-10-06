from models.__init__ import CURSOR, CONN
from models.author import Author
import datetime


class Book:

    all_books = {}

    def __init__(self, title, author_id, total_pages, rating, published_date, id=None):
        self.title = title
        self.author_id = author_id
        self.total_pages = total_pages
        self.rating = rating
        self.published_date = published_date
        self.id = id

    def __repr__(self):
        return (
            f"<<<Book {self.id}: {self.title}, {self.total_pages}, {self.rating}, {self.published_date}, " +
            f"Author ID: {self.author_id} >>>"
        )

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title):
            self._title = title
        else:
            raise ValueError(
                "Book title must be a non-empty string"
            )

    @property
    def total_pages(self):
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        if isinstance(total_pages, int):
            self._total_pages = total_pages
        else:
            raise ValueError(
                "The book's total page count must be an integer"
            )

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if isinstance(rating, int):
            self._rating = rating
        else:
            raise ValueError(
                "Book rating must be an integer"
            )

    @property
    def published_date(self):
        return self._published_date

    @published_date.setter
    def published_date(self, date_str):
        date_format = "%m/%d/%Y"
        try:
            parsed_date = datetime.datetime.strptime(date_str, date_format)
        except ValueError:
            raise ValueError(
                "Invalid date format, please use mm/dd/yyy format"
            )
        self._published_date = parsed_date.strftime(date_format)

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS books
            (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author_id INT,
            FOREIGN KEY (author_id) REFERENCES authors(id),
            total_pages INT,
            rating INT,
            published_date TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS books
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO books
            (title, author_id, total_pages, rating, published_date)
            VALUES
            (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title), (self.author_id), (self.total_pages),
                       (self.rating), (self.published_date))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all_books[self.id] = self

    def update(self):
        sql = """
            UPDATE books
            SET
            title = ?,
            author_id = ?,
            total_pages = ?,
            rating = ?,
            published_date = ?
        """
        CURSOR.execute(sql, (self.title), (self.author_id),
                       (self.total_pages), (self.rating), (self.published_date))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM books
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all_books[self.id]
        self.id = None

    @classmethod
    def create(cls, title, author_id, total_pages, rating, published_date):
        book = cls(title, author_id, total_pages, rating, published_date)
        book.save()
        return book
