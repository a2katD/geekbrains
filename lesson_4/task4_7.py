# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

from itertools import count


def fact(n):
    rez = 1
    for i in range(1, n + 1):
        rez = rez * i
        yield rez


n = int(input("Введите число n: "))
i = 1
for el in fact(n):
    print(f"Факториал числа {i}! = {el}")
    i += 1
