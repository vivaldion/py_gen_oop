'''Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case. При создании экземпляра класс не должен принимать никаких аргументов.

Класс CaseHelper должен иметь четыре статических метода:

is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Snake Case, или False в противном случае
is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Upper Camel Case, или False в противном случае
to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case, записывает ее в стиле Snake Case и возвращает полученный результат
to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case, записывает ее в стиле Upper Camel Case и возвращает полученный результат'''

import re

class CaseHelper:
    camel = re.compile(r'^([A-Z][a-z]+)+$')
    snake = re.compile(r'^([a-z]+_?)+$')

    @staticmethod
    def is_snake(string):
        return bool(CaseHelper.snake.search(string))

    @staticmethod
    def is_upper_camel(string):
        return bool(CaseHelper.camel.search(string))

    @staticmethod
    def to_snake(string):
        string = re.sub(r'\B([A-Z])\B', r'_\1', string)
        return string.lower()

    @staticmethod
    def to_upper_camel(string):
        return re.sub(r'_', r'', string.title())