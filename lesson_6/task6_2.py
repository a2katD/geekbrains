class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_masses(self, depth=1):
        print(f"Масса асфальта будет равна: {self._length * self._width * 25 * depth} кг")


try:
    length = int(input("Введите длинну дороги в метрах: "))
    width = int(input("Введите ширину дороги в метрах: "))
    depth = int(input("Введите толщину асфальта в сантиметрах: "))
    r = Road(length, width)
    r.asphalt_masses(depth)
except:
    print("Введены некорректные данные")
