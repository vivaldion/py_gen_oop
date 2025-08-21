"""
Реализуйте функцию anything(), которая возвращает такой объект, результат сравнения с которым c помощью операторов ==, !=, >, <, >= и <= всегда равен True.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию anything(), но не код, вызывающий ее.
"""


class Anything:
    def __eq__(self, other):
        return True
    __ne__ = __gt__=  __lt__= __ge__ = __le__ = __eq__

def anything():
    return Anything()


import math, re

print(anything() != [])
print(anything() < 'World')
print(anything() > 81)
print(anything() >= re)
print(anything() <= math)
print(anything() == ord)