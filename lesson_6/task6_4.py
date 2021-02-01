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
        self.is_police = True


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
