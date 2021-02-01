# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

transfer = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task5_4_read.txt", "r", encoding="utf-8") as file_read:
    with open("task5_4_write.txt", "w", encoding="utf-8") as file_write:
        for line in file_read:
            line = line.split()
            line[0] = transfer[line[0]]
            file_write.writelines(" ".join(line) + "\n")
