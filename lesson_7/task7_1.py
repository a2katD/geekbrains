# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __add__(self, other):
        new_matrix = self.matrix_list
        for index_1, value_1 in enumerate(other):
            if len(new_matrix) < index_1 + 1:
                new_matrix.append(other[index_1])
            else:
                for index_2, value_2 in enumerate(value_1):
                    if len(new_matrix[index_1]) < index_2 + 1:
                        new_matrix[index_1].append(other[index_1][index_2])
                    else:
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
b = Matrix([[7, 8, 9, 5, 2], [10, 11, 12, 5], [20, 30, 40, 50]])
print(b)
