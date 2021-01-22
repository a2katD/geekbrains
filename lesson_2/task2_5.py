# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
import random as rd

my_list = sorted([rd.randint(1, 100) for i in range(10)], reverse=True)
print(f"Имеется следующий рейтинг: {' '.join(map(str, my_list))}")
while True:
    user_value = input("Введите новый элемент рейтинга\n")
    if not user_value.isdigit():
        print("Введено некорректное значение, необходимо ввести число")
    else:
        user_value = int(user_value)
        break
num = 0
for value in my_list:
    if value < user_value:
        my_list.insert(num, user_value)
        break
    num += 1
    if num == len(my_list):
        my_list.append(user_value)
        break
print(f"Обновленный рейтинг: {' '.join(map(str, my_list))}")
