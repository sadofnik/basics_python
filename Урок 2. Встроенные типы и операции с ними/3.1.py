# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

season = ["Зима", "Весна", "Лето", "Осень"]
a = int(input("Введите целое число от 1 до 12: "))
if 3 <= a <= 5:
    print(season[1])
elif 6 <= a <= 8:
    print(season[2])
elif 9 <= a <= 11:
    print(season[3])
elif a == 12 or a == 1 or a == 2:
    print(season[0])
else:
    print("Такого месяца нет.")