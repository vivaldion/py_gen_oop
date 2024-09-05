'''Класс Gun
Реализуйте класс Gun, описывающий ружье. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Gun должен иметь три метода экземпляра:

shoot() — метод, при первом вызове которого выводится строка pif, при втором — paf, при третьем — pif, при четвертом — paf, и так далее
shots_count() — метод, возвращающий актуальное количество вызовов метода shoot()
shots_reset() — метод, сбрасывающий количество вызовов метода shoot() до нуля'''
from itertools import cycle

class Gun:
    def __init__(self):
        self.sh = cycle(('pif', 'paf'))
        self.counter = 0
    def shoot(self):
        print(next(self.sh))
        self.counter += 1
    def shots_count(self):
        return self.counter
    def shots_reset(self):
        self.counter = 0
        self.sh = cycle(('pif', 'paf'))

gun = Gun()
gun.shoot()
print(gun.shots_count())
gun.shots_reset()
print(gun.shots_count())
gun.shoot()
gun.shoot()