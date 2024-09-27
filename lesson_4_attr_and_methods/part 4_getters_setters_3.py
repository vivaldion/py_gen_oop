'''Реализуйте класс User, описывающий интернет-пользователя. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя пользователя. Если name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
age — возраст пользователя. Если age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
Некорректный возраст
Экземпляр класса User должен иметь два атрибута:

_name — имя пользователя
_age — возраст пользователя
Класс User должен иметь четыре метода экземпляра:

get_name() — метод, возвращающий имя пользователя
set_name() — метод, принимающий в качестве аргумента значение new_name и изменяющий имя пользователя на new_name. Если new_name не является непустой строкой, состоящей только из букв, должно быть возбуждено исключение ValueError с текстом:
Некорректное имя
get_age() — метод, возвращающий возраст пользователя
set_age() — метод, принимающий в качестве аргумента значение new_age и изменяющий возраст пользователя на new_age. Если new_age не является целым числом, принадлежащим отрезку [0; 110], должно быть возбуждено исключение ValueError с текстом:
Некорректный возраст'''
import re
class User:


    def __init__(self, name, age):
        self._name = None
        self._age = None
        self.set_name(name)
        self.set_age(age)
    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and re.fullmatch(r'[A-Za-zА-Яа-я]+', new_name):
            self._name = new_name
        else:
            raise ValueError('Некорректное имя')

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance((new_age), int) and re.fullmatch(r'\d+', str(new_age)) and  0 <= new_age <= 110:
            self._age = new_age
        else:
            raise ValueError('Некорректный возраст')

user = User('Меган', 37)

invalid_ages = ('ten', [], '', [True], -1, 111, 136, -50, 18.5)
for age in invalid_ages:
    try:
        user.set_age(age)
    except ValueError as e:
        print(e)