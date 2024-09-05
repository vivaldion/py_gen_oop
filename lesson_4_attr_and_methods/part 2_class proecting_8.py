

class Scales:
    def __init__(self, left=0, right=0):
        self.left = left
        self.right = right
    def add_right(self, n):
        self.right += n
    def add_left(self, n):
        self.left +=n

    def get_result(self):
        if self.right == self.left:
            print('Весы в равновесии')
        else:
            return (f'{("Левая", "Правая")[self.right > self.left]} чаша тяжелее')

scales = Scales()

scales.add_right(2)
scales.add_left(1)

print(scales.get_result())