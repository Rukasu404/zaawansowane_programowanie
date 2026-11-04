from datetime import date

class Employee:
    def __init__(
            self,
            first_name: str,
            last_name: str,
            hire_date: date,
            birth_date: date,
            city: str,
            street: str,
            zip_code: str,
            phone: str,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return (f"Dane pracownika:\n"
                f"Imię: {self.first_name}\n"
                f"Nazwisko: {self.last_name}\n"
                f"Data urdzoenia: {self.birth_date}\n"
                f"Zamieszkałe miasto: {self.city}\n"
                f"Ulica: {self.street}\n"
                f"Kod pocztowy: {self.street}\n"
                f"Numer telefonu: {self.phone}\n")
