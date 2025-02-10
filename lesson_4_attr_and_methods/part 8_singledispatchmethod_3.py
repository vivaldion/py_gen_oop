from functools import singledispatchmethod



class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @format.register
    @staticmethod
    def _types_format(data: int | float | tuple | list | dict):
        d = {int: 'Целое число', float: 'Вещественное число', list: 'Элементы списка', tuple: 'Элементы кортежа',
             dict: 'Пары словаря'}
        stri1 = d[type(data)] + ':'
        if isinstance(data, int|float):
            stri2 = str(data)
        elif isinstance(data, tuple|list):
            stri2 = ', '.join(map(lambda x: f"'{x}'" if isinstance(x, str) else str(x), data))
        else:
            stri2 = list(data.items())
            stri2 = ', '.join(map(lambda x: f"'{x}'" if isinstance(x, str) else str(x), stri2))

        print(stri1, stri2)

Formatter.format({'Cuphead': 1, 'Mugman': 3})
Formatter.format({1: 'one', 2: 'two'})
Formatter.format({1: True, 0: False})
Formatter.format(1337)
Formatter.format(20.77)