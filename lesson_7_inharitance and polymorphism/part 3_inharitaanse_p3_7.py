"""Реализуйте класс AdvancedTuple, наследника класса tuple, который описывает кортеж, умеющий выполнять операцию сложения (+, +=) не только с экземплярами классов AdvancedTuple и tuple, но и с любыми итерируемыми объектами. Процесс создания экземпляра класса AdvancedTuple должен совпадать с процессом создания экземпляра класса tuple.

Примечание 1. Как бы ни выполнялось сложение, с помощью оператора + или +=, результатом операции должен являться новый экземпляр класса AdvancedTuple.

Примечание 2. Никаких ограничений касательно реализации класса AdvancedTuple нет, она может быть произвольной."""

class AdvancedTuple(tuple):

    @staticmethod
    def check(obj):
        if hasattr(obj, '__iter__') or hasattr(obj, '__getitem__'):
            return True
        return False

    def __add__(self, other):
        if AdvancedTuple.check(other):
            return AdvancedTuple(super().__add__(tuple(other)))
        return NotImplemented

    def __iadd__(self, other):
        if AdvancedTuple.check(other):
            return AdvancedTuple(super().__add__(tuple(other)))
        return NotImplemented

    def __radd__(self, other):
        if AdvancedTuple.check(other):
            return AdvancedTuple(tuple(other) + tuple(self))
        return NotImplemented