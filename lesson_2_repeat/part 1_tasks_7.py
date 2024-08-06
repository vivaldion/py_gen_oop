'''Реализуйте функцию quantify(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
predicate — функция-предикат, то есть функция, возвращающая True или False. Если имеет значение None, то работает аналогично функции bool()
Функция quantify() должна считать, для скольких элементов итерируемого объекта iterable функция-предикат predicate вернула значение True, и возвращать полученный результат.
'''

def quantify(iterable, predicate= bool):

    from itertools import filterfalse
    return len(list(filter(predicate, iterable)))