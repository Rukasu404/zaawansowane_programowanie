from magazine import Student

a = Student.Student("s1", [2, 4, 6, 6, 6])
b = Student.Student("s2", [1, 1, 1, 1, 2, 3])

is_passed = a.is_passed()
is_not_passed = b.is_passed()
