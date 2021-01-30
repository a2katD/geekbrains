def atoi(word):
    num = []
    for i in word:
        if i.isdigit():
            num.append(i)
    return "".join(num)


def sum_parser(string):
    total = 0
    words = string.split()
    for word in words:
        if word[0].isdigit():
            total += int(atoi(word))
    return total


journal = dict()
with open("task5_6.txt", "r", encoding="utf-8") as f:
    for string in f:
        total = sum_parser(string)
        journal[(string.split()[0][:-1])] = total
print(journal)
