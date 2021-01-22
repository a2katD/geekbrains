# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

if len(argv) != 4:
    print("""Invalid number of parameters entered
    You must enter:
    1) Productivity in hours
    2) Rate per hour
    3) Amount of premium""")
    exit()

work_hours, rate, premium = argv[1:]

try:
    wage = int(work_hours) * int(rate) + int(premium)
    print(f'salary was: {wage}')
except:
    print("You entered not a number")
