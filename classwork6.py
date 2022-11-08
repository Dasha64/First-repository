
try:
    try:
        print("Start code")
        print(error)
        print("end code")
    except NameError:
        print("Wrong syntax")
    print("Test1")
    print(10/0)
    print("Test2")
except (NameError, ZeroDivisionError) as error:
    print("Have some", error)
except ZeroDivisionError:
    print("Zero devision error!")
else:
    print("work else")
finally:
    print("Work finally")

print("after try")

def checker(var1):
    if type(var1) != str:
        # raise вибрасує ексепшен
        raise TypeError("Sorry we need a str type var")
    else:
        return var1

checker("10")

class BuildingError(Exception):
    def __str__(self):
        return "materials!"


def checkMaterial(amountOfMaterial, LimitValue):
    if amountOfMaterial > LimitValue:
        return "good"
    else:
        raise BuildingError(amountOfMaterial)


try:
    checkMaterial(200, 300)
except BuildingError as error:
    print("Buy some",error)


import warnings

warnings.warn("WARNING! SOMETHING! ERROR!", SyntaxWarning)




