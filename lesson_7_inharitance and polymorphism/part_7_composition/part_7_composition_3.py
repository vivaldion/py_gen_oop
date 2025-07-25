'''1. Реализуйте класс Card, описывающий игральную карту. При создании экземпляра класс должен принимать два аргумента в следующем порядке:

suit — масть игральной карты, представленная одним из следующих символов:
♣, ♢, ♡, ♠
rank — ранг игральной карты, представленный одним из следующих символов или парой символов:
2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
Экземпляр класса Card должен иметь следующее неформальное строковое представление:

<масть игральной карты><ранг игральной карты>
2. Также реализуйте класс данных Deck, описывающий классическую колоду из 52 игральных карт. Карты в колоде должны быть расположены сперва в порядке возрастания мастей, а затем — в порядке возрастания рангов. При создании экземпляра класс не должен принимать никаких аргументов.

Класс Deck должен иметь два метода экземпляра:

shuffle() — метод, перемешивающий все карты в колоде. Перемешивать колоду можно только в том случае, если в колоде на данный момент находятся все 52 карты. Если в колоде меньше 52 карт, должно быть возбуждено исключение ValueError с текстом:
Перемешивать можно только полную колоду
deal() — метод, удаляющий из колоды последнюю карту и возвращающий ее. Если колода пуста, должно быть возбуждено исключение ValueError с текстом:
Все карты разыграны
Экземпляр класса Deck должен иметь следующее неформальное строковое представление:

Карт в колоде: <текущее количество карт в колоде>
Примечание 1. Порядок старшинства карточных рангов от младшего к старшему:

2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
Порядок старшинства карточных мастей от младшего к старшему:

♣, ♢, ♡, ♠
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.

Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.'''


import random

suits = ("♣", "♢", "♡", "♠")
ranks = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.suit+ self.rank


class Deck:
    def __init__(self):
        self.deck = [Card(s,r) for s in suits for r in ranks]

    def deal(self):
        if self.deck:
            return self.deck.pop()
        else:
            raise ValueError('Все карты разыграны')

    def shuffle(self):
        if len(self.deck) == 52:
            random.shuffle(self.deck)
        else:
            raise ValueError('Перемешивать можно только полную колоду')

    def __str__(self):
        return f'Карт в колоде: {len(self.deck)}'


deck = Deck()

deck.shuffle()

for _ in range(50):
    print(deck.deal())