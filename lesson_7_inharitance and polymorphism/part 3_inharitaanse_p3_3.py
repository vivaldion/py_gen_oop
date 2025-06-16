"""Реализуйте класс FuzzyString, наследника класса str, описывающий строку, которая при любых сравнениях (==, !=, >, <, >=, <=) и проверках на принадлежность (in, not in) не учитывает регистр. Процесс создания экземпляра класса FuzzyString должен совпадать с процессом создания экземпляра класса str.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented."""

from functools import total_ordering


@total_ordering
class FuzzyString(str):

    def __le__(self, other):
        if isinstance(other, str):
            return self.lower() <= other.lower()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, str):
            return self.lower() == other.lower()
        return NotImplemented

    def __contains__(self, substring):
        if isinstance(substring, str):
            return substring.lower() in self.lower()
        return NotImplemented

    __lt__ = getattr(object, '__lt__', None)
    __gt__ = getattr(object, '__gt__', None)
    __ge__ = getattr(object, '__ge__', None)
    __ne__ = getattr(object, '__ne__', None)