from itertools import count

class Cell:
    def __init__(self, count):
        self.count = count

    def __int__(self):
        return int(self.count)

    def __add__(self, other):
        return self.count + int(other)

    def __sub__(self, other):
        if self.count - int(other) > 0:
            return self.count - int(other)
        else:
            print("Ошибка, Разность количества ячеек двух клеток меньше или равна нулю")

    def __mul__(self, other):
        return self.count * int(other)

    def __truediv__(self, other):
        return self.count // int(other)

    def make_order(self, cells_row):
        ch = '*'
        string = ""
        line = 0
        for i in range(self.count):
            line += 1
            string = string + ch
            if line == cells_row:
                line = 0
                string = string + '\n'
        return string

cell_1 = Cell(12)
cell_2 = Cell(5)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(5))
