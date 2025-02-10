"""Реализуйте класс Version, описывающий версию программного обеспечения. При создании экземпляра класс должен принимать один аргумент:

version — строка из трех целых чисел, разделенных точками и описывающих версию ПО. Например, 2.8.1. Если одно из чисел не указано, оно считается равным нулю. Например, версия 2 равнозначна версии 2.0.0, а версия 2.8 равнозначна версии 2.8.0
Экземпляр класса Version должен иметь следующее формальное строковое представление:

Version('<версия ПО в виде трех целых чисел, разделенных точками>')
И следующее неформальное строковое представление:

<версия ПО в виде трех целых чисел, разделенных точками>
Также экземпляры класса Version должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два Version объекта считаются равными, если все три числа в их версиях совпадают. Version объект считается больше другогоVersion объекта, если первое число в его версии больше. Или если второе число в его версии больше, если первые числа совпадают. Или если третье число в его версии больше, если первые и вторые числа совпадают."""

from functools import total_ordering



@total_ordering
class Version:
    def __init__(self, version):
        version = version.split('.')
        while len(version) < 3:
            version.append('0')
        self.version = '.'.join(version)

    def __repr__(self):
        return f"Version('{self.version}')"

    def __str__(self):
        return f"{self.version}"

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.version == other.version
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return tuple(map(int,self.version.split('.'))) < tuple(map(int, other.version.split('.')))
        return NotImplemented

versions = [Version('162.5'), Version('68.3'), Version('173.8'), Version('108.9'), Version('159.6'), Version('145.7'),
            Version('187.6'), Version('137.7'), Version('33.7'), Version('22.4'), Version('199.4'), Version('122.1'),
            Version('47.4'), Version('10.2'), Version('164.9'), Version('191.6'), Version('139.9'), Version('184.4'),
            Version('94.9'), Version('188.6'), Version('56.8'), Version('138.7'), Version('83.2'), Version('59.4'),
            Version('189.7'), Version('128.5'), Version('6.6'), Version('111.2'), Version('5.6'), Version('188.8'),
            Version('64.9'), Version('76.6'), Version('85.5'), Version('195.6'), Version('12.8'), Version('66.7'),
            Version('121.7'), Version('20.3'), Version('9.8'), Version('140.8'), Version('70.3'), Version('12.3'),
            Version('97.9'), Version('10.4'), Version('98.5'), Version('74.1'), Version('164.8'), Version('55.1'),
            Version('147.7'), Version('39.2'), Version('27.4'), Version('50.3'), Version('174.7'), Version('196.9'),
            Version('106.3'), Version('89.1'), Version('59.9'), Version('189.4'), Version('45.7'), Version('158.2'),
            Version('147.5'), Version('3.2'), Version('49.9'), Version('173.6'), Version('63.9'), Version('8.2'),
            Version('29.4'), Version('15.7'), Version('85.2'), Version('109.2'), Version('152.9'), Version('49.6'),
            Version('53.5'), Version('26.7'), Version('135.9'), Version('155.3'), Version('134.7'), Version('159.4'),
            Version('99.3'), Version('188.9'), Version('197.4'), Version('99.2'), Version('160.5'), Version('183.7'),
            Version('74.2'), Version('184.7'), Version('139.8'), Version('199.2'), Version('122.1'), Version('198.7'),
            Version('190.1'), Version('200.2'), Version('40.3'), Version('150.4'), Version('20.2'), Version('186.7'),
            Version('47.2'), Version('57.5'), Version('72.8'), Version('23.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))