"""
Декоратор @track_instances
Реализуйте декоратор @track_instances для декорирования класса. Декоратор должен добавлять декорируемому классу атрибут instances, содержащий список всех созданных экземпляров этого класса.

Примечание 1. Экземпляры декорируемого класса в списке по атрибуту instances должны располагаться в том порядке, в котором они были созданы.
"""


import functools


def track_instances(cls: object):
    old_init = cls.__init__
    if not hasattr(cls, 'instances'):
        cls.instances = []

    @functools.wraps(old_init)
    def new_init(self,*args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__= new_init
    return  cls