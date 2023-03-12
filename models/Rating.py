class Rating:
    def __init__(self, title=None, username=None, score=None):
        self.book_title = title
        self.username = username
        self.score = score
    
    # Serialize the object to a dictionary
    def serialize(self):
        return {
            'book_title': self.book_title,
            'username': self.username,
            'score': self.score
        }
