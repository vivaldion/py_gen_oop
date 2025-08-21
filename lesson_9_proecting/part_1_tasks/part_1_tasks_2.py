"""
Реализуйте класс Vector, экземпляр которого представляет собой вектор произвольной размерности. Экземпляр класса Vector должен создаваться на основе собственных координат:

a = Vector(1, 2, 3)
b = Vector(3, 4, 5)
c = Vector(5, 6, 7, 8)
В качестве неформального строкового представления вектор должен иметь собственные координаты, заключенные в круглые скобки:

print(a)                       # (1, 2, 3)
print(b)                       # (3, 4, 5)
print(c)                       # (5, 6, 7, 8)
Векторы должны поддерживать между собой операции сложения, вычитания, произведения и нормирования:

print(a + b)                   # (4, 6, 8)
print(a - b)                   # (-2, -2, -2)
print(a * b)                   # 1*3 + 2*4 + 3*5 = 26
print(c.norm())                # sqrt(5**2 + 6**2 + 7**2 + 8**2) = sqrt(174) = 13.19090595827292
а также операции сравнения на равенство и неравенство:

print(a == Vector(1, 2, 3))    # True
print(a == Vector(4, 5, 6))    # False
При попытке выполнить какую-либо операцию с векторами разной размерности должно быть возбуждено исключение ValueError с текстом:

Векторы должны иметь равную длину
"""
import math


class Vector:
    def __init__(self, *coords):
        self.coords = coords

    def __str__(self):
        return f"({', '.join(map(str, self.coords))})"

    def __repr__(self):
        return f"Vector{self.coords}"

    def _check_length(self, other):
        if len(self.coords) != len(other.coords):
            raise ValueError("Векторы должны иметь равную длину")

    def __add__(self, other):
        self._check_length(other)
        return Vector(*(a + b for a, b in zip(self.coords, other.coords)))

    def __sub__(self, other):
        self._check_length(other)
        return Vector(*(a - b for a, b in zip(self.coords, other.coords)))

    def __mul__(self, other):
        self._check_length(other)
        return sum(a * b for a, b in zip(self.coords, other.coords))

    def norm(self):
        return math.sqrt(sum(x ** 2 for x in self.coords))

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        self._check_length(other)
        return self.coords == other.coords

    def __ne__(self, other):
        if not isinstance(other, Vector):
            return True
        self._check_length(other)
        return self.coords != other.coords

vector1 = Vector(1, 2, 3)
vector2 = Vector(5, 6, 7, 8)

try:
    print(vector1 == vector2)
except ValueError as e:
    print(e)