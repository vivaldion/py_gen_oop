"""
Предположим, что у нас имеется некоторая игра. За каждую игровую сессию игрок получает определенное количество баллов в зависимости от своего результата. Вашей задачей является реализация класса HighScorescores — таблицы рекордов, которую можно будет обновлять с учетом итоговых результатов игрока.

Изначально таблица рекордов является пустой. Максимальное количество рекордов указывается при создании таблицы:

high_score_scores = HighScorescores(3)
Таблица должна позволять просматривать текущие рекорды и добавлять новые результаты:

print(high_score_scores.scores)    # []
high_score_scores.update(10)
high_score_scores.update(8)
high_score_scores.update(12)
print(high_score_scores.scores)    # [12, 10, 8]
Текущие рекорды всегда должны располагаться в порядке убывания. Так как таблица содержит именно рекорды, то после заполнения таблицы добавляться должны только те результаты, которые лучше текущих:

high_score_scores.update(6)
high_score_scores.update(7)
print(high_score_scores.scores)    # [12, 10, 8]
high_score_scores.update(9)
print(high_score_scores.scores)    # [12, 10, 9]
Таблица должна поддерживать сброс всех результатов:

high_score_scores.reset()
print(high_score_scores.scores)    # []
"""


class HighScoreTable:
    def __init__(self, players):
        self.len = players
        self.scores = []

    def update(self, score):
        self.scores.append(score)
        self.scores = sorted(self.scores, reverse=True)[0:self.len ]

    def reset(self):
        self.scores.clear()

high_score_table = HighScoreTable(3)

print(high_score_table.scores)    # []
high_score_table.update(10)
high_score_table.update(8)
high_score_table.update(12)
print(high_score_table.scores)    # [12, 10, 8]

high_score_table.update(6)
high_score_table.update(7)
print(high_score_table.scores)    # [12, 10, 8]
high_score_table.update(9)
print(high_score_table.scores)    # [12, 10, 9]