# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


request = input("Введите число: ")
sum_1 = request
sum_2 = request + request
sum_3 = request + request + request
print(int(sum_1) + int(sum_2) + int(sum_3))
