'''В целях безопасности в базах данных пароли от аккаунтов пользователей хранятся не в явном виде, а в виде хеш-значений — чисел, вычисленных по специальному алгоритму на основе паролей.

Вам доступна функция hash_function(), которая принимает в качестве аргумента пароль и возвращает его хеш-значение.

Реализуйте класс Account, описывающий аккаунт интернет-пользователя на некотором сервисе. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

login — логин пользователя
password — пароль пользователя
Класс Account должен иметь два свойства:

login — свойство, доступное только для чтения, возвращающее логин пользователя. При попытке изменения свойства должно быть возбуждено исключение AttributeError с текстом:
Изменение логина невозможно
password — свойство, доступное для чтения и записи, возвращающее хеш-значение пароля от аккаунта пользователя. При изменении свойство должно вычислять хеш-значение нового пароля и сохранять его, а не сам пароль'''


def hash_function(password):
    hash_value = 0
    for char, index in zip(password, range(len(password))):
        hash_value += ord(char) * index
    return hash_value % 10**9

class Account:
    def __init__(self, login, password):
        self._login = login
        self.password = password
        pass

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, *args, **kwargs):
        raise AttributeError('Изменение логина невозможно')

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self, password):
        self._password = hash_function(password)



account = Account('hannymad', 'cakeisalie')

print(account.login)
print(account.password)