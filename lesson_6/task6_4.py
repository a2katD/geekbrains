# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

from random import choice


class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.name} поехал")

    def stop(self):
        print(f"Автомобиль {self.name} остановился")

    def turn(self, direction):
        print(f"Автомобиль {self.name} повернул {direction}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} = {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Автомобиль {self.name} превысил допустимую скорость {self.speed}")
        else:
            print(f"Текущая скорость автомобиля {self.name} = {self.speed}")


class SportCar(Car):
    def go(self):
        print(f"Спорткар {self.name} за считанные секунды разогнался до {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Автомобиль {self.name} превысил допустимую скорость {self.speed}")
        else:
            print(f"Текущая скорость автомобиля {self.name} = {self.speed}")


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


police = PoliceCar("AUDI", "White-Blue", 120)
tractor = WorkCar("ZIL", "Brown", 30)
deputy = TownCar("BMW", "Red", 100)
autobus = WorkCar("AutoBus", "Green", 50)
taxi = TownCar("Toyota", "Yellou", 60)
major = SportCar("lamborghini", "White", 200)
cars = [police, tractor, deputy, autobus, taxi, major]

for car in cars:
    print(f"Автомобиль {car.name} имеет окраску {car.color}")
    if car.is_police == True:
        print(f"Автомобиль {car.name} является полцейской машиной!")
    car.go()
    rd = choice(["", "Направо", "Налево"])
    if rd:
        car.turn(rd)
    car.show_speed()
    car.stop()
    print()
