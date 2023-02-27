from mysql import connector

class BookRepo:

    def __init__(self):
        self.db = connector.connect(
            user="root",
            password="B46usg30!mbK",
            host="localhost",
            database = "book_management"
        )
        self.mycursor = self.db.cursor()


    def list_by_genre(self, genre):
        queryset = []
        self.mycursor.execute("""
        SELECT * FROM Book WHERE genre = %s
        """, (genre,))
        for row in self.mycursor:
            queryset.append({
                'id': row[0],
                'title': row[1],
                'genre': row[2],
                'description': row[3],
                'publisher': row[4],
                'publish_date': row[5].isoformat(),
                'isbn': row[6],
                'price': row[7],
                'sales': row[8],
                'author_id': row[9],
            })
        return queryset
    

    def list_best_sellers(self):
        queryset = []
        self.mycursor.execute("""
        SELECT * FROM Book ORDER BY sales DESC LIMIT 10
        """)
        for row in self.mycursor:
            queryset.append({
                'id': row[0],
                'title': row[1],
                'genre': row[2],
                'description': row[3],
                'publisher': row[4],
                'publish_date': row[5].isoformat(),
                'isbn': row[6],
                'price': row[7],
                'sales': row[8],
                'author_id': row[9],
            })
        return queryset
    

if __name__ == "__main__":
    db = BookRepo()
    print(db.list_by_genre('Fantasy'))