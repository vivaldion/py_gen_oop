"""Реализуйте класс Peekable. При создании экземпляра класс должен принимать один аргумент:

iterable — итерируемый объект
Экземпляр класса Peekable должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.

Класс Peekable должен иметь один метод экземпляра:

peek() — метод, возвращающий следующий элемент итератора аналогично функции next(), но при этом не сдвигающий итератор. Если итератор пуст, должно быть возбуждено исключение StopIteration. Также метод должен уметь принимать один необязательный аргумент default — объект, который будет возвращен вместо возбуждения исключения StopIteration, если итератор пуст"""
new = object()
class Peekable:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.peeked = None
        self.has_peeked = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.has_peeked:
            self.has_peeked = False
            return self.peeked
        else:
            return next(self.iterator)

    def peek(self, default=StopIteration):
        if not self.has_peeked:
            try:
                self.peeked = next(self.iterator)
                self.has_peeked = True
            except StopIteration:
                if default is not StopIteration:
                    return default
                raise
        return self.peeked

if __name__ == "__main__":
    iterator = Peekable(iter([]))

    try:
        iterator.peek()
    except StopIteration:
        print('Пустой итератор')

    try:
        next(iterator)
    except StopIteration:
        print('Пустой итератор')

