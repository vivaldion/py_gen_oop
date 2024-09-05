'''Класс Knight должен иметь четыре метода экземпляра:

get_char() — метод, возвращающий символ N
can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае
move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтальной и по вертикальной осям и заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку с указанными координатами, его координаты должны остаться неизменными
draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может переместиться конь, — символом *
Примечание 1. Шахматное поле имеет вид:



Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.'''

class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color

    def get_char(self):
        return 'N'
    def can_move(self, hor, vert):
        horizonal =ord(self.horizontal) - 97
        vertical = int(self.vertical)
        hor = ord(hor) - 97
        return (abs(horizonal - hor) == 1 and abs(vert - vertical) == 2) or (abs(horizonal - hor) == 2 and abs(vertical - vert) == 1)
    def move_to(self, hor, vert):
        horizonal = ord(self.horizontal) - 97
        vertical = int(self.vertical)
        hor = ord(hor) - 97
        if (abs(horizonal - hor) == 1 and abs(vert - vertical) == 2) or (
                    abs(horizonal - hor) == 2 and abs(vertical - vert) == 1):
            self.horizontal = chr(hor + 97)
            self.vertical = vert
    def draw_board(self):
        board = [['.'] * 8 for _ in range(8)]
        horizontal = ord(self.horizontal) - 97
        vertical = 8 - self.vertical
        board[vertical][horizontal] = 'N'
        for i in range(8):
            for j in range(8):
                if abs(vertical - i) * abs(horizontal - j) == 2:
                    board[i][j] = '*'
        for row in board:
            print(*row, sep='')

knight = Knight('c', 3, 'white')

print(knight.horizontal, knight.vertical)
print(knight.can_move('e', 5))
print(knight.can_move('e', 4))

knight.move_to('e', 4)
print(knight.horizontal, knight.vertical)
knight = Knight('c', 3, 'white')

knight.draw_board()