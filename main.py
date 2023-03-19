print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")

try:
    print(0/0)
except NameError as err1:
    print(f"ти какашка код не можиш писать, помилка {err1}")
except:
    print("Непонятно")
else:
    print('im else')
finally:
    print("Конец проверки")
print("Всо")

def checker(var_1):
    if type(var_1) != str:
        raise TypeError("кукиш з маслом")
    else:
        return var_1


class BuildingError(Exception):
    def __str__(self):
        return f"House cannot be build"


def check_material(amount_material, limit_value):
    if(amount_material > limit_value):
        return "enough material"
    else:
        raise BuildingError(amount_material)


check_material(112, 100)
check_material(75, 112)


# var = 10
# var2 = "hello"
# print(checker(var))
# print(checker(var2))

