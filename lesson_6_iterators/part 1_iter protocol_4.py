"""Реализуйте класс SkipIterator. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

iterable — итерируемый объект
n — целое неотрицательное число
Экземпляр класса SkipIterator должен являться итератором, который генерирует элементы итерируемого объекта iterable, пропуская по n элементов, а затем возбуждает исключение StopIteration.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Класс SkipIterator должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:"""

from itertools import islice

class SkipIterator:
    def __init__(self, iterable, n):
        self.n = n
        self.iterable = islice(iterable, 0, None, n+1)

    def __next__(self):
        return next(self.iterable)

    def __iter__(self):
        return self




# TEST_10:
skipiterator = SkipIterator(range(1000), 7)

for _ in range(25):
    next(skipiterator)

print(next(skipiterator))
print(next(skipiterator))
print(next(skipiterator))