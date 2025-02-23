from functools import total_ordering


@total_ordering
class RomanNumeral:

    int_roman = {
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
    }

    roman_int = {
        'I': 1, 'IV': 4, 'V': 5, 'IX': 9,
        'X': 10, 'XL': 40, 'L': 50, 'XC': 90,
        'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000
    }

    @staticmethod
    def int_to_roman(number):
        result = ''
        for n in (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1):
            while n <= number:
                result += RomanNumeral.int_roman[n]
                number -= n
        return result

    @staticmethod
    def roman_to_int(number):
        summ = 0
        for i in range(len(number) - 1, -1, -1):
            num = RomanNumeral.roman_int[number[i]]
            if 3 * num < summ:
                summ -= num
            else:
                summ += num
        return summ

    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number

    def __int__(self):
        return RomanNumeral.roman_to_int(self.number)

    def __add__(self, other):
        if isinstance(other, RomanNumeral):
            num1, num2 = int(self), int(other)
            return RomanNumeral(RomanNumeral.int_to_roman(num1 + num2))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumeral):
            num1, num2 = int(self), int(other)
            return RomanNumeral(RomanNumeral.int_to_roman(num1 - num2))
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, RomanNumeral):
            return self.number == other.number
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumeral):
            return RomanNumeral.roman_to_int(self.number) > RomanNumeral.roman_to_int(other.number)
        return NotImplemented

a = RomanNumeral('X')
b = RomanNumeral('XII')

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)