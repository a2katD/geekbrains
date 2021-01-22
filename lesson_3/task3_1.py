# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(dividend, divider):
    try:
        return dividend / divider
    except ZeroDivisionError:
        print("Ошибка, деление на ноль")


try:
    dividend = int(input("Введите делимое: "))
    divider = int(input("Введите делитель: "))
except:
    print("Ошибка, неверные параметры")
else:
    if division(dividend, divider):
        print(division(dividend, divider))
