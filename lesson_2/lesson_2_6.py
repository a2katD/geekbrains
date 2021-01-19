# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

products = []
print("Давайте заполним табилцу с товарами")
while True:
    quantity = input("Для начала введите, сколько всего наименований имеется\n")
    if not quantity.isdigit():
        print("Вы ввели некорректное значение, нужно ввести число")
        continue
    else:
        quantity = int(quantity)
        break
i = 0
while i < quantity:
    user_data = input("Введите через пробел: Название, цену, количество, и единицу измерения\n").split()
    if len(user_data) != 4 or not user_data[1].isdigit() or not user_data[2].isdigit():
        print("Вы ввели некорректное значение, попробуйте еще раз")
        continue
    products.append(
        (i + 1,
         {"название": user_data[0], "цена": int(user_data[1]), "количество": int(user_data[2]), 'ед': user_data[3]}))
    i += 1
analytics = \
    {
        "название": [],
        "цена": [],
        "количество": [],
        "ед": []
    }
for i in range(quantity):
    analytics["название"].append(products[i][1]["название"])
    analytics["цена"].append(products[i][1].get("цена"))
    analytics["количество"].append(products[i][1]["количество"])
    analytics["ед"].append(products[i][1].get("ед"))
analytics["ед"] = list(set(analytics.get("название")))
analytics["ед"] = list(set(analytics.get("цена")))
analytics["ед"] = list(set(analytics.get("количество")))
analytics["ед"] = list(set(analytics.get("ед")))
print(analytics)
