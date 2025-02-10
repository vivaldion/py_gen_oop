"""IP-адрес — это уникальный адрес, идентифицирующий устройство в интернете или локальной сети. IP-адреса представляют собой набор из четырех целых чисел, разделенных точками. Например, 192.158.1.38. Каждое число в наборе принадлежит интервалу от 0 до 255. Таким образом, полный диапазон IP-адресации — это адреса от 0.0.0.0 до 255.255.255.255.

Реализуйте класс IPAddress, описывающий IP-адрес. При создании экземпляра класс должен принимать один аргумент:

ipaddress — IP-адрес, представленный в одном из следующих вариантов:
строка из четырех целых чисел, разделенных точками
список или кортеж из четырех целых чисел
Экземпляр класса IPAddress должен иметь следующее формальное строковое представление:

IPAddress('<IP-адрес в виде четырех целых чисел, разделенных точками>')
И следующее неформальное строковое представление:

<IP-адрес в виде четырех целых чисел, разделенных точками>"""

from functools import singledispatchmethod


class IPAddress:
    @singledispatchmethod
    def __init__(self, ip):
        self.ip = ip

    @__init__.register
    def implementation(self, ip: list | tuple):
        ip = '.'.join(map(str, ip))
        return IPAddress.__init__(self, ip)

    def __repr__(self):
        return f"IPAddress('{self.ip})"

    def __str__(self):
        return self.ip

ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))