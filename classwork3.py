import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
        self.day = 0

    def to_study(self):
        # print("Time to study!")
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        # print("time to sleep")
        self.gladness += 3

    def to_chill(self):
        # print("Rest time!")
        self.progress -= 0.1
        self.gladness += 5

    def is_alive(self):
        if self.progress < -0.5:
            print("Good buy Univer ")
            self.alive = False
        elif self.gladness <= 0:
            # print("Depression...")
            self.alive = False

    def endOfDay(self):
        print("Gladness: ", self.gladness)
        print("Progress: ", self.progress)

    def showResult(self):
        print("Day", str(self.day), " of ", self.name, "life")
        self.endOfDay()

    def live(self):
        self.day += 1
        num = random.randint(1, 3)
        if num == 1:
            self.to_study()
        elif num == 2:
            self.to_chill()
        elif num == 3:
            self.to_sleep()

        self.is_alive()


class Gruppa:
    def __init__(self, name):
        self.name = name
        self.students = []

    #     1 реализовать метод добавления студента в группу
    def addStudent(self, newStudent):
        self.students.append(newStudent)

    #     2 реализовать метод показа в консоль списка студентов этой группы
    def printStudents(self):
        if self.students != []:
            print("Name of the grupp: ", self.name)
            for st in self.students:
                print(st.name)
        else:
            print("No students in this grupp!")

    def delStudent(self, delStudent):
        try:
            self.students.remove(delStudent)
        except:
            print("There are no", delStudent.name, "in this grupp ", self.name)

 #     3 реализовать метод симуляции жизни группы
    def simulateGrupp(self):
        for st in self.students:
            for day in range(365):
                if st.alive == False:
                    self.delStudent(st)
                    break
                st.live()

            st.showResult()


nick = Student("nick")
bill = Student("bill")

gruppa1 = Gruppa("vsha17_01")

gruppa1.addStudent(nick)
gruppa1.addStudent(bill)
# gruppa1.delStudent(nick)

gruppa1.printStudents()

gruppa1.simulateGrupp()


