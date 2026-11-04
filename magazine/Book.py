from magazine import Library
from datetime import date

class Book:
    def __init__(
            self,
            library: Library,
            publication_date: date,
            author_name: str,
            author_surname: str,
            number_of_pages: int,
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return (f"Dane dotyczące książki:\n"
                f"Biblioteka: {self.library}\n"
                f"Imię autora: {self.author_name}\n"
                f"Nazwisko autora: {self.author_surname}\n"
                f"Liczba stron: {self.number_of_pages}\n")