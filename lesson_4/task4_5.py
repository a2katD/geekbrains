# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы).
# Нужно получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce


def multiplication(num_1, num_2):
    return num_1 * num_2

num_list = [num for num in range(100, 1001, 2)]

# или вот так
#num_list = [num for num in range(100, 1001) if num % 2 == 0]

print(num_list)
print(reduce(multiplication, num_list))
