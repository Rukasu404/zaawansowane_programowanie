class Library:
    def __init__(self, city: str, street: str, zip_code: str,
                 open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return (f"Informacje dotyczące biblioteki:\n"
                f"Miasto: {self.city}\n"
                f"Ulica: {self.street}\n"
                f"Kod pocztowy: {self.zip_code}\n"
                f"Godziny otwarcia: {self.open_hours}\n"
                f"Numer telefonu: {self.phone}\n")