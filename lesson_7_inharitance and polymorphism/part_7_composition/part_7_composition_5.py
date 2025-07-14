""". Реализуйте класс Lecture, описывающий некоторое выступление. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

topic — тема выступления
start_time — время начала выступления в виде строки в формате HH:MM
duration — длительность выступления в виде строки в формате HH:MM
2. Также реализуйте класс Conference, описывающий конференцию, протяженностью в один день. Конференция представляет собой набор последовательных выступлений. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Conference должен иметь четыре метода экземпляра:

add() — метод, принимающий в качестве аргумента выступление и добавляющий его в конференцию. Если выступление пересекается по времени с другими выступлениями, должно быть возбуждено исключение ValueError с текстом:
Провести выступление в это время невозможно
total() — метод, возвращающий суммарную длительность всех выступлений в конференции в виде строки в формате HH:MM
longest_lecture() — метод, возвращающий длительность самого долгого выступления в конференции в виде строки в формате HH:MM
longest_break() — метод, возвращающий длительность самого долгого перерыва между выступлениями в конференции в виде строки в формате HH:MM
Примечание 1. Перерыв между выступлениями может быть нулевым. Другими словами, одно выступление может заканчиваться, например, в 12:00, а другое начинаться в 12:00.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными."""


from datetime import timedelta
from functools import reduce

class Lecture:
    def __init__(self, topic, start_time, duration):
        self.d = duration
        self.topic = topic
        hh, mm = list(map(int, start_time.split(':')))
        self.start_time = timedelta(hours=hh, minutes=mm).total_seconds() // 60
        hh, mm = list(map(int, duration.split(':')))
        self.duration = timedelta(hours=hh, minutes=mm).total_seconds() // 60
        self.end_time = self.start_time + self.duration

class Conference:
    conf : list[Lecture]
    def __init__(self):
        self.conf = []

    def add(self, lecture: Lecture):
        if any(lecture.start_time < l.end_time and l.start_time < lecture.end_time for l in self.conf):
            raise ValueError('Провести выступление в это время невозможно')
        self.conf.append(lecture)
        self.conf.sort(key=lambda x: x.start_time)

    def longest_lecture(self):
        return f'{max(self.conf, key=lambda x: x.duration).d}'

    def total(self):
        total =  reduce(lambda x, y: x + y.duration, self.conf, 0)
        return f'{int(total // 60):02}:{int(total % 60):02}'

    def longest_break(self):
        if len(self.conf) < 2:
            return '00:00'
        diff = max([b.start_time - a.end_time for a, b in zip(self.conf, self.conf[1:])])
        return f'{int(diff // 60):02}:{int(diff % 60):02}'

conference = Conference()
conference.add(Lecture('Муравьиный алгоритм', '09:30', '02:00'))
conference.add(Lecture('Жизнь после ChatGPT', '11:45', '04:00'))
conference.add(Lecture('Простые числа', '08:00', '01:30'))

print(conference.longest_lecture())
print(conference.longest_break())