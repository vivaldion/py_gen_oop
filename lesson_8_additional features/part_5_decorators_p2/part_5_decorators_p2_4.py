"""
екоратор @singleton
Реализуйте декоратор @singleton для декорирования класса. Декоратор должен превращать декорируемый класс в синглтон, то есть в класс, при первом вызове создающий единственный свой экземпляр и при последующих вызовах возвращающий его же.

Примечание 1. Подробнее почитать про шаблон проектирования синглтон можно по ссылке.
"""
import functools


def singleton(cls):
    cls_new = cls.__new__
    cls._instance = None

    @functools.wraps(cls_new)
    def new_for_singleton(*args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    cls.__new__ = new_for_singleton
    return cls

@singleton
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


instances = [Person('John Doe') for _ in range(1000)]
person = Person('Doe John')
print(person)
print(instances[389])
print(all(instance is person for instance in instances))
