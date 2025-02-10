from functools import singledispatchmethod

class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(int)
    @neg.register(float)
    @staticmethod
    def _int_float_neg(data):
        return data * (-1)

    @neg.register(bool)
    @staticmethod
    def _bool_neg(data):
        return not data
