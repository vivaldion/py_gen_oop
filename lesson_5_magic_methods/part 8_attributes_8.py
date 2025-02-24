"""Будем считать атрибут защищенным, если его имя начинается с символа нижнего подчеркивания (_). Например, _password, __email и __dict__.

Реализуйте класс ProtectedObject. При создании экземпляра класс должен принимать произвольное количество именованных аргументов. Все передаваемые аргументы должны устанавливаться создаваемому экземпляру в качестве атрибутов.

Класс ProtectedObject должен запрещать получать и изменять значения защищенных атрибутов своих экземпляров, а также удалять эти атрибуты или создавать новые. При попытке получить или изменить значение защищенного атрибута, а также попытке удалить атрибут или создать новый, должно возбуждаться исключение AttributeError с текстом:

Доступ к защищенному атрибуту невозможен
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

Примечание 2. Никаких ограничений касательно реализации класса ProtectedObject нет, она может быть произвольной.

Примечание 3. Тестовые данные доступны по ссылкам:"""

class ProtectedObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            object.__setattr__(self,k, v)

    def __setattr__(self, key: str, value):
        if not key.startswith("_"):
            object.__setattr__(self, key, value)
        else:
            raise AttributeError('Доступ к защищенному атрибуту невозможен')

    def __getattribute__(self, item: str):
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            return object.__getattribute__(self, item)

    def __delattr__(self, item):
        if item.startswith('_'):
            raise AttributeError('Доступ к защищенному атрибуту невозможен')
        else:
            object.__delattr__(self, item)


user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')

user.login = 'Kamiya'
print(user.login)

user.nickname = 'PG'
print(user.nickname)