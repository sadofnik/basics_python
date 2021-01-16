# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real_number, imaginary_number):
        self.real_number = real_number
        self.imaginary_number = imaginary_number

    def __add__(self, other):
        return ComplexNumber(self.real_number + other.real_number, self.imaginary_number + other.imaginary_number)

    def __mul__(self, other):
        return ComplexNumber(
            self.real_number * other.real_number + (self.imaginary_number * other.imaginary_number * -1),
            self.real_number * other.imaginary_number + self.imaginary_number * other.real_number)

    def __str__(self):
        if self.imaginary_number >= 0:
            return f"({self.real_number}+{self.imaginary_number}j)"
        else:
            return f"({self.real_number}+{self.imaginary_number}j)"


a = ComplexNumber(1, 3)
b = ComplexNumber(4, -5)
print(a + b)
print(f"Проверка: {complex(1, 3) + complex(4, -5)}")

c = ComplexNumber(1, -1)
d = ComplexNumber(3, 6)
print(c * d)
print(f"Проверка: {complex(1, -1) * complex(3, 6)}")
