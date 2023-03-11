import os
from mysql import connector


class DatabaseSetup:

    def __init__(self):
        self.db = connector.connect(
            user="root",
            password="B46usg30!mbK",
            host="localhost",
            database = "book_management"
        )
        self.mycursor = self.db.cursor()


    def create_tables(self):
        self.mycursor.execute("""
                CREATE TABLE CreditCard(
                creditcard_id INT PRIMARY KEY AUTO_INCREMENT,
                card_number BIGINT NOT NULL,
                cvc_code SMALLINT)""")
        self.mycursor.execute("""
                CREATE TABLE WishList(
                wishlist_id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                UNIQUE (name))""")
        self.mycursor.execute("""
                CREATE TABLE ShoppingCart(
                shoppingcart_id INT PRIMARY KEY AUTO_INCREMENT)""")
        self.mycursor.execute("""
                CREATE TABLE User(
                user_id INT PRIMARY KEY AUTO_INCREMENT,
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                name VARCHAR(255),
                email VARCHAR(255),
                home_address VARCHAR(255),
                creditcard_id INT,
                FOREIGN KEY (creditcard_id) REFERENCES CreditCard(creditcard_id),
                UNIQUE (username))""")
        self.mycursor.execute("""
                CREATE TABLE Comment(
                comment_id INT PRIMARY KEY AUTO_INCREMENT,
                content LONGTEXT NOT NULL,
                date DATE NOT NULL)""")
        self.mycursor.execute("""
                CREATE TABLE Rating(
                rating_id INT PRIMARY KEY AUTO_INCREMENT,
                score SMALLINT NOT NULL,
                date DATE NOT NULL)""")
        self.mycursor.execute("""
                CREATE TABLE Author(
                author_id INT PRIMARY KEY AUTO_INCREMENT,
                firstname VARCHAR(255) NOT NULL,
                lastname VARCHAR(255) NOT NULL,
                biography LONGTEXT NOT NULL,
                publisher VARCHAR(255) NOT NULL)""")
        self.mycursor.execute("""
                CREATE TABLE Book(
                book_id INT PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(255) NOT NULL,
                genre VARCHAR(255) NOT NULL,
                description LONGTEXT NOT NULL,
                publisher VARCHAR(255) NOT NULL,
                published_date DATE NOT NULL,
                isbn VARCHAR(20) NOT NULL,
                price DECIMAL(10,2) NOT NULL,
                sales BIGINT NOT NULL,
                author_id INT NOT NULL,
                FOREIGN KEY (author_id) REFERENCES Author(author_id))""")
        
        #add foreign keys
        self.mycursor.execute("ALTER TABLE Wishlist ADD COLUMN book_id INT NOT NULL AFTER name")
        self.mycursor.execute("ALTER TABLE Wishlist ADD FOREIGN KEY (book_id) REFERENCES Book(book_id)")
        self.mycursor.execute("ALTER TABLE Wishlist ADD COLUMN user_id INT NOT NULL AFTER name")
        self.mycursor.execute("ALTER TABLE Wishlist ADD FOREIGN KEY (user_id) REFERENCES User(user_id)")
        self.mycursor.execute("ALTER TABLE ShoppingCart ADD COLUMN book_id INT NOT NULL AFTER shoppingcart_id")
        self.mycursor.execute("ALTER TABLE ShoppingCart ADD FOREIGN KEY (book_id) REFERENCES Book(book_id)")
        self.mycursor.execute("ALTER TABLE ShoppingCart ADD COLUMN user_id INT NOT NULL AFTER shoppingcart_id")
        self.mycursor.execute("ALTER TABLE ShoppingCart ADD FOREIGN KEY (user_id) REFERENCES User(user_id)")
        self.mycursor.execute("ALTER TABLE Comment ADD COLUMN user_id INT NOT NULL AFTER content")
        self.mycursor.execute("ALTER TABLE Comment ADD FOREIGN KEY (user_id) REFERENCES User(user_id)")
        self.mycursor.execute("ALTER TABLE Comment ADD COLUMN book_id INT NOT NULL AFTER content")
        self.mycursor.execute("ALTER TABLE Comment ADD FOREIGN KEY (book_id) REFERENCES Book(book_id)")
        self.mycursor.execute("ALTER TABLE Rating ADD COLUMN user_id INT NOT NULL AFTER score")
        self.mycursor.execute("ALTER TABLE Rating ADD FOREIGN KEY (user_id) REFERENCES User(user_id)")
        self.mycursor.execute("ALTER TABLE Rating ADD COLUMN book_id INT NOT NULL AFTER score")
        self.mycursor.execute("ALTER TABLE Rating ADD FOREIGN KEY (book_id) REFERENCES Book(book_id)")


    def insert_author(self, firstname, lastname, biography, publisher):
        self.mycursor.execute("""INSERT INTO Author (firstname, lastname, biography, publisher) 
                VALUES (%s, %s, %s, %s)""", (firstname, lastname, biography, publisher))
        self.db.commit()


    def insert_book(self, title, genre, desc, publisher, published_date, isbn, price, sales, author_id):
        self.mycursor.execute("""INSERT INTO Book (title, genre, description, publisher, published_date, isbn, price, sales, author_id) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (title, genre, desc, publisher, published_date, isbn, price, sales, author_id))
        self.db.commit()


    def insert_admin(self, username, password):
        self.mycursor.execute("""INSERT INTO User (username, password)
                VALUES (%s, %s)""", (username, password))
        self.db.commit()


    def insert_user(self, username, password, name, email, home_address):
        self.mycursor.execute("""INSERT INTO User (username, password, name, email, home_address)
                VALUES (%s, %s, %s, %s, %s)""", (username, password, name, email, home_address))
        self.db.commit()


    def load_authors_table(self):
        db.insert_author("John", "Tolkien", "A writer", "HarperCollins")
        db.insert_author("George", "Orewell", "A writer", "HarperCollins")
        db.insert_author("Frank", "Herbert", "A writer", "Chilton Books")
        db.insert_author("Paulo", "Coelho", "A writer", "HarperCollins")
        db.insert_author("Harper", "Lee", "A writer", "J. B. Lippincott & Co.")
        db.insert_author("Stephen", "King", "A writer", "Simon & Schuster")
        db.insert_author("J.D.", "Salinger", "A writer", "Little, Brown and Company")
        db.insert_author("S.E.", "Hinton", "A writer", "Penguin Books")
        db.insert_author("George", "Martin", "A writer", "Bantam Spectra")


    def load_books_table(self):
        db.insert_book("The Lord of the Rings", "Fantasy", "A book about a ring", "HarperCollins", "1954-07-29", "978-0618260300", 29.99, 600000000, 1)
        db.insert_book("1984", "Dystopian", "A book about a dystopian future", "HarperCollins", "1949-06-08", "978-0451524935", 15.99, 100000000, 2)
        db.insert_book("Dune", "Science Fiction", "A book about a desert planet", "Chilton Books", "1965-06-01", "978-0441172719", 9.99, 20000000, 3)
        db.insert_book("The Alchemist", "Fantasy", "A book about personal growth", "HarperCollins", "1988-10-05", "978-0061122415", 20.99, 150000000, 4)
        db.insert_book("To Kill a Mockingbird", "Southern Gothic", "A book about morality", "J. B. Lippincott & Co.", "1960-07-11", "978-0446310789", 11.86, 40000000, 5)
        db.insert_book("It", "Horror", "A book about a scary clown", "Simon & Schuster", "1986-09-15", "978-1501142970", 16.99, 400000000, 6)
        db.insert_book("The Shining", "Horror", "A book about a haunted hotel", "Simon & Schuster", "1977-01-28", "978-0307743657", 16.99, 700000, 6)
        db.insert_book("11/22/63", "Horror", "A book about a time traveler", "Simon & Schuster", "2011-11-08", "978-1451648546", 16.99, 10000000, 6)
        db.insert_book("The Catcher in the Rye", "Comming of Age", "A book about struggles growing up", "Little, Brown and Company", "1951-07-16", "978-0316769488", 8.93, 65000000, 7)
        db.insert_book("The Outsiders", "Coming of Age", "A book about a gang", "Little, Brown and Company", "1967-01-01", "978-0142407332", 8.46, 8000000, 8)
        db.insert_book("A Game of Thrones", "Fantasy", "A book about a war", "Bantam Spectra", "1996-08-01", "978-0553593716", 9.99, 90000000, 9)


    def load_users_table(self):
        db.insert_admin("admin", "admin")
        db.insert_user("someone123", "password123", "someone", "someone@gmail.com", "1234 Main St")

    
if __name__ == "__main__":
    db = DatabaseSetup()
    db.create_tables()
    db.load_authors_table()
    db.load_books_table()
    db.load_users_table()
