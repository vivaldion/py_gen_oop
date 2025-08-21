"""
Реализуйте класс MultiKeyDict, который практически во всем повторяет класс dict. Создание экземпляра класса MultiKeyDict должно происходить аналогично созданию экземпляра класса dict:

multikeydict1 = MultiKeyDict(x=1, y=2, z=3)
multikeydict2 = MultiKeyDict([('x', 1), ('y', 2), ('z', 3)])

print(multikeydict1['x'])        # 1
print(multikeydict2['z'])        # 3
Особенностью класса MultiKeyDict должен являться метод alias(), который должен позволять давать имеющимся ключам псевдонимы. Обращение по созданному псевдониму не должно ничем отличаться от обращения по оригинальному ключу, то есть с момента создания псевдонима у значения становится два ключа (или больше, если псевдонимов несколько):

multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'z')     # добавление ключу 'x' псевдонима 'z'
multikeydict.alias('x', 't')     # добавление ключу 'x' псевдонима 't'
print(multikeydict['z'])         # 100
multikeydict['t'] += 1
print(multikeydict['x'])         # 101

multikeydict.alias('y', 'z')     # теперь 'z' становится псевдонимом ключа 'y'
multikeydict['z'] += [30]
print(multikeydict['y'])         # [10, 20, 30]
Значение должно оставаться доступным по псевдониму даже в том случае, если оригинальный ключ был удален:

multikeydict = MultiKeyDict(x=100)

multikeydict.alias('x', 'z')
del multikeydict['x']
print(multikeydict['z'])         # 100
Ключи должны иметь приоритет над псевдонимами. Если некоторые ключ и псевдоним совпадают, то все операции при обращении к ним должны выполняться именно с ключом:

multikeydict = MultiKeyDict(x=100, y=[10, 20])

multikeydict.alias('x', 'y')
print(multikeydict['y'])         # [10, 20]
"""


class MultiKeyDict:
    def __init__(self, *args, **kwargs):
        self._values = {}  # Основное хранилище значений
        self._primary_keys = {}  # {псевдоним: основной ключ}
        self._aliases = {}  # {основной ключ: [псевдонимы]}

        # Инициализация как у обычного dict
        if len(args) == 1 and isinstance(args[0], (list, tuple, dict)):
            items = args[0]
            if isinstance(items, dict):
                items = items.items()
            for key, value in items:
                self._values[key] = value
                self._aliases[key] = []
        else:
            for key, value in kwargs.items():
                self._values[key] = value
                self._aliases[key] = []

    def alias(self, original_key, alias_name):
        """Добавляет псевдоним для существующего ключа"""
        # Если псевдоним уже существует как оригинальный ключ - ничего не делаем
        if alias_name in self._values:
            return

        # Находим истинный оригинальный ключ (может быть псевдонимом)
        current_key = original_key
        while current_key in self._primary_keys:
            current_key = self._primary_keys[current_key]

        if current_key not in self._values:
            raise KeyError(f"Key '{original_key}' not found")

        # Если пытаемся создать псевдоним на самого себя - игнорируем
        if alias_name == current_key:
            return

        self._primary_keys[alias_name] = current_key
        self._aliases[current_key].append(alias_name)

    def __getitem__(self, key):
        """Получение значения по ключу или псевдониму"""
        # Сначала проверяем оригинальные ключи (они имеют приоритет)
        if key in self._values:
            return self._values[key]
        # Затем проверяем псевдонимы
        if key in self._primary_keys:
            primary_key = self._primary_keys[key]
            return self._values[primary_key]
        raise KeyError(key)

    def __setitem__(self, key, value):
        """Установка значения по ключу или псевдониму"""
        # Если ключ существует - обновляем значение
        if key in self._values:
            self._values[key] = value
        # Если это псевдоним - обновляем оригинальный ключ
        elif key in self._primary_keys:
            primary_key = self._primary_keys[key]
            self._values[primary_key] = value
        # Иначе создаем новый ключ
        else:
            self._values[key] = value
            self._aliases[key] = []

    def __delitem__(self, key):
        """Удаление ключа"""
        if key in self._values:
            # Если есть псевдонимы, делаем первый псевдоним новым ключом
            aliases = self._aliases[key]
            if aliases:
                new_primary = aliases[0]
                self._values[new_primary] = self._values[key]
                # Переносим оставшиеся псевдонимы
                self._aliases[new_primary] = aliases[1:]
                for alias in aliases[1:]:
                    self._primary_keys[alias] = new_primary
                # Обновляем primary_keys для нового ключа
                if new_primary in self._primary_keys:
                    del self._primary_keys[new_primary]
            del self._values[key]
            del self._aliases[key]
        elif key in self._primary_keys:
            primary_key = self._primary_keys[key]
            self._aliases[primary_key].remove(key)
            del self._primary_keys[key]
        else:
            raise KeyError(key)

    def __contains__(self, key):
        return key in self._values or key in self._primary_keys

    def __repr__(self):
        items = []
        for key, value in self._values.items():
            items.append(f"'{key}': {repr(value)}")
            for alias in self._aliases[key]:
                items.append(f"'{alias}'(alias to '{key}'): {repr(value)}")
        return "{" + ", ".join(items) + "}"

# TEST_3:
multikeydict = MultiKeyDict(lecture='python', lesson='object oriented programming')

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

multikeydict.alias('lecture', 'lesson')
print(multikeydict['lesson'])

del multikeydict['lesson']
print(multikeydict['lesson'])