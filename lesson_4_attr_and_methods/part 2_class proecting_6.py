'''Класс Gun
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Gun должен иметь один метод экземпляра:

shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее'''
from itertools import cycle

class Gun:
    def __init__(self):
        self.sh = cycle(iter(('pif', 'paf')))
    def shoot(self):
        print(next(self.sh))
gun = Gun()

gun.shoot()
gun.shoot()
gun.shoot()
gun.shoot()