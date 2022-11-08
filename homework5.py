import colorama

print(help(colorama))
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
def test_func():
    pass

class Animal:
    pass

cl = colorama
test_f = test_func()
giraffe = Animal

print(cl.__name__)
print(giraffe.__name__)

print(type(cl))

name = ""
for method in dir(cl):
    print(method)


print(callable(giraffe))
print(callable(test_func()))

class P:
    pass


class F(P):
    pass

class M:
    pass

print(issubclass(F, P))

object2 = F()
print(isinstance(obj1, P))
print(isinstance(obj1, F))
print(isinstance(obj1, M))

