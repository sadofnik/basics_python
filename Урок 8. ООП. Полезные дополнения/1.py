# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.


from datetime import datetime  # Импорт модуля datetime для проверки даты


class Date:
    def __init__(self, text):
        self.text = text

    @classmethod
    def my_m(cls, param):
        """Метод проверяет корректность введённых значений."""
        if all([i.isdigit() for i in param.split("-")]):
            return Date.valid(param)
        else:
            return f"{param} - Некорректная дата!"

    @staticmethod
    def valid(date):
        """Валидация даты. Проверяет есть ли такая дата в календаре через datetime."""
        try:
            valid_date = datetime.strptime(date, '%d-%m-%Y')
            return datetime.date(valid_date)
        except ValueError:
            return 'Такой даты нет!'


date = Date("25-01-2021")
print(date.my_m(date.text))
