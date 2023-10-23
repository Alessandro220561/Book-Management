from models.__init__ import CURSOR, CONN
from models.author import Author
import datetime


class Book:

    all_books = {}

    def __init__(self, title, pages, rating, published_date, author_id, id=None):
        self.title = title
        self.author_id = author_id
        self.pages = pages
        self.rating = rating
        self.published_date = published_date
        self.id = id

    def __repr__(self):
        return (
            f"<<<Book {self.id}: {self.title}, {self.pages}, {self.rating}, {self.published_date}, " +
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
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if isinstance(pages, int):
            self._pages = pages
        else:
            raise ValueError(
                "The book's page count must be an integer"
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
            pages INT,
            rating INT,
            published_date TEXT,
            author_id INT,
            FOREIGN KEY (author_id) REFERENCES authors(id)
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
            (title, author_id, pages, rating, published_date)
            VALUES
            (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.author_id, self.pages,
                       self.rating, self.published_date))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all_books[self.id] = self

    def update(self):
        sql = """
            UPDATE books
            SET
            title = ?,
            author_id = ?,
            pages = ?,
            rating = ?,
            published_date = ?
            WHERE
            id = ?
        """
        CURSOR.execute(sql, (self.title, self.author_id,
                       self.pages, self.rating, self.published_date, self.id))
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
    def create(cls, title, pages, rating, published_date, author_id):
        book = cls(title, pages, rating, published_date, author_id)
        book.save()
        return book

    @classmethod
    def instance_from_db(cls, row):
        book = cls.all_books.get(row[0])
        if book:
            book.title = row[1]
            book.pages = int(row[2])
            book.rating = int(row[3])
            book.published_date = row[4]
            book.author_id = row[5]
        else:
            book = cls(row[1], row[2], row[3], row[4], row[5])
            book.id = row[0]
            cls.all_books[book.id] = book
        return book

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM books
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def get_books_by_author(cls, author_id):
        sql = """
            SELECT * FROM books
            WHERE author_id = ?
        """
        rows = CURSOR.execute(sql, (author_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
