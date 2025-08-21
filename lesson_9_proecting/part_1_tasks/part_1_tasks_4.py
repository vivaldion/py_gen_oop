"""Классы ArithmeticProgression и GeometricProgression
Реализуйте класс ArithmeticProgression для генерации членов арифметической прогрессии. При создании экземпляра класса ArithmeticProgression должны указываться первый член последовательности и разность прогрессии:

progression = ArithmeticProgression(0, 1)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 0 1 2 3 4 5 6 7 8 9 10
Обратите внимание, что арифметическая прогрессия должна быть итерируемой, а также бесконечной.

Аналогичным образом реализуйте класс GeometricProgression для генерации членов геометрической прогрессии. При создании экземпляра класса GeometricProgression должны указываться первый член последовательности и знаменатель прогрессии:

progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')    # 1 2 4 8
Геометрическая прогрессия, как и арифметическая, должна быть итерируемой, а также бесконечной."""


from collections.abc import Iterator

class ArithmeticProgression(Iterator):
    def __init__(self, fst, diff):
        self.fst = fst
        self.diff = diff


    def __next__(self):
        if 'now' in self.__dict__:
            self.now = self.now + self.diff
            return self.now
        else:
            self.now = self.fst
            return self.fst



class GeometricProgression(Iterator):
    def __init__(self, fst, cmn):
        self.fst = fst
        self.cmn = cmn


    def __next__(self):
        if 'now' in self.__dict__:
            self.now = self.now * self.cmn
            return self.now
        else:
            self.now = self.fst
            return self.now


progression = GeometricProgression(1, 2)

for elem in progression:
    if elem > 10:
        break
    print(elem, end=' ')