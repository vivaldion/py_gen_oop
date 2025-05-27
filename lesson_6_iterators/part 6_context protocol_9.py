'''Реализуйте класс Atomic. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

data — произвольный список, множество или словарь
deep — булево значение, по умолчанию равняется False
Экземпляр класса Atomic должен являться контекстным менеджером, который позволяет выполнять операции над коллекцией data внутри блока with в атомарном режиме, то есть либо все операции должны быть выполнены, либо ни одна из них. Если все операции корректны (не приводят к возбуждению исключения), они должны быть применены к коллекции data. Если какая-либо операция некорректна, все ранее выполненные операции должны быть отменены, а коллекция data должна быть возвращена в исходное состояние.

Параметр deep должен определять состояние вложенных структур коллекции data после завершения блока with. Если он имеет значение False, контекстный менеджер должен возвращать в исходное состояние только саму коллекцию data, не затрагивая ее вложенные структуры. Например, если data является двумерным списком и внутри блока with произошло изменение одного из его вложенных списков, то этот вложенный список должен сохранить свое новое состояние, даже если последующие операции внутри блока with приведут к возбуждению исключения и возврату коллекции data в исходное состояние. Если же параметр deep имеет значение True, контекстный менеджер должен возвращать в исходное состояние не только саму коллекцию data, но и ее вложенные структуры.

Примечание 1. Наглядные примеры использования класса Atomic продемонстрированы в тестовых данных.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.'''


import copy


class Atomic:
    def __init__(self, data, deep=False):
        self.data = data
        self.deep = deep
        self.copy = None

    def __enter__(self):
        if isinstance(self.data, (list, set, dict)):
            if self.deep:
                self.copy = copy.deepcopy(self.data)
            else:
                if isinstance(self.data, list):
                    self.copy = self.data.copy()
                elif isinstance(self.data, set):
                    self.copy = set(self.data)
                elif isinstance(self.data, dict):
                    self.copy = dict(self.data)
        return self.copy

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            if isinstance(self.data, list):
                self.data[:] = self.copy
            elif isinstance(self.data, set):
                self.data.clear()
                self.data.update(self.copy)
            elif isinstance(self.data, dict):
                self.data.clear()
                self.data.update(self.copy)
        self.copy = None
        return True


numbers = [1, 2, 3, 4, 5]

with Atomic(numbers) as atomic:
    atomic.append(6)
    atomic[2] = 0
    del atomic[100]           # обращение по несуществующему индексу

print(numbers)