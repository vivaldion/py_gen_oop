"""
Декоратор @snake_case
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.

Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.

Частным случаем стиля Camel Case является lower Camel Case, когда с заглавной буквы пишутся все слова, кроме первого. Например, beeGeek и helloWorld.

Реализуйте декоратор @snake_case для декорирования класса. Декоратор должен принимать один аргумент:

attrs — булево значение, по умолчанию равняется False
Декоратор должен переименовывать все не магические методы в декорируемом классе, меняя их стиль написания c Camel Case и lower Camel Case на Snake Case. Параметр attrs должен определять, будут ли аналогичным образом переименованы атрибуты класса. Если он имеет значение True, стиль написания имен атрибутов класса должен поменяться с Camel Case и lower Camel Case на Snake case, если False — остаться прежним.
"""

import re
import functools
import inspect

def reformat(string: str):
    pattern = re.compile('([A-Z]?[a-z]*)')
    res =  pattern.findall(string)
    return "_".join(res).lower().rstrip('_').replace('__', "_")



def snake_case(attrs = False):
    def wrapper(cls):
        for name, attrib in list(vars(cls).items()):
                if (callable(attrib) and not name.startswith('__')) or attrs:
                    snake_name = reformat(name)
                    if snake_name != name:
                        setattr(cls, snake_name, attrib)
                        if name in cls.__dict__ and not name.startswith('__'):
                            delattr(cls, name)
        return cls
    return wrapper


@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

    def __init__(self):
        self.MyName = 'John Doe'


obj = MyClass()
print(obj.MyName)

myclass_attrs = ['FirstAttr', 'superSecondAttr']

for attr in myclass_attrs:
    try:
        print(MyClass.__dict__[attr])
    except KeyError:
        print('атрибут отсутствует')