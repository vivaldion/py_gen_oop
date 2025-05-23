"""Реализуйте класс HistoryDict, описывающий словарь, который запоминает предыдущие значения по каждому ключу. При создании экземпляра класс должен принимать один аргумент:

data — словарь, определяющий начальный набор элементов экземпляра класса HistoryDict. Если не передан, начальный набор элементов считается пустым
Класс HistoryDict должен иметь пять методов экземпляра:

keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса HistoryDict
values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра класса HistoryDict
items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса HistoryDict в виде кортежей (<ключ>, <значение>)
history() — метод, принимающий в качестве аргумента ключ и возвращающий список, элементами которого являются все значения, которые когда-либо содержались в экземпляре класса HistoryDict по указанному ключу. Если данный ключ не содержится в экземпляре класса HistoryDict (был удален или никогда не добавлялся), метод должен вернуть пустой список
all_history() — метод, возвращающий словарь, ключами в котором являются ключи экземпляра класса HistoryDict, а значениями — списки, содержащие все значения, которые когда-либо содержались по этим ключам. Если какой-либо ключ был удален из экземпляра класса HistoryDict, то считается, что была удалена и его история
При передаче экземпляра класса HistoryDict в функцию len() должно возвращаться количество элементов в нем.

Также экземпляр класса HistoryDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, с помощью цикла for.

Наконец, экземпляр класса HistoryDict должен позволять получать и изменять значения своих элементов по их ключам, добавлять новые пары (ключ, значение) и удалять уже имеющиеся."""

from copy import deepcopy

class HistoryDict:
    def __init__(self, data={}):
        self.data = deepcopy(data)
        self._history = {key: [value] for key, value in self.data.items()}

    def __len__(self):
        return len(self.data)

    def values(self):
        return self.data.values()

    def keys(self):
        return self.data.keys()

    def items(self):
        return self.data.items()

    def history(self, key):
        return self._history.get(key, [])

    def all_history(self):
        return self._history

    def __getitem__(self, item):
        return self.data[item]

    def __delitem__(self, key):
        self.data.pop(key, None)
        self._history.pop(key, None)

    def __setitem__(self, key, value):
        self.data[key] = value
        try:
            self._history[key].append(value)
        except:
            self._history[key] = [value]

    def __iter__(self):
        return iter(self.data)

historydict = HistoryDict({'ducks': 99, 'cats': 1})

historydict['dogs'] = 1
print(len(historydict))
del historydict['ducks']
del historydict['cats']
print(len(historydict))