# Обсуждали на уроке возможность вставки буквенных значений для итераций. Вы сказали попробовать дома.

class Iterator:
    """
    Объект-итератор
    """

    # Можно было сделать "вилку" для универсальности(числа, большие\маленькие буквы),
    # но я хотел именно проверить можно ли буквы поочередно вывести.

    def __init__(self, start, end):
        self.i = ord(start) - 1
        self.end = ord(end)

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i < self.end:
            return chr(self.i)
        else:
            raise StopIteration


for el in Iterator(start='a', end='j'):
    print(el)
