# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def calc(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return f'На ноль делить нельзя'

print(f"{'*'*10} Функция деления {'*'*10}")

firstNumber = int(input("Введите делимое: "))
secondNumber = int(input("Введите делитель: "))

print(f'{calc(firstNumber,secondNumber):.2f}')
