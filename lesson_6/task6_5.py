class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки Ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки Карандашом")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки Маркером")


pen = Pen("Синяя ручка")
pencil = Pencil("Красный карандаш")
handle = Handle("Черный фломастер")
pen.draw()
pencil.draw()
handle.draw()
