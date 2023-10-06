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
