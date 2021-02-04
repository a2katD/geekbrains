# Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

from re import sub


def atoi(word):
    num = []
    for i in word.lstrip():
        if i.isdigit():
            num.append(i)
    return int("".join(num))


def sum_parser(string):
    total = 0
    words = string.split()
    for word in words:
        if word[0].isdigit():
            total += atoi(word)
    return total


journal = dict()
with open("task5_6.txt", "r", encoding="utf-8") as f:
    for string in f:
        journal[sub(":", "", (string.split()[0]))] = sum_parser(string)
print(journal)
