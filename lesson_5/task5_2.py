with open("task5_2.txt", "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        print(f"В строке №{i + 1} содержится {len(line.split())} слова")
    print(f"В файле содержится {i + 1} строк")
