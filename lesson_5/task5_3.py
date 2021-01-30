with open("task5_3.txt", "r", encoding="utf-8") as f:
    total = 0
    for i, line in enumerate(f):
        family, salary = line.split()
        if float(salary) < 20000:
            print(f"Сотрудник {family} имеет оклад {salary}")
        total += float(salary)
    print(f"Средняя величина дохода сотрудников {round(total / i , 2)}")
