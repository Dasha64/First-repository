import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("Time to study!")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Rest time!")
        self.progress -= 0.1
        self.gladness += 5

    def is_alive(self):
        if self.progress < -0.5:
            print("Good buy Univer ")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False

    def endOfDay(self):
        print("Gladness: ",self.gladness)
        print("Progress: ",self.progress)

    def live(self,day):
        print('Day',day,'of Students life')
        num = random.randint(1,3)
        if num == 1:
            self.to_chill()
        if num == 2:
            self.to_study()
        if num == 3:
            self.to_sleep()
        self.endOfDay()
        self.is_alive()


class Gruppa:

    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self,Student):
        self.students.append(Student)


    def printStudents(self):
        if self.students != []:
            print("Name of the group: ", self.name)
            for ps in self.students:
                print("Name of student: ", ps.name)
            else:
                print("No students in the group")

    def  delStudent(self, delStudents):
        try:
            self.students.remove(delStudents)
        except:
            print("There are no", delStudents.name,"in this grupp",self.name)

    def simulateGrupp(self):
        for st in self.students:
            for day in range(365):
                if st.alive == False:
                    self.delStudent(st)
                    break
                st.live()

gruppa1 = Gruppa("550")
jim = Student("Jim")
max = Student('Max')
nick = Student("Nick")
gruppa1.add_student(nick)
gruppa1.add_student(jim)
gruppa1.add_student(max)

gruppa1.printStudents()


# for day in range(365):
#     if nick.alive == False:
#         break
#     nick.live(day)
