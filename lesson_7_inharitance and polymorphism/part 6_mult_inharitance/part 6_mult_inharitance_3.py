"""Реализуйте функцию get_method_owner(), которая принимает два аргумента в следующем порядке:

cls — произвольный класс
method — строковое название метода
Функция должна возвращать класс, от которого класс cls унаследовал метод method. Если метода method нет ни в самом классе, ни в одном другом классе из его иерархии, функция get_method_owner() должна вернуть значение None."""


from typing import Type, Any
def get_method_owner(cls: Type[Any], method):

    if method in cls.__dict__:
        return cls

    for base in cls.__mro__:
        if method in base.__dict__:
            return get_method_owner(base, method)
    return None

class A:
    def method(self):
        print('Метод класса A')


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(get_method_owner(D, 'method'))