'''Целым числом будем считать последовательность из одной или более цифр, которая может начинаться с необязательного символа дефиса -.

Реализуйте функцию is_integer(), которая принимает один аргумент:

string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой целое число, или False в противном случае.'''
import re
def is_integer(string):
    expr = r'-?\d+'
    return bool(re.fullmatch(expr, string))