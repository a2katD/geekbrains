# Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция вызывается следующим образом: for el in fact(n).
# Она отвечает за получение факториала числа.
# В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

# я не очень понял задание, сделал 2 варианта
def fact(n):
    rez = 1
    for i in range(1, n + 1):
        rez = rez * i
        yield rez


try:
    n = int(input("Введите число n: "))
except:
    print("Вы вели не число")
    quit()

for i, el in enumerate(fact(n)):
    print(f"Факториал числа {i + 1}! = {el}")

# вариант 2, тут сама функция факториал бесконечная, а n влияет только на цикл
from itertools import count


def factorial():
    rez = 1
    for i in count(1):
        rez = rez * i
        yield rez


iterator = factorial()

for i in range(n):
    print(f"Второй вариант, Факториал числа {i + 1}! = {next(iterator)}")
