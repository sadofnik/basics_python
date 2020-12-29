# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что
# машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_polise=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def go(self):
        return f'{self.name} едет'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула {direction}'

    def show_speed(self):
        return f'Скорость {self.name} составляет: {self.speed} км\ч'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.name} едет с превышением скорости'
        else:
            return Car.show_speed(self)


class SportCar(Car):
    def show_speed(self):
        if self.speed > 100:
            return f'{self.name} едет с превышением скорости'
        else:
            return Car.show_speed(self)


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'{self.name} едет с превышением скорости'
        else:
            return f'Скорость {self.name} составляет: {self.speed} км\ч'


class PoliceCar(Car):
    def expection(self):
        return f'{self.name} патрулирует город'

    def chase(self, name):
        return f'Погоня за {name}'


auto_1 = TownCar(45, 'green', 'Ford Focus')
print(auto_1.go(), auto_1.show_speed())

auto_2 = SportCar(110, 'red', 'Porsche')
print(auto_2.go(), auto_2.turn('на запад'), auto_2.show_speed())

auto_3 = PoliceCar(40, 'white', 'Ford', True)
print(auto_3.expection(), auto_3.chase(auto_2.name))
print(auto_2.stop(), auto_3.expection())