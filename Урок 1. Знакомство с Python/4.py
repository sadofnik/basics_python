# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
# a = 12358334222321
# print(a%10)

# print(a//10)
a = int(input('Введите целое положительное число: 5'))
b = 0
while a > 0:
    i = a % 10
    if i == 9:
        b = i
        break
    elif i > b:
        b = i
    a = a // 10
print(f'Самая большая цифра в вашем числе - {b}')
