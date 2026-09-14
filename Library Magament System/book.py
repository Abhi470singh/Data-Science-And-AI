class Book:
    
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["book_id"],
            data["title"],
            data["author"]
        )
        book.available = data["available"]
        return book
    


















