# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в
# этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и
# рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, clot_name, size):
        self.name = clot_name
        self.size = size

    @abstractmethod
    def expend(self):
        pass

    def __add__(self, other):
        return self.expend + other.expend


class Coat(Clothes):
    def __init__(self, clot_name, coat_size):
        super().__init__(clot_name, size=coat_size)
        self.V = coat_size

    @property
    def expend(self):
        return self.V / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, clot_name, costume_size):
        super().__init__(clot_name, size=costume_size)
        self.H = costume_size

    @property
    def expend(self):
        return self.H * 2 + 0.3


a = Coat("Летнее пальто", 22.75)
print(a.expend)
b = Costume("Костюм Тройка", 1.35)
print(b.expend)
print(f"Суммарный расход ткани: {a.expend + b.expend}")  # Указывая метод, можно передавать больше 2х значений
