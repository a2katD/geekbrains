# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    return arg_1 + arg_2 + arg_3 - min(arg_1, arg_2, arg_3)


try:
    arg_1 = int(input("Введите первоче число: "))
    arg_2 = int(input("Введите второе число: "))
    arg_3 = int(input("Введите третье число: "))
except:
    print("Ошибка, вы ввели не число")
else:
    print(my_func(arg_1, arg_2, arg_3))
