
class Student:
    count_students = 0
    def __init__(self, name, height):
        self.name = name
        self.height = height
        Student.count_students += 1

    def printer(self):
        print("Name: ", self.name, 'Height', self.height)

    def set_name(self, newName):
        self.name = newName

first_student = Student("Володимир Зеленський", 180)
first_student.printer()

first_student.set_name("Валерій Залужний")
first_student.printer()

second_student = Student("Борис Джонсон", 170)
second_student.printer()
print("Кількість студентів -",Student.count_students)