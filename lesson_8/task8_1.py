# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, str_data):
        self.str_data = str_data

    @staticmethod
    def validation(day, month, year):
        months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if year % 4 == 0:
            months[2] = 29
        if year < 0:
            return None
        elif month < 1 or month > 12:
            return None
        elif day < 1 or day > months[month]:
            return None
        else:
            return True

    @classmethod
    def swap_to_int(cls, str_data):
        if len(str_data.split("-")) != 3:
            return f"Неверный формат даты"
        day, month, year = str_data.split("-")
        return day, month, year


d = Data("11-12-2000")
print(Data.validation(29, 2, 2020))
print(Data.validation(12, 90, 2021))
print(Data.validation(29, 11, -1))
print(d.validation(1, 1, 2000))

print(Data.swap_to_int("11-12-2000"))
print(d.swap_to_int("11-12-2000"))
