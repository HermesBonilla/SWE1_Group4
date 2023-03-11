from mysql import connector
from Book import Book

class BookRepo:

    def __init__(self):
        self._db = connector.connect(
            user="root",
            password="B46usg30!mbK",
            host="localhost",
            database = "book_management"
        )
        self._mycursor = self._db.cursor()


    def list_by_genre(self, genre):
        queryset = []
        self._mycursor.execute("""
        SELECT * FROM Book WHERE genre = %s
        """, (genre,))
        for row in self._mycursor:
            book = Book(row[0], row[1], row[2], row[3], row[4], row[5].isoformat(), 
                        row[6], row[7], row[8], row[9])
            queryset.append(book.serialize())
        return queryset
    

    def list_best_sellers(self):
        queryset = []
        self._mycursor.execute("""
        SELECT * FROM Book ORDER BY sales DESC LIMIT 10
        """)
        for row in self._mycursor:
            book = Book(row[0], row[1], row[2], row[3], row[4], row[5].isoformat(), 
                        row[6], row[7], row[8], row[9])
            queryset.append(book.serialize())
        return queryset

    

if __name__ == "__main__":
    db = BookRepo()