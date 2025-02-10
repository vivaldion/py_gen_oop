"""Реализуйте класс Matrix, описывающий двумерную матрицу. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

rows — количество строк в матрице
cols — количество столбцов в матрице
value — начальное значение для элементов матрицы, по умолчанию имеет значение 0
Экземпляр класса Matrix должен иметь два атрибута:

rows — количество строк в матрице
cols — количество столбцов в матрице
Класс Matrix должен иметь два метода экземпляра:

get_value() — метод, принимающий в качестве аргументов строку row и столбец col и возвращающий элемент матрицы со строкой row и столбцом col
set_value() — метод, принимающий в качестве аргументов строку row, столбец col и значение value и устанавливающий в качестве значения элемента матрицы со строкой row и столбцом col значение value
Экземпляр класса Matrix должен иметь следующее формальное строковое представление:

Matrix(<количество строк в матрице>, <количество столбцов в матрице>)
Неформальным строковым представлением должна быть строка, в которой перечислены все элементы матрицы. Элементы строки матрицы должны быть разделены пробелом, строки матрицы должны быть разделены символом переноса строки \n. Например, для объекта Matrix(2, 3) неформальным строковым представлением должна быть строка 0 0 0\n0 0 0, которая при выводе будет отображаться следующим образом:

0 0 0
0 0 0
Также экземпляр класса Matrix должен поддерживать унарные операторы +, - и ~:

результатом унарного + должен являться новый экземпляр класса Matrix c исходным количеством строк и столбцов и с исходными элементами
результатом унарного - должен являться новый экземпляр класса Matrix c исходным количеством строк и столбцов и с элементами, взятыми с противоположным знаком
результатом унарного ~ должен являться новый экземпляр класса Matrix, представляющий транспонированную матрицу
Наконец, при передаче экземпляра класса Matrix в функцию round() должен возвращаться новый экземпляр класса Matrix c исходным количеством строк и столбцов и с элементами, округленными с помощью функции round(). Во время передачи в функцию round() должна быть возможность в качестве второго необязательного аргумента указать целое число, определяющее количество знаков после запятой при округлении.

Примечание 1. Индексация строк и столбцов в матрице начинается с нуля.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 3. Никаких ограничений касательно реализации класса Matrix нет, она может быть произвольной.

Примечание 4. Тестовые данные доступны по ссылкам:

Архив с тестами"""


class Matrix:
    def __init__(self, rows, cols, value=0):
        self.rows = rows
        self.cols = cols
        self.value = value
        self._matrix = [[value] * cols for _ in range(rows)]

    def get_value(self, row, col):
        return self._matrix[row][col]

    def set_value(self, row, col, value):
        self._matrix[row][col] = value

    def __str__(self):
        string_matrix = [[str(ele) for ele in row] for row in self._matrix]
        return '\n'.join(' '.join(row) for row in string_matrix)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'

    def __pos__(self):
        matrix = Matrix(self.rows, self.cols)
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, self.get_value(row, col))
        return matrix

    def __neg__(self):
        matrix = Matrix(self.rows, self.cols)
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, -self.get_value(row, col))
        return matrix

    def __round__(self, n):
        matrix = Matrix(self.rows, self.cols)
        for row in range(matrix.rows):
            for col in range(matrix.cols):
                matrix.set_value(row, col, round(self.get_value(row, col), n))
        return matrix

    def __invert__(self):
        matrix = Matrix(self.cols, self.rows)
        for row in range(self.cols):
            for col in range(self.rows):
                matrix.set_value(row, col, self.get_value(col, row))
        return matrix