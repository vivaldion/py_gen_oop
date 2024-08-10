'''Функция intersperse()
Реализуйте генераторную функцию intersperse(), которая принимает два аргумента в следующем порядке:

iterable — итерируемый объект
delimiter — значение-разделитель
Функция должна возвращать генератор, порождающий последовательность из элементов итерируемого объекта iterable, между которыми располагается значение-разделитель delimiter.'''


def intersperse(iterab, separator):
    flag = False
    for i in iterab:
        if  flag:
            yield separator
        yield i
        flag = True







