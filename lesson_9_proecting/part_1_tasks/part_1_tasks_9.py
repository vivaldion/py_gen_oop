"""
Класс TicTacToe
Реализуйте класс TicTacToe для игры в Крестики-Нолики. Экземпляр класса TicTacToe должен представлять собой игровое поле из трех строк и трех столбцов, на котором игроки по очереди могут помечать свободные клетки. Первый ход делает игрок, ставящий крестики:

tictactoe = TicTacToe()

tictactoe.mark(1, 1)         # помечаем крестиком клетку с координатами (1; 1)
tictactoe.mark(3, 1)         # помечаем ноликом клетку с координатами (3; 1)
Помечать уже помеченные клетки нельзя. При попытке сделать это должен быть выведен текст Недоступная клетка:

tictactoe.mark(1, 1)         # Недоступная клетка

tictactoe.mark(1, 3)         # помечаем крестиком клетку с координатами (1; 3)
tictactoe.mark(1, 2)         # помечаем ноликом клетку с координатами (1; 2)
tictactoe.mark(3, 3)         # помечаем крестиком клетку с координатами (3; 3)
tictactoe.mark(2, 2)         # помечаем ноликом клетку с координатами (2; 2)
tictactoe.mark(2, 3)         # помечаем крестиком клетку с координатами (2; 3)
С помощью метода winner() должна быть возможность узнать победителя игры. Метод должен вернуть:

символ X, если победил игрок, ставящий крестики
символ O, если победил игрок, ставящий нолики
строку Ничья, если произошла ничья
значение None, если победитель еще не определен
print(tictactoe.winner())    # X
Помечать клетки после завершения игры нельзя. При попытке сделать это должен быть выведен текст Игра окончена:

tictactoe.mark(2, 1)         # Игра окончена
С помощью метода show() должна быть возможность посмотреть текущее состояние игрового поля. Оно должно быть построено из символов | и -, а также X и O, если игроками были сделаны какие-либо ходы. Для приведенного выше поля tictactoe вызов tictactoe.show() должен вывести следующее:

X|O|X
-----
 |O|X
-----
O| |X
"""


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner_status = None

    def mark(self, row, col):
        if self.game_over:
            print("Игра окончена")
            return

        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Недоступная клетка")
            return

        if self.board[row - 1][col - 1] != ' ':
            print("Недоступная клетка")
            return

        self.board[row - 1][col - 1] = self.current_player

        if self.check_winner():
            self.winner_status = self.current_player
            self.game_over = True
        elif self.is_board_full():
            self.winner_status = "Ничья"
            self.game_over = True
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):

        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True


        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True


        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def winner(self):
        return self.winner_status

    def show(self):
        for i in range(3):
            print("|".join(self.board[i]))
            if i < 2:
                print("-----")

tictactoe = TicTacToe()
tictactoe.show()

