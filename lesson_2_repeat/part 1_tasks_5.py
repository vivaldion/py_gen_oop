'''Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.

Также декоратор должен сохранять имя и строку документации декорируемой функции'''
import functools
import json
def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapper