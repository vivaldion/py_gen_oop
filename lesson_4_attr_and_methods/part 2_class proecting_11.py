'''Будем называть словом любую последовательность из одной или более букв. Текстом будем считать набор слов, разделенных пробельными символами.

Реализуйте класс TextHandler, описывающий изначально пустой расширяемый набор слов. При создании экземпляра класс не должен принимать никаких аргументов.

Экземпляр класса TextHandler должен иметь три метода:

add_words() — метод, принимающий в качестве аргумента текст и добавляющий слова из данного текста в набор
get_shortest_words() — метод, возвращающий актуальный список самых коротких слов в наборе
get_longest_words() — метод, возвращающий актуальный список самых длинных слов в наборе
Примечание 1. Слова в списках, возвращаемых методами get_shortest_words() и get_longest_words(), должны располагаться в том порядке, в котором они были добавлены в набор.

Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.'''

class TextHandler:
    def __init__(self):
        self.words = []
    def add_words(self, text:str):
        self.words.extend(text.split())
    def get_shortest_words(self):
        return [i for i in self.words if len(i) == len(min(self.words, key=len))]
    def get_longest_words(self):
        return [i for i in self.words if len(i) == len(max(self.words, key=len))]


texthandler = TextHandler()

texthandler.add_words('do not be sorry')
texthandler.add_words('be')
texthandler.add_words('better')

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())