"""Реализуйте класс SuperString, описывающий строку. При создании экземпляра класс должен принимать один аргумент:

string — значение строки
Экземпляр класса SuperString должен иметь следующее неформальное строковое представление:

<значение строки>
Помимо этого, экземпляры класса SuperString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса SuperString, представляющий конкатенацию исходных.

Также экземпляр класса SuperString должен поддерживать операции умножения, деления, побитового сдвига влево и побитового сдвига вправо на целое число n с помощью операторов *, /, << и >> соответственно:

результатом умножения должен являться новый экземпляр класса SuperString, представляющий исходную строку, умноженную на n.
результатом деления должен являться новый экземпляр класса SuperString, представляющий строку из первых m символов исходной строки, где m — длина исходной строки, поделенная нацело на n
результатом побитового сдвига влево должен являться новый экземпляр класса SuperString, представляющий исходную строку без последних n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
результатом побитового сдвига вправо должен являться новый экземпляр класса SuperString, представляющий исходную строку без первых n символов. Если n больше или равно длине исходной строки, результатом должен являться экземпляр класса SuperString, представляющий пустую строку
Операция умножения должна быть выполнима независимо от порядка операндов, то есть должна быть возможность умножить как строку на число, так и число на строку.

Примечание 1. Гарантируется, что экземпляр класса SuperString всегда делится на ненулевое число.

Примечание 2. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.

Примечание 3. Никаких ограничений касательно реализации класса SuperString нет, она может быть произвольной."""

class SuperString():
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f"{self.string}"

    def __add__(self, other):
        if isinstance(other, SuperString):
            return SuperString(self.string + other.string)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int):
            return SuperString(self.string * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int):
            return SuperString(self.string[0: len(self.string) // other])
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int):
            if len(self.string) >= other:
                return SuperString(self.string[0: len(self.string) - other])
            else:
                return ''
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            if len(self.string) >= other:
                return SuperString(self.string[other::])
            else:
                return ''
        return NotImplemented

superstring = SuperString('bee')
print(superstring.__add__([]))
print(superstring.__mul__(()))
print(superstring.__truediv__({}))
print(superstring.__lshift__(set()))
print(superstring.__rshift__('geek'))