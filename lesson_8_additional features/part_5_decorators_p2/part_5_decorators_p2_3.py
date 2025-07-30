"""
Декоратор @jsonattr
Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен принимать один аргумент:

filename — имя json файла, содержимым которого является JSON объект
Декоратор должен открывать файл filename и добавлять в качестве атрибута декорируемому классу каждую пару ключ-значение JSON объекта, содержащегося в этом файле.

Примечание. Тестовые данные доступны по ссылкам:
"""

import functools
import json


def jsonattr(file):
    def wrapper(cls):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for key, value in data.items():
                setattr(cls, key, value)
        return  cls
    return wrapper




