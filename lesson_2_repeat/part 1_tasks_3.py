''' Каждая инверсия — это пара элементов, нарушающих порядок.

Реализуйте функцию inversions(), которая принимает один аргумент:

sequence — последовательность, элементами которой являются числа
Функция должна возвращать единственное число — количество инверсий в последовательности sequence.'''
def inversions(iterable):
    from itertools import combinations
    comp = combinations(iterable ,2)
    number = len(tuple(filter(lambda x: x[1]< x[0], comp)))
    return number
