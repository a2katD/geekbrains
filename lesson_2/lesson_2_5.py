# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
import random

my_list = [i for ]
user_value = int(input("Введите новый элемент рейтинга\n"))
i = 0
for value in my_list:
    if value < user_value:
        my_list.insert(i, user_value)
        break
    i += 1
    if i == len(my_list):
        my_list.append(user_value)
        break
print(*my_list)
# запустить рандом