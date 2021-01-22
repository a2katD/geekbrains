# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для его формирования используйте генератор.

from random import randint
from itertools import count

rand_list = [randint(0, 100) for i in range(10)]
print(f"Изначальный список {rand_list}")

new_list = [value for index, value in enumerate(rand_list) if value > rand_list[index - 1]]
print(f"Обработанный список {new_list}")
