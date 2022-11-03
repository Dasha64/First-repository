import requests
import random
#
# Отримуємо в консоль общу інформацію по модулю
# print(help(random))


def first_func():
    pass

class Human:
    pass

rq = requests
first_f = first_func
nick = Human
# можна дізнатися про ім'я об'єктів
print(rq.__name__)
print(first_f.__name__)
print(nick.__name__)
# можна дізнатися тип об'єкта
print(type(rq))
print(type(first_f))
print(type(nick))

# можна дізнатися про атрибути і методи
name = ""
for method in dir(rq):
    print(method)

print("hasattr")
print(hasattr(name, "reverse"))
print(hasattr(name, "index"))

print("getattr - ")
print(getattr(name, "index"))

# callable() відповідає на питання чи можна викликати об'єкт

print(callable(name))
print(callable(first_func))

class A:
    pass


class B(A):
    pass

class C:
    pass

print(issubclass(B, A))

obj1 = B()
print(isinstance(obj1, A))
print(isinstance(obj1, B))
print(isinstance(obj1, C))

import inspect

print(inspect.ismodule(rq))
print(inspect.ismodule(obj1))
print(inspect.isclass(requests))

print(inspect.getmodule(requests.get))

import sys

print(sys.executable)
print(sys.version)

print(sys.platform)