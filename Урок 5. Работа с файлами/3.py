# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


def salary():
    while True:
        q = input("Введите фамилию и размер з\п \nДля выхода нажмите 'Enter':\n")
        if not q:
            print('Завершение программы. Вы ввели:\n')
            break
        else:
            with open('task_3.txt', 'a', encoding='UTF-8') as file:
                file.write(f'{q}\n')


def salary_list():
    with open('task_3.txt', 'r', encoding='UTF-8') as file:
        context = file.readlines()
        small_salary = []
        mid_salary = 0
        for i in range(len(context)):
            salary = context[i].split()
            mid_salary += int(salary[1])
            if int(salary[1]) < 20000:
                small_salary.append(salary[0])

    return f'Сотрудники с окладом менее 20000: {[i for i in small_salary]}\n' \
           f'Средняя величина дохода сотркдников: {round(mid_salary / (i + 1), 2)}'


salary()
print(salary_list())
