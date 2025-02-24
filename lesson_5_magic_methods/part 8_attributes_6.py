"""Реализуйте класс AttrsNumberObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Экземпляр класса AttrsNumberObject должен иметь один атрибут:

attrs_num — количество атрибутов, которыми обладает экземпляр класса AttrsNumberObject на данный момент, включая сам атрибут attrs_num
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса AttrsNumberObject нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:"""

class AttrsNumberObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


    def __getattr__(self, item):
        if item == 'attrs_num':
            return len(self.__dict__)


music_group = AttrsNumberObject(name='Alexandra Savior', genre='dream pop')

print(music_group.attrs_num)
del music_group.genre
print(music_group.attrs_num)

