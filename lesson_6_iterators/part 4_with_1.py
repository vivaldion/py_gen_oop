"""Реализуйте функцию print_file_content(), которая принимает один аргумент:

filename — имя текстового файла
Функция должна выводить содержимое файла с именем filename. Если файла с данным именем нет в папке с программой, функция должна вывести текст:

Файл не найден
Примечание 1. Имя файла, передаваемого в функцию, уже содержит расширение.

Примечание 2. При открытии файла используйте явное указание кодировки UTF-8.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию print_file_content(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:"""

def print_file_content(filename):
    try:
        with open(f'{filename}', 'r', encoding="UTF-8") as file:
            lines = file.read()
            print(lines)
    except FileNotFoundError:
        print("Файл не найден")


with open('Precepts_of_Zote.txt', 'w', encoding='utf-8') as file:
    file.write('Сражения и путешествия берут своё')

print_file_content('Precepts_of_Zote.txt')