'''
в 2025-02-25 должен выводить:

1
 в 2025-02-26 должен выводить:

2
Примечание 2. Для проверки того, что свойство age возвращает верный возраст, мы используем собственную функцию current_age(), которая вычисляет возраст в годах на основе даты рождения и текущей даты.'''

from datetime import date
from datetime import timedelta
from functools import singledispatchmethod



class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def dat(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def stri(self, birth_date):
        try:
            birth_date = date.fromisoformat(birth_date)
            self.birth_date = birth_date
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register
    def dat(self, birth_date: tuple|list):
        try:
            self.birth_date = date(*birth_date)
        except:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        return  date.today().year - self.birth_date.year - ((date.today().month, date.today().day) < (self.birth_date.month, self.birth_date.day))


birthday = date(2020, 9, 18)
birthinfo = BirthInfo(birthday)
print(birthinfo.age)
