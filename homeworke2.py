# Симулятор кота
import random

class Cat:
    def __init__(self, name = 'Вогнезір'):
        self.name = name
        self.famine = 50
        self.gladness = 50
        self.leadership = True
        self.alive = True
        self.clan_service = 50
        self.wound =0

    def to_catchm(self):
        print("Зловив. Час пополювати")
        self.gladness += 5
        self.famine -= 20
        self.clan_service += 15

    def sleep(self):
        print('Час поспати')
        self.famine += 10
        self.gladness += 5

    def did_not_catch(self):
        print('Не пощастило у полюванні')
        self.famine += 15
        self.gladness -= 10
        self.clan_service -= 20

    def eat(self):
        print('Час поїсти')
        self.famine -= 20
        self.gladness += 15

    def eve_of_the_clan(self):
        print("Віче клану. Я", self.name, 'провідник Громового....')
        self.clan_service += 7
        self.gladness += 5

    def gathering(self):
        print('Зборище!')
        self.famine += 15
        self.clan_service += 30

    def battle_for_territory(self):
        print("Перемога. Забиирайтеся з нашої землі!!! І ніколи не повертайтеся!!!")
        self.famine += 10
        self.gladness +=40
        self.wound += 10
        self.clan_service += 50

    def lostbattle(self):
        print('Поразка. Громовий клане, відступаємо!')
        self.famine += 10
        self.gladness -=40
        self.wound += 20
        self.clan_service -= 10

    def education(self):
        print('Гайда на тренування')
        self.famine += 15
        self.gladness += 15
        self.clan_service += 25

    def is_alive(self):
        if self.famine > 100:
            self.alive = False
            print('Голод забрав одне з життів нашого провідника.')
        if self.wound > 95:
            self.alive = False
            print("Бій забрав одне з життів нашого провідника")
        elif self.clan_service < 10:
            print("Я поганий провідник")
            self.leadership = False


    def end_of_day(self):
        print(self.name)
        print("Голод:", self.famine)
        print("Щастя:", self.gladness)
        print("Провідництво:", self.leadership)
        print("Живий:", self.alive)
        print("Служіння клану:", self.clan_service)
        print("Поранення:", self.wound)
        print("--------------------------------------------------------------------------")

    def live(self,day):
        print('День',day,'з життя Вогнезора')
        num = random.randint(1,9)
        if num == 1:
            self.to_catchm()
        if num == 2:
            self.sleep()
        if num == 3:
            self.did_not_catch()
        if num == 4:
            self.eat()
        if num == 5:
            self.eve_of_the_clan()
        if num == 6:
            self.gathering()
        if num == 7:
            self.battle_for_territory()
        if num == 8:
            self.lostbattle()
        if num == 9:
            self.education()
        self.end_of_day()
        self.is_alive()

name = Cat("Вогнезір")
for day in range(365):
    if name.alive == False:
        break
    elif name.clan_service == False:
        break
    name.live(day)


