# Task 3: Student Result System
# Design a Student Result System using encapsulation.
# Requirements:
# 1. Private attribute __marks
# 2. Methods: set_marks(), get_marks(), calculate_grade()
# 3. Create at least two student objects

class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0
    def set_marks(self, marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def calculate_grade(self):
        if self.__marks >= 80:
            return "A"
        elif self.__marks >= 60:
            return "B"
        elif self.__marks >= 40:
            return "C"
        else:
            return "F"

s1 = Student("obaid")
s2 = Student("jawas")
s1.set_marks(80)
s2.set_marks(50)

print(s1.name, s1.get_marks(), s1.calculate_grade())
print(s2.name, s2.get_marks(), s2.calculate_grade())
