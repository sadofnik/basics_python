# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
# деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек
# исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
# двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение
# количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.


class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):
        i = self.quantity - other.quantity
        if i < 0:
            return f"Некорректная операция, вычитание не может быть произведено"
        else:
            return i

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        i = self.quantity // other.quantity
        if i <= 0:
            return f"Число близко к нулю"
        else:
            return i

    def make_order(self, in_a_row):
        self.in_a_row = in_a_row
        print(f"Организация клеток по рядам: ")

        i = self.quantity
        while i > 0:
            if i > self.in_a_row:
                print('*' * self.in_a_row)
                i -= self.in_a_row
            else:
                print('*' * i)
                i -= i


a = Cell(23)
b = Cell(2)
print(f"Объединение двух клеток: {a + b}")
print(f"Разность количества двух клеток: {a - b}")
print(f"Произведение двух клеток: {a * b}")
print(f"Деление двух клеток: {a / b}")
a.make_order(5)
