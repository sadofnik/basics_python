# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность)
# на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать
# экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):

    def get_full_name(self):
        return f'Ф.И.О. сотрудника: {self.name} {self.surname}'

    def get_total_income(self):
        total_income = self._income.get('wage') + self._income.get("bonus")
        return f'Доход сотрудника: {total_income}'


# Проверка значения атрибутов
def data_question():
    user_name = input('Ваше имя: ').title()
    user_surname = input('Ваша фамилия: ').title()
    user_position = input('Ваша должность: ')
    user_wage = float(input('Ваш оклад: '))
    user_bonus = float(input('Ваша премия: '))

    return user_name, user_surname, user_position, user_wage, user_bonus


try:
    user = Position(*data_question())

    print(user.get_full_name())
    print(user.get_total_income())
except:
    print('Введены некорректные данные')
