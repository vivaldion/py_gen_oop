"""Реализуйте класс EasyDict, наследника класса dict, описывающий словарь, значения элементов которого можно получать как по ключам ([key]), так и по одноименным атрибутам (.key). Процесс создания экземпляра класса EasyDict должен совпадать с процессом создания экземпляра класса dict.

Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса EasyDict нет, она может быть произвольной."""


class EasyDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self:
            setattr(self, i, self[i])

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        setattr(self, key, value)


easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})

easydict['city'] = 'Dubai'
easydict['age'] = 30
print(easydict.city)
print(easydict.age)

class EasyDict(dict):
    __getattr__ = dict.__getitem__