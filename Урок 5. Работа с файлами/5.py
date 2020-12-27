# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


def file_write():
    q = input("Введите числа через пробел:\n")
    with open('task_5.txt', 'w', encoding='UTF-8') as file:
        file.write(q)
    with open('task_5.txt', 'r', encoding='UTF-8') as file:
        lines = file.read().split()
        try:
            summ = 0
            for i in range(len(lines)):
                summ += int(lines[i])
            print(summ)
        except ValueError:
            print(f'Вы ввели недопустимые символы.')


file_write()
