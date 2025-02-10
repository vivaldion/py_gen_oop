class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book('{title}', '{author}', {year})"

    def __repr__():
        return f'{title} ({author}, {year})'