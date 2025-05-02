class Book:
    def __init__(self, title, author, year, rating=0, genre, notes, id):

        self.title = title
        self.author = author
        self.year = year
        self.rating = rating
        self.genre = genre
        self.notes = notes
        self.id = id

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "rating": self.rating,
            "genre": self.genre,
            "notes": self.notes
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            title = data.get("title", ""),
            author = data.get("author", ""),
            year = data.get("year", ""),
            rating = data.get("rating", ""),
            genre = data.get("genre", ""),
            notes = data.get("notes", "")
        )