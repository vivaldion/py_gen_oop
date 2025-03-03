"""Реализуйте класс Vector, описывающий вектор на плоскости. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

x — координата вектора по оси
x
x
y — координата вектора по оси
y
y
Экземпляр класса Vector должен иметь следующее формальное строковое представление:

Vector(<координата x>, <координата y>)
И следующее неформальное строковое представление:

(<координата вектора по оси x>, <координата вектора по оси y>)
Также экземпляр класса Vector должен поддерживать унарные операторы + и -:

результатом унарного + должен являться новый экземпляр класса Vector с исходными координатами
результатом унарного - должен являться новый экземпляр класса Vector с координатами, взятыми с противоположным знаком
Наконец, при передаче экземпляра класса Vector в функцию abs() должен возвращаться его модуль.

Примечание 1. Модуль вектора с координатами
(
x
,
y
)
(x,y) вычисляется по формуле
x
2
+
y
2
x
2
 +y
2

​
 .

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными."""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __pos__(self):
        return self.__class__(self.x, self.y)

    def __neg__(self):
        return self.__class__(-self.x, -self.y)

    def __abs__(self):
        return pow((self.x ** 2 + self.y ** 2), 0.5)

vector = Vector(3, -4)

print(+vector)
print(-vector)
print(abs(vector))