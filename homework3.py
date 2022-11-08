import random

class Animal:
    def __init__(self, name, breed):
        self.breed = breed
        self.name = name
        self.satiety = 80


    def eat(self):
        self.satiety += 20
        print("Satiety -",self.satiety)


class Zoo():
    def __init__(self, name):
        self.name = name
        self.satiety = 80
        self.count_food = 150
        self.Animals = []

    def add_animal(self, add_animal):
        self.Animals.append(add_animal)

    def del_animal(self, del_animal):
        if self.satiety <= 0:
            self.Animals.remove(del_animal)

    def feed_animals(self):
        num1 = random.randint(1,35)
        self.satiety += num1
        print("Satiety -", self.satiety)

    def get_info(self):
        if self.Animals != []:
            print("Name of the Zoo -", self.name)
            for an in self.Animals:
                print("Name of the animal:", an.name)
                zoo = Zoo("MegaZoo")
                zoo.feed_animals()
        else:
            print("No animals in the Zoo!")


zoo = Zoo("MegaZoo")
bear = Zoo("Bear")
sandcat = Zoo("SandCat")
wolf = Zoo("Wolf")
lione = Zoo("Lion")
leopard = Zoo("Leopard")
fox = Zoo("Fox")


zoo.add_animal(bear)
zoo.add_animal(sandcat)
zoo.add_animal(wolf)
zoo.add_animal(lione)
zoo.add_animal(leopard)
zoo.add_animal(fox)

zoo.get_info()