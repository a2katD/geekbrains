# Второе задание
time = int(input("Введите время в секундах: "))
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print(f"{hour:02}:{minutes:02}:{seconds:02}")

# # Третье задание
n = input("Введиче число n: ")
print(int(n) + int(n + n) + int(n + n + n))

# Четверное задание
x = input("Введиче целове положительное число: ")
i = 0
maximum = 0
while (i < len(x)):
    if int(x[i]) > maximum:
        maximum = int(x[i])
    i += 1
print(maximum)

# # Пятое задание
proceeds = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))

if proceeds > costs:
    profit = proceeds - costs
    print("У Вас прибыль " + str(profit))
    print("Рентабельность выручки составляет " + str(round(profit / proceeds * 100, 2)) + "%")
    staff = int(input("Введите количество сотрудников: "))
    print("Прибыль фирмы на 1 сотрудника составляет " + str(round(proceeds / staff, 2)))
elif proceeds == costs:
    print("Вы отработали в ноль")
else:
    print("У Вас убытки " + str(abs(proceeds - costs)))

# Задание шестое
a = int(input("Сколько составил результат в 1 день? "))
b = int(input("Какого результата необходимо достигнуть? "))
day = 1
while (a < b):
    a += a * 0.1
    day += 1
print(f"на {day}-й день спортсмен достиг результата — не менее {b} км.")
