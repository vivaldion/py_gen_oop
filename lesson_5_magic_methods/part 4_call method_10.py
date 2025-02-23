"""Нередко во время сортировки объектов мы используем дополнительную функцию, которая описывает правило сортировки. Например, если нам нужно отсортировать список экземпляров некоторого класса на основе значений определенного атрибута, мы можем реализовать функцию, которая принимает в качестве аргумента этот экземпляр и возвращает значение необходимого атрибута.

Приведенный ниже код:

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]

print(sorted(users, key=lambda user: user.age))
выводит:

[User(Arthur, 20), User(Timur, 30), User(Gvido, 67)]
Удобно было бы иметь класс SortKey, позволяющий сортировать объекты на основе значений различных атрибутов, лишь перечисляя имена этих атрибутов.

Чтобы приведенный ниже код:

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'


users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20)]

print(sorted(users, key=SortKey('age')))            # сортировка на основе атрибута age
print(sorted(users, key=SortKey('name', 'age')))    # сортировка на основе атрибута name, а затем age
выводил:

[User(Arthur, 20), User(Timur, 30), User(Gvido, 67)]
[User(Arthur, 20), User(Gvido, 67), User(Timur, 30)]
Реализуйте класс SortKey, описывающий ключ для сортировки объектов на основе значений их определенных атрибутов. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых представляет имя атрибута, участвующего в сортировке.

Примечание 1. Имена атрибутов при создании экземпляра класса SortKey передаются в порядке приоритета, то есть при сортировке сначала должно учитываться значение первого атрибута, затем второго, и так далее.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными."""


class SortKey:

    def __init__(self, *args):
        self.keys = args

    def __call__(self, obj):
        return tuple(obj.__getattribute__(i) for i in self.keys)



class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'User({self.name}, {self.age})'

users = [User('Gvido', 67), User('Timur', 30), User('Arthur', 20), User('Timur', 45), User('Gvido', 60)]

print(sorted(users, key=SortKey('name')))
print(sorted(users, key=SortKey('name', 'age')))
print(sorted(users, key=SortKey('age')))
print(sorted(users, key=SortKey('age', 'name')))

