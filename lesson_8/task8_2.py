# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyBadNameError(Exception):
    pass
    # def __init__(self, dividend, divider):
    #     self.dividend = dividend
    #     self.divider = divider


dividend = int(input('Введите делимое: '))
divider = int(input('Введите делитель: '))

try:
    print(dividend/divider)
except:
    MyBadNameError()