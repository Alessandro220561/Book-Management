import sqlite3

CONN = sqlite3.connect('book_manager.db')
CURSOR = CONN.cursor()
