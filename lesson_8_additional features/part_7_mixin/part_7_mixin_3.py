"""Класс AttributesMixin
Реализуйте класс AttributesMixin, добавляющий классам функционал получения информации об атрибутах их экземпляров.

Класс AttributesMixin должен иметь два метода экземпляра:

get_public_attributes() — метод, возвращающий список имен и значений публичных атрибутов экземпляров класса, которому добавляется функционал
get_protected_attributes() — метод, возвращающий список имен и значений защищенных атрибутов экземпляров класса, которому добавляется функционал
Списки, возвращаемые методами get_public_attributes() и get_protected_attributes(), должны иметь следующий формат:

[(<имя атрибута>, <значение атрибута>), (<имя атрибута>, <значение атрибута>), ...]
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса AttributesMixin нет, она может быть произвольной.
"""


class AttributesMixin:
    def get_public_attributes(self):
        return [(name, value) for name, value in self.__dict__.items() if not name.startswith('_')]

    def get_protected_attributes(self):
        return [(name, value) for name, value in self.__dict__.items() if name.startswith('_') and not  name.startswith(f'_{self.__class__.__name__}__')]

class BankAccount(AttributesMixin):
    def __init__(self, account_number, balance):
        self._account_number = account_number
        self.__balance = balance

bank_account = BankAccount(245980, 1000)
print(bank_account.get_public_attributes())
print(bank_account.get_protected_attributes())