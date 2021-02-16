# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

class StorageError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class Storage:
    def __init__(self):
        self.storage = dict()

    def __str__(self):
        print("На складе имеется:")
        for key in self.storage:
            if self.storage[key] != 0:
                print(f"{key.name} в колличестве {self.storage[key]}")
        return f"Конец интентаризации"

    def reception(self, unit, quantity:int):
        if not isinstance(unit, OfficeEquipment):
            raise StorageError("Нельзя оприховать не оргтехнику")
        elif not quantity or quantity <= 0:
            raise StorageError("Неверное количество")
        elif unit in self.storage:
            self.storage[unit] += quantity
            print(f"{unit.name} в колличестве {quantity} поступил на склад")
        else:
            self.storage[unit] = quantity
            print(f"{unit.name} в колличестве {quantity} поступил на склад")

    def broadcast(self, unit, quantity:int):
        if not unit in self.storage:
            raise StorageError(f"На складе нет {unit}")
        elif quantity <= 0:
            raise StorageError("Неверное количество")
        elif self.storage[unit] - quantity < 0:
            raise StorageError(f"На складе нет столько единиц {unit}")
        else:
            self.storage[unit] -= quantity
            print(f"{unit.name} в колличестве {quantity} был передан со склада")


class OfficeEquipment:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Printer(OfficeEquipment):
    def __init__(self, name, color, print_color):
        super().__init__(name, color)
        self.print_color = print_color


class Scanner(OfficeEquipment):
    def __init__(self, name, color, type_size):
        super().__init__(name, color)
        self.type_size = type_size


class Copier(OfficeEquipment):
    def __init__(self, name, color, print_color, type_size):
        super().__init__(name, color)
        self.print_color = print_color
        self.type_size = type_size


mystorage = Storage()
hp600 = Printer("HP600", "Blue", "White-Black")
scanner_cano = Scanner("CanoScan", "Red", "A4")
phaser = Copier("phaser", "Black", "multicolored", "A3")

mystorage.reception(hp600, 10)
mystorage.reception(scanner_cano, 1)
mystorage.reception(phaser, 3)

mystorage.broadcast(hp600, 5)
print(mystorage)