"""Реализуйте класс NumberList, наследника класса UserList, описывающий список, элементами которого могут быть лишь числа. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса NumberList. Если хотя бы один элемент переданного итерируемого объекта не является числом, должно быть возбуждено исключение TypeError с текстом:
Элементами экземпляра класса NumberList должны быть числа
Итерируемый объект может быть не передан, в таком случае начальный набор элементов считается пустым
При изменении экземпляра класса NumberList с помощью индексов, операций сложения (+, +=) и методов append(), extend() и insert() должна производиться проверка на то, что добавляемые элементы являются числами, в противном случае должно возбуждаться исключение TypeError с текстом:

Элементами экземпляра класса NumberList должны быть числа
Примечание 1. Числами будем считать экземпляры классов int и float.

Примечание 2. Экземпляры класса NumberList должны поддерживать операции сложения (+, +=) и метод extend() как между собой, так и между любыми итерируемыми объектами.

Примечание 3. Экземпляр класса NumberList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса NumberList измениться  не должен.

Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными."""



from collections import UserList


class NumberList(UserList):
    @staticmethod
    def num(num):
        if isinstance(num, int | float):
            return num
        else:
            raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def __init__(self, iterable=None):
        if iterable is None:
            iterable = []
        super().__init__(self.num(i) for i in iterable)

    def append(self, n):
        self.data.append(self.num(n))

    def extend(self, n):
        self.data.extend(self.num(i) for i in n)

    def insert(self, i: int, item) -> None:
        self.data.insert(i, self.num(item))

    def __setitem__(self, key, value):
        self.data.__setitem__(key, self.num(value))

    def __iadd__(self, other):
        return self.data + [self.num(i) for i in other]

    def __add__(self, other):
        return self.data + [self.num(i) for i in other]

numberlist = NumberList([1, 2])
try:
    numberlist.insert(0, [5, 4, 3])
except TypeError as e:
    print(e)