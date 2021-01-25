# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

# Решение через **
def my_func_star(x, y):
    return x ** y


# Решение через цикл
def my_func_cycle(x, y):
    rez = 1
    for i in range(abs(y)):
        rez *= x
    if y >= 0:
        return rez
    else:
        return 1 / rez


try:
    x = int(input("Введите число x: "))
    y = int(input("Введите число y: "))
except:
    print("Ошибка, вы ввели не число")
else:
    print(my_func_star(x, y))
    print(my_func_cycle(x, y))
