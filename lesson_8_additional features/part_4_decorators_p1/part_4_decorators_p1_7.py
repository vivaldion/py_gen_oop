"""
Декоратор @type_check
Реализуйте класс декоратор @type_check, который принимает один аргумент:

types — список, элементами которого являются типы данных
Декоратор должен проверять, что типы всех позиционных аргументов, передаваемых в декорируемую функцию, полностью сопоставляются с типами из списка types, то есть типом первого аргумента является первый элемент списка types, типом второго аргумента — второй элемент списка types, и так далее. Если данное условие не выполняется, должно быть возбуждено исключение TypeError.

Если количество позиционных аргументов больше, чем количество элементов в списке types, то не сопоставляемые аргументы не должны учитываться при проверке. Если количество позиционных аргументов меньше чем количество элементов в списке types, то не сопоставляемые типы из списка types не должны учитываться при проверке.

Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, с
"""

import functools
from itertools import starmap

class type_check:
    def __init__(self, types):
        self.types = types


    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            fst = args[:len(self.types)]
            snd = self.types[:len(args)]
            if all(starmap(lambda x, y: isinstance(x, y) ,zip(fst, snd))):
                return func(*args, **kwargs)
            raise TypeError

        return wrapper


@type_check([int, int])
def add(a, b):
    return a + b

print(add(1, 2))