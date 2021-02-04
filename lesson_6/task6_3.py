class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        print(f"{self.surname} {self.name}")

    def get_total_income(self):
        wage = self._income.get("wage")
        bonus = self._income.get("bonus")
        print(f"Доход с учетом премии {wage + bonus}")


p = Position("Павел", "Воронов", "ИП", {"wage": 1000, "bonus": 500})
p.get_total_income()
p.get_full_name()
