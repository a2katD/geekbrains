# Создать (не программно) текстовый файл, в котором каждая строка должна содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Итоговый список сохранить в виде json-объекта в соответствующий файл.

from json import dump

profit = dict()
average = {"average_profit": 0, "count": 0}

with open("task5_7.txt", "r", encoding="utf-8") as f:
    for company in f:
        name, ownership, proceeds, damages = company.split()
        profit[name] = int(proceeds) - int(damages)
        if profit[name] > 0:
            average["average_profit"] += profit[name]
            average["count"] += 1

average["average_profit"] = int(average["average_profit"] / average["count"])
del average["count"]

json_object = list()
json_object.append(profit)
json_object.append(average)

with open("task5_7.json", "w", encoding="utf-8") as js:
    dump(json_object, js, ensure_ascii=False, indent=4)
