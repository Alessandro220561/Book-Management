from models.__init__ import CURSOR, CONN


class Author:

    all_authors = {}

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"<<<Author {self.id}: {self.name}>>>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "<<< Author's name must be a non-empty string >>>"
            )

    @classmethod
    def create(self):
        sql = """
            CREATE TABLE IF NOT EXISTS authors
            (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit

    @classmethod
    def drop_table(self):
        sql = """
            DROP TABLE IF EXISTS authors
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO authors
            (name)
            VALUES
            (?)
        """
        CURSOR.execute(sql, (self.name),)
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all_authors[self.id] = self

    def update(self):
        sql = """
            UPDATE authors
            SET 
            name = ?
            WHERE
            id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM authors
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all_authors[self.id]
        self.id = None

    @classmethod
    def create(cls, name):
        author = cls(name)
        author.save()
        return author

    def instance_from_db(cls, row):
        author = cls.all_authors.get(row[0])
        if author:
            author.name = row[1]
        else:
            author = cls(row[1])
            author.id = row[0]
            cls.all_authors[author.id] = author
        return author

    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM authors
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM authors
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
