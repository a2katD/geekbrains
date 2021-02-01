# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

numbers = [randint(1, 100) for i in range(randint(1, 20))]
with open("task5_5.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(map(str, numbers)))

with open("task5_5.txt", "r", encoding="utf-8") as f:
    numbers = map(int, f.read().split())
    print(f"Сумма всех значений из файла = {sum(numbers)}")
