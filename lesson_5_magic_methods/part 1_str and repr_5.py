"""Реализуйте класс PhoneNumber, описывающий телефонный номер. При создании экземпляра класс должен принимать один аргумент:

phone_number — телефонный номер, представляющий строку из десяти цифр в одном из следующих форматов:
dddddddddd
ddd ddd dddd
Экземпляр класса PhoneNumber должен иметь следующее формальное строковое представление:

PhoneNumber('<телефонный номер в формате dddddddddd>')
И следующее неформальное строковое представление:

<телефонный номер в формате (ddd) ddd-dddd>"""

class PhoneNumber:
    def __init__(self, num:str):
        self.num = num.replace(' ', '')

    def __str__(self):
        return f'({self.num[0:3]}) {self.num[3:6]}-{self.num[6:-1]}'

    def __repr__(self):
        return f"PhoneNumber('{self.num}')"

phone = PhoneNumber('918 396 3389')

print(str(phone))
print(repr(phone))