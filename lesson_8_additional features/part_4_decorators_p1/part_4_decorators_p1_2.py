"""
Реализуйте класс декоратор @limited_calls, который принимает один аргумент:

n — целое число
Декоратор должен разрешать вызывать декорируемую функцию n раз. Если декорируемая функция вызывается более n раз, должно быть возбуждено исключение MaxCallsException с текстом:

Превышено допустимое количество вызовов
Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @limited_calls, но не код, вызывающий его.
"""


import functools


class MaxCallsException(Exception):
    pass


class limited_calls:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.n == 0:
                raise MaxCallsException('Превышено допустимое количество вызовов')
            self.n -= 1
            return func(*args, **kwargs)

        return wrapper



@limited_calls(3)
def add(a, b):
    return a + b


print(add(1, 2))
print(add(3, 4))
print(add(5, 6))

try:
    print(add())
except MaxCallsException as e:
    print(e)