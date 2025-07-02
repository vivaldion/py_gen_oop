"""Реализуйте класс SortedList, описывающий список, который автоматически сортируется при создании и любом изменении. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект, определяющий начальный набор элементов отсортированного списка. Если не передан, начальный набор элементов считается пустым
Класс SortedList должен иметь три метода экземпляра:

add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в экземпляр класса SortedList
discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий все его включения из экземпляра класса SortedList, если он в нем присутствует
update() — метод, принимающий в качестве аргумента итерируемый объект и добавляющий все его элементы в экземпляр класса SortedList
Также класс SortedList должен иметь такие методы экземпляра, как append(), insert(), extend() и reverse(), при попытке воспользоваться которыми должно быть возбуждено исключение NotImplementedError.

Экземпляр класса SortedList должен иметь следующее формальное строковое представление:

SortedList([<первый элемент списка>, <второй элемент списка>, ...])
При передаче экземпляра класса SortedList в функцию len() должно возвращаться количество элементов в нем. При попытке передачи экземпляра класса SortedList в функцию reversed() должно быть возбуждено исключение NotImplementedError.

Помимо этого, экземпляр класса SortedList должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Также экземпляр класса SortedList должен поддерживать операцию проверки на принадлежность с помощью оператора in.

Вдобавок ко всему, экземпляр класса SortedList должен позволять получать и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных. При попытке изменить значение элемента по его индексу должно быть возбуждено исключение NotImplementedError.

Экземпляры класса SortedList должны поддерживать между собой арифметические операции с помощью операторов + и +=:

оператор + должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки. Результатом работы оператора должен являться новый экземпляр класса SortedList
оператор += должен выполнять операцию сложения двух отсортированных списков путем их конкатенации и последующей сортировки. Результатом работы оператора должен являться левый экземпляр класса SortedList
Наконец, экземпляр класса SortedList должен поддерживать операцию умножения на целое число n с помощью операторов * и *=:

оператор * должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. Результатом работы оператора должен являться новый экземпляр класса SortedList
оператор *= должен выполнять операцию умножения отсортированного списка на число с последующей его сортировкой. Результатом работы оператора должен являться левый экземпляр класса SortedList
Примечание 1. Гарантируется, что элементами одного экземпляра класса SortedList являются объекты, сравнимые между собой.

Примечание 2. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.

Примечание3. Экземпляр класса SortedList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса SortedList измениться  не должен.

Примечание 4.  Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.

Примечание 5. Никаких ограничений касательно реализации класса SortedList нет, она может быть произвольной. Однако попробуйте решить задачу так, чтобы операция добавления элементов в список выполнялась как можно быстрее."""

from collections.abc import MutableSequence

import bisect


class SortedList(MutableSequence):
    def __init__(self, data: list = None):
        self.data = list(sorted(data))[:] if data else []

    def add(self, obj):
        bisect.insort(self.data, obj)

    def discard(self, obj):
        self.data = [i for i in self.data if i != obj]


    def update(self, iterable):
        for i in iterable:
            bisect.insort(self.data, i)

    def append(self, value = 0, index=0):
        raise NotImplementedError

    __reversed__ =  insert = extend = append

    def __setitem__(self, key, value):
        raise NotImplementedError

    def __len__(self):
        return len(self.data)

    def __delitem__(self, key):
        del self.data[key]

    def __repr__(self):
        return f'SortedList({self.data})'

    def __getitem__(self, item):
        return self.data[item]

    def __add__(self, other):
        if not isinstance(other, (SortedList, list, tuple)):
            return NotImplemented
        return SortedList(self.data + list(other))

    def __iadd__(self, other):
        if not isinstance(other, (SortedList, list, tuple)):
            return NotImplemented
        self.update(other)
        return self

    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.data = list.__mul__(self.data, other)
        return self.__class__(self.data)

    def __imul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        self.data *= other
        self.data = list(sorted(self.data))
        return self


if __name__ == "__main__":
    numbers = SortedList([5, 3, 4, 2, 1])
    print(numbers.__add__(1))
    print(numbers.__iadd__(1.1))
    print(numbers.__mul__([1, 2, 3]))
    print(numbers.__imul__({4, 5, 6}))