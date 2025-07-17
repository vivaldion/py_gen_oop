"""Реализуйте класс Shape, описывающий геометрическую фигуру. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

name — название фигуры
color — цвет фигуры
area — площадь фигуры
Экземпляр класса Shape должен иметь три атрибута:

name — название фигуры
color — цвет фигуры
area — площадь фигуры
Помимо приведенных выше трех атрибутов, экземпляр класса Shape не должен иметь возможности получить какие-либо другие атрибуты.

Также экземпляр класса Shape должен иметь следующее неформальное строковое представление:

<цвет фигуры> <название фигуры> (<площадь фигуры>)
Наконец, экземпляры класса Shape должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Две фигуры считаются равными, если их площади совпадают. Фигура считается больше другой фигуры, если ее площадь больше.

Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 2. Никаких ограничений касательно реализации класса Shape нет, она может быть произвольной."""


from functools import total_ordering


@total_ordering
class Shape:
    __slots__ = ('name', 'color', 'area')
    def __init__(self, name, color, area):
        self.color = color
        self.name = name
        self.area = area

    def __str__(self):
        return f'{self.color} {self.name} ({self.area})'

    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.area == other.area
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Shape):
            return self.area < other.area
        return NotImplemented

print(Shape('rectangle', 'green', 12) == Shape('triangle', 'red', 12))
print(Shape('triangle', 'red', 15) > Shape('triangle', 'red', 12))
