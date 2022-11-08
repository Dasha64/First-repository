

# 1

class Human:
    def __init__(self):
        pass


class Brains(Human):
    pass


class Heart(Human):
    pass


class Legs(Human):
    pass





# 2

class Shape:
    def __init__(self, color, x, y):
        self.color = color
        self.numberPi = 3.14
        self.x = y
        self.y = x


class rectangle(Shape):
    def set_info(self):
        self.color = input("Введіть колір будь ласка - ")
        self.x = int(input("Введіть скільки дорівнює x = "))
        self.y = int(input('Введіть скільки дорівнює y = '))
        print("Маємо такий прямокутник:")
        print("Колір -", self.color)
        print('Периметр прямокутника =',2 * (self.x + self.y))
        print("Площа прямокутника =", self.x*self.y)

    def draw_rectangle(self):
        for i in range(self.y):
            print("*" * self.x)


rectangle.set_info(Shape)
rectangle.draw_rectangle(Shape)

