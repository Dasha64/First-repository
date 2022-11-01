# базовий клас
class Animal:
    def __init__(self,name, ves, poroda):
        self.name = name
        self.ves = ves
        self.poroda = poroda

    def golos(self):
        pass
    def show_info(self):
        print("Name:", self.name,'Poroda:', self.poroda,'Ves: ', self.ves)

# дочірній клас створений на основі базового
class Dog(Animal):
    def __init__(self, name, ves, poroda):
        super().__init__(name, ves, poroda)

    def golos(self):
        print("Gav gav")

myDog = Dog('Bobik', 20, "Staff")
myDog.show_info()
myDog.golos()

class Cat(Animal):
    def __init__(self, name, ves, poroda):
        super().__init__(name, ves, poroda)

    def golos(self):
        print("Mau mau")

myCat = Cat('Firestar', 6, "clancat")
myCat.show_info()
myCat.golos()

class Catdog(Cat, Dog):
    pass

catDog = Catdog('bill', 40, 'catdog')
catDog.show_info()




