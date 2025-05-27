"""Лог-файл — это текстовый файл, в который автоматически записывается важная информация о работе системы или программы. Форматов лог-файла довольно много, однако в рамках этой задачи будем считать, что все лог-файлы имеют следующий единый формат:

2022-01-01 INFO: User logged in
2022-01-01 ERROR: Invalid input data
2022-01-01 WARNING: File not found
2022-01-02 INFO: User logged out
2022-01-03 INFO: User registered
То есть каждая строка лог-файла описывает некоторое событие, которое характеризуется датой в формате YYYY-MM-DD, типом и кратким описанием.

Реализуйте функцию log_for(), которая принимает два аргумента в следующем порядке:

logfile — имя лог-файла
date_str — строковая дата в формате YYYY-MM-DD
Функция должна создавать текстовый файл с именем:

log_for_<date_str>.txt
и записывать в него все события из файла logfile, которые произошли в дату date_str. События должны записываться без указания даты, а также располагаться в своем исходном порядке."""



def  log_for(logfile, date_str):
    with open(logfile, 'r', encoding='utf-8') as file:
        with open(f"log_for_{date_str}.txt", 'w') as file1:
            for line in file:
                if line.startswith(date_str):
                    line1 = line.removeprefix(date_str + ' ')
                    file1.write(line1)

with open('log.txt', 'w', encoding='utf-8') as file:
    print('2022-01-01 INFO: User logged in', file=file)
    print('2022-01-01 ERROR: Invalid input data', file=file)
    print('2022-01-02 INFO: User logged out', file=file)
    print('2022-01-03 INFO: User registered', file=file)

log_for('log.txt', '2022-01-01')

with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
    print(file.read())

