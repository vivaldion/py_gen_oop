"""
1. Реализуйте класс Weekday, описывающий перечисление с днями недели. Перечисление должно иметь семь элементов:

MONDAY — элемент со значением 0
TUESDAY — элемент со значением 1
WEDNESDAY — элемент со значением 2
THURSDAY — элемент со значением 3
FRIDAY — элемент со значением 4
SATURDAY — элемент со значением 5
SUNDAY — элемент со значением 6
2. Также реализуйте класс NextDate, который позволяет определять следующую ближайшую дату, соответствующую указанному дню недели: например, дату ближайшего вторника или дату ближайшей пятницы. При создании экземпляра класс должен принимать три аргумента в следующем порядке:

today — текущая дата, представленная экземпляром класса date. Относительно этой даты должна определяться следующая ближайшая дата, соответствующая некоторому дню недели
weekday — день недели, представленный элементом перечисления Weekday
considering_today — булево значение, по умолчанию равняется False
Параметр considering_today должен определять, учитывается ли дата today при определении даты, соответствующей дню недели weekday. Если параметр имеет значение True, дата today должна учитываться, если False — не учитываться. Например, если день недели даты today равен weekday и параметр considering_today равен True, то искомой датой, соответствующей дню недели weekday, будет являться сама дата today.

Класс NextDate должен иметь два метода экземпляра:

date() — метод, возвращающий следующую ближайшую (относительно даты today) дату, соответствующую дню недели weekday, в виде экземпляра класса date
days_until() — метод, возвращающий количество дней до следующей ближайшей (относительно даты today) даты, соответствующей дню недели weekday
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.
"""


from enum import Enum
from datetime import date, timedelta

Weekday = Enum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'],start = 0)


class NextDate:
    today : date

    def __init__(self, today, weekday, considering_today= False):
        self.today = today
        self.weekday = weekday
        self.considering_today = considering_today

    def date(self):
        today = self.today.weekday()
        weekday = self.weekday.value
        if self.considering_today and today == weekday:
            return self.today
        days = weekday - today
        if days <= 0:
            days += 7
        return self.today + timedelta(days=days)

    def days_until(self):
        return (self.date() - self.today).days

