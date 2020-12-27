# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


def file_write():
    while True:
        q = input("Для окончания работы программы введите 'Enter':\n")
        if not q:
            print('Завершение программы. Вы ввели:\n')
            break
        else:
            with open('my_file.txt', 'a+', encoding='UTF-8') as file:
                file.write(f'{q}\n')


file_write()

file = open('my_file.txt', 'r', encoding='UTF-8')
lines = file.read()
print(lines)
file.close()
