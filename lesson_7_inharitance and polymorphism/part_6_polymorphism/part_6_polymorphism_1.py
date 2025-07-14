'''
1. Реализуйте класс USADate, описывающий дату в американском формате. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

year — год
month — месяц
day — день
Класс USADate должен иметь два метода экземпляра:

format() — метод, который возвращает строку, представляющую собой дату в формате MM-DD-YYYY
iso_format() — метод, который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
2. Также реализуйте класс ItalianDate, описывающий дату в итальянском формате, конструктор которого принимает три аргумента:

year — год
month — месяц
day — день
Класс ItalianDate должен иметь два метода экземпляра:

format() — метод, который возвращает строку, представляющую собой дату в формате DD/MM/YYYY
iso_format() — метод, который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
'''
from datetime import datetime

class USADate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.dt = datetime.strptime(f"{month}-{day}-{year}", f"%m-%d-%Y")

    def format(self):
        return self.dt.strftime('%m-%d-%Y')

    def iso_format(self):
        return self.dt.date().isoformat()


class ItalianDate(USADate):
    def format(self):
        return self.dt.strftime('%d/%m/%Y')


usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())