class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        srednia = sum(self.marks)/len(self.marks)
        if srednia > 3:
            print("passed")
            return True
        else:
            print("not passed")
            return False


a = Student("s1", [2, 4, 6, 6, 6])
b = Student("s2", [1, 1, 1, 1, 2, 3])

is_passed = a.is_passed()
is_not_passed = b.is_passed()
