transfer = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("task5_4_read.txt", "r", encoding="utf-8") as file_read:
    with open("task5_4_write.txt", "w", encoding="utf-8") as file_write:
        for line in file_read:
            line = line.split()
            line[0] = transfer[line[0]]
            file_write.writelines(" ".join(line) + "\n")
