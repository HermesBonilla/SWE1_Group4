from mysql import connector
from models.Book import Book
from models.Rating import Rating

class BroswingAndSortingDB:
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
    

    def list_by_rating(self, rating):
        queryset = []
        self._mycursor.execute("""
        SELECT Book.title, User.username, Rating.score 
        FROM Rating 
        LEFT JOIN Book ON Rating.book_id=Book.book_id 
        RIGHT JOIN User ON Rating.user_id=User.user_id 
        WHERE score >= %s 
        ORDER BY score DESC;
        """, (rating,))
        for row in self._mycursor:
            user_rating = Rating(row[0], row[1], row[2])
            queryset.append(user_rating.serialize())
        return queryset
    

    # write a method to discount books by publisher
    def discount_by_publisher(self, publisher, discount):
        queryset = []
        self._mycursor.execute("""
        UPDATE Book SET price = price - (price * %s) WHERE publisher = %s
        """, (discount, publisher))
        self._db.commit()
        self._mycursor.execute("""
        SELECT title, publisher, price FROM Book WHERE publisher = %s
        """, (publisher,))
        for row in self._mycursor:
            print(row)
            book = Book()
            book.title=row[0]
            book.publisher=row[1]
            book.price=row[2]
            queryset.append(book.serialize_discount())
        return queryset


if __name__ == "__main__":
    db = BroswingAndSortingDB()