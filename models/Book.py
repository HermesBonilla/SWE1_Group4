class Book:
    def __init__(self, id=None, title=None, genre=None, 
                description=None, publisher=None, publish_date=None, 
                isbn=None, price=None, sales=None, author_id=None):
        self.id = id
        self.title = title
        self.genre = genre
        self.description = description
        self.publisher = publisher
        self.publish_date = publish_date
        self.isbn = isbn
        self.price = price
        self.sales = sales
        self.author_id = author_id

    # Serialize the object to a dictionary
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'description': self.description,
            'publisher': self.publisher,
            'publish_date': self.publish_date,
            'isbn': self.isbn,
            'price': self.price,
            'sales': self.sales,
            'author_id': self.author_id,
        }
    
    def serialize_discount(self):
        return {
            'title': self.title,
            'publisher': self.publisher,
            'price': self.price,
        }