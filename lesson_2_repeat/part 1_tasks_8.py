'''Pycon
Каждый месяц в Сан-Диего организовывается встреча любителей Python, которая проходит в четвертый четверг месяца.

Напишите программу, которая определяет день проведения очередной встречи питонистов в Сан-Диего.

Формат входных данных
На вход программе подается два натуральных числа, представляющие год и месяц, каждое на отдельной строке.

Формат выходных данных
Программа должна определить день проведения встречи в Сан-Диего в указанных году и месяце и вывести результат в формате DD.MM.YYYY.'''

from datetime import datetime
import calendar

year, month = int(input()), int(input())


while True:
    cal = calendar.Calendar().monthdays2calendar(year, month)
    if cal[0][3][0] == 0 and cal[4][3][0] != 0:
        day = cal[4][3][5]
        break
    elif cal[0][3][0] != 0 and cal[3][3][3] != 0:
        day = cal[3][3][3]
        break
    else:
        month += 1
print(datetime(year,month, day).strftime('%d.%m.%Y'))






