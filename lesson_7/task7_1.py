# Добавить проверку через лен на то какой размер матрицы больше
# и создавать новую матрицу на основе максимального размера

class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        new_matrix = self.matrix_list
        for index_1, value_1 in enumerate(new_matrix):
            for index_2, value_2 in enumerate(value_1):
                new_matrix[index_1][index_2] += other[index_1][index_2]
        return new_matrix

    def __getitem__(self, index):
        return self.matrix_list[index]

    def __str__(self):
        for i in self.matrix_list:
            for j in i:
                print(j, end=" ")
            print()
        return ""


m = Matrix([[1, 2, 3], [4, 5, 6]])
b = Matrix([[7, 8, 9], [10, 11, 12]])
print(m + b)
