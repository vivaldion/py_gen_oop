'''Будем считать вещественным числом последовательность из одной или более цифр, которая может начинаться с необязательного символа дефиса -, а также содержать на любой позиции одну десятичную точку ., кроме случая, когда точка стоит перед символом дефиса.

Реализуйте функцию is_decimal(), которая принимает один аргумент:

string — строка, содержащая произвольный набор символов
Функция должна возвращать True, если строка string представляет собой целое или вещественное число, или False в противном случае.'''
import re
def is_decimal(string):
    reg_expr = r'-?(\d+)?(\.\d+)?|-?\d+\.'
    return bool(re.fullmatch(reg_expr,string))