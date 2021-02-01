# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.

from random import randint

num_list = [randint(0, 10) for i in range(14)]
print(f"Изначальный список {num_list}")
new_list = [i for i in num_list if num_list.count(i) == 1]
print(f"Обработанный список {new_list}")
