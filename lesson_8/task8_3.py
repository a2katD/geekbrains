# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные
# и заполнять список необходимо только числами. Класс-исключение должен контролировать типы данных элементов списка.

class ListIntError:
    def __init__(self):
        self.values = []

    def check_input(self):
        while True:
            try:
                value = input("Введите значение, для остановки stop: ")
                if value.lower() == "stop":
                    break
                self.values.append(int(value))
            except:
                print("Вы ввели неверное значение, попробуйте еще, для остановки stop: ")
        return self.values

test = ListIntError()
print(test.check_input())