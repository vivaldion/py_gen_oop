'''Реализуйте класс Person, описывающий человека. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

name — имя человека
surname — фамилия человека
Экземпляр класса Person должен иметь два атрибута:

name — имя человека
surname — фамилия человека
Класс Person должен иметь одно свойство:

fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:
<имя> <фамилия>
Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя. Аналогично при изменении полного имени должны изменяться имя и фамилия.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.'''

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_full(self):
        return self.name + ' ' + self.surname


    def setter_full(self, full_name):
        self.name, self.surname = full_name.split()

    fullname = property(get_full, setter_full)

person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)

