from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def need_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size

    @property
    def need_cloth(self):
        return f"Потребуется {round(self.size / 6.5 + 0.5, 2)} ткани"


class Costume(Clothes):
    def __init__(self, growth):
        self.growth = growth

    @property
    def need_cloth(self):
        return f"Потребуется {self.growth * 2 + 0.3} ткани"


a = Costume(14)
b = Coat(175)
print(a.need_cloth)
print(b.need_cloth)
