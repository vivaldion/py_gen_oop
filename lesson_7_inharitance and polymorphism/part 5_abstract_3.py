"""
1. Реализуйте абстрактный класс Validator, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение является корректным. При создании экземпляра класс не должен принимать никаких аргументов.

Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.

При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:

Атрибут не найден
При установке или изменении значения атрибута дескриптор должен сперва проверять его на корректность с помощью метода validate().

Класс Validator должен иметь один абстрактный метод экземпляра:

validate() — пустой метод
2. Также реализуйте класс Number, наследника класса Validator, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение является числом из определенного диапазона. Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

minvalue — левая граница диапазона, по умолчанию имеет значение None и не ограничивает число слева
maxvalue — правая граница диапазона, по умолчанию имеет значение None и не ограничивает число справа
Класс Number должен иметь один метод экземпляра:

validate() — метод, принимающий в качестве аргумента произвольный объект и возбуждающий исключение, если он не удовлетворяет каким-либо условиям. Если указанный объект не принадлежит типу int или float, должно быть возбуждено исключение TypeError с текстом:
Устанавливаемое значение должно быть числом
Если указанный объект является числом меньше minvalue, должно быть возбуждено исключение ValueError с текстом:
Устанавливаемое число должно быть больше или равно <minvalue>
Если указанный объект является числом больше maxvalue, должно быть возбуждено исключение ValueError с текстом:
Устанавливаемое число должно быть меньше или равно <maxvalue>
3. Наконец, реализуйте класс String, наследника класса Validator, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение является строкой определенной длины. Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

minsize — минимальная длина слова, по умолчанию имеет значение None и не ограничивает минимальную длину
maxsize — максимальная длина слова, по умолчанию имеет значение None и не ограничивает максимальную длину
predicate — функция-предикат для дополнительной валидации, по умолчанию имеет значение None и не используется
Класс String должен иметь один метод экземпляра:

validate() — метод, принимающий в качестве аргумента произвольный объект и возбуждающий исключение, если он не удовлетворяет каким-либо условиям. Если указанный объект не принадлежит типу str, метод должен возбуждать исключение TypeError с сообщением:
Устанавливаемое значение должно быть строкой
Если указанный объект является строкой с длиной меньше minsize, должно быть возбуждено исключение ValueError с текстом:
Длина устанавливаемой строки должна быть больше или равна <minsize>
Если указанный объект является строкой с длиной больше maxsize, должно быть возбуждено исключение ValueError с текстом:
Длина устанавливаемой строки должна быть меньше или равна <maxsize>
Если указанный объект при передаче в функцию predicate() возвращает False, должно быть возбуждено исключение ValueError с текстом:
Устанавливаемая строка не удовлетворяет дополнительным условиям
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используется только с корректными данными.
"""


from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.attr = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.attr in instance.__dict__:
            return instance.__dict__[self.attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        if self.validate(value):
            instance.__dict__[self.attr] = value
        else:
            raise ValueError('Некорректное значение')

    @abstractmethod
    def validate(self, value):
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Устанавливаемое значение должно быть числом')
        if self.minvalue is not None:
            if value < self.minvalue:
                raise ValueError(f'Устанавливаемое число должно быть больше или равно {self.minvalue}')
        if self.maxvalue:
            if value > self.maxvalue:
                raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self.maxvalue}')
        return True


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Устанавливаемое значение должно быть строкой')
        if self.minsize:
            if len(value) < self.minsize:
                raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self.minsize}')
        if self.maxsize:
            if len(value) > self.maxsize:
                raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self.maxsize}')
        if self.predicate is not None:
            if not self.predicate(value):
                raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')
        return True


class Student:
    age = Number(18, 99)


student = Student()
student.age = 19
print(student.age)