from models.__init__ import CURSOR, CONN

class Author:

    all_authors = {}

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __repr__(self):
        return f"<<<Author {self.id}: {self.name}>>>"
        