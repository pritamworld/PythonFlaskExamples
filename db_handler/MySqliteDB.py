import sqlite3

from flask import jsonify


# https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

class MySqliteDatabase:
    def getAll(self):
        conn = sqlite3.connect('db/books.db')
        conn.row_factory = self.dict_factory
        cur = conn.cursor()
        all_books = cur.execute('SELECT * FROM books;').fetchall()

        return jsonify(all_books)

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
