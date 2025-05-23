"""Реализуйте класс SequenceZip. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является последовательностью. Класс SequenceZip должен описывать последовательность, элементами которой являются элементы переданных в конструктор итерируемых объектов, объединенные в кортежи. Объединение должно происходить аналогично тому, как это делает функция zip().

При передаче экземпляра класса SequenceZip в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса SequenceZip должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.

Наконец, экземпляр класса SequenceZip должен позволять получать значения своих элементов с помощью индексов."""

from memory_profiler import memory_usage
from copy import deepcopy
from itertools import islice

class SequenceZip:
    def __init__(self, *args):
        self.len = min(len(i) for i in args) if args else 0
        self.args = deepcopy(args)

    def __iter__(self):
        return zip(*self.args)

    def __len__(self):
        return self.len

    def __getitem__(self, item):
        new = zip(*self.args)
        return next(islice(new, item, None))

def func():
    many_large_sequences = [range(100000) for _ in range(100)]
    sequencezip = SequenceZip(*many_large_sequences)
    return sequencezip[99999]

if __name__ == '__main__':
    print(f"Peak usage: {max(memory_usage(func))}")