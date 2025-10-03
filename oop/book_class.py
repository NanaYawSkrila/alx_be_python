class Book:
    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize Book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor prints message when book is deleted"""
        print(f"Deleting {self.title}")

    def __str__(self):
        """String representation for user-friendly output"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation to recreate the Book instance"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
