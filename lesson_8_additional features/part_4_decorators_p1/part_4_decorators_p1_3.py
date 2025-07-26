"""Декоратор @takes_numbers
Реализуйте класс декоратор @takes_numbers, который проверяет, что все аргументы, передаваемые в декорируемую функцию, принадлежат типам int или float. Если хотя бы один аргумент принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:

Аргументы должны принадлежать типам int или float
Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @takes_numbers, но не код, вызывающий его."""


import functools
from itertools import chain


class  takes_numbers:
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        if all(isinstance(arg, (int, float)) for arg in chain(args, kwargs.values())):
            return self.func(*args, **kwargs)
        else:
            raise TypeError('Аргументы должны принадлежать типам int или float')


@takes_numbers
def mul(a, b):
    return a * b


print(mul(1, 2))
print(mul(1, 2.5))
print(mul(1.5, 2))
print(mul(1.5, 2.5))
