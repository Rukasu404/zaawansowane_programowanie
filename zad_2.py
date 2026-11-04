from datetime import date
from zad_1 import Student
from magazine import Book, Employee, Library, Order

lib1 = Library.Library("Czeladź", "Reymonta", "41-250",
               "7.00 - 8.00", "+48 213 742 241")
lib2 = Library.Library("Katowice", "1 Maja", "40-001",
               "7.00 - 8.00", "+48 213 202 241")

b1 = Book.Book(lib1, date(1993, 1, 1), "Andrzej", "Sapkowski", 332)
b2 = Book.Book(lib1, date(1961, 6, 1), "Stanisław", "Lem", 204)
b3 = Book.Book(lib2, date(1834, 6, 28), "Adam", "Mickiewicz", 340)
b4 = Book.Book(lib2, date(1884, 3, 2), "Henryk", "Sienkiewicz", 610)
b5 = Book.Book(lib1, date(1949, 6, 8), "George", "Orwell", 328)

e1 = Employee.Employee("Anna", "Kowalska", date(2015, 3, 1),
              date(1985, 7, 12), "Czeladź", "Szkolna 5", "41-250",
              "+48 501 234 567")
e2 = Employee.Employee("Piotr", "Nowak", date(2019, 9, 16),
              date(1992, 11, 3), "Katowice", "Mariacka 10", "40-014",
              "+48 602 345 678")
e3 = Employee.Employee("Marta", "Wiśniewska", date(2022, 1, 10),
              date(1998, 2, 25), "Sosnowiec", "Warszawska 3",
              "41-200", "+48 703 456 789")

s1 = Student.Student("Kasia", [80, 75, 90, 60])
s2 = Student.Student("Tomek", [40, 55, 30, 45])
s3 = Student.Student("Ola", [65, 70, 50, 85])

o1 = Order.Order(e1, s1, [b1, b2, b5], date(2026, 10, 20))
o2 = Order.Order(e2, s3, [b3, b4], date(2026, 10, 24))

print(o1)
print(o2)
