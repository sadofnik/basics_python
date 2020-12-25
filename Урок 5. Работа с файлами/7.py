# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные
# о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее
# в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]


def firm():
    with open('task_7.txt', 'r', encoding='UTF-8') as file_r:
        context = file_r.readlines()
        firm_dict = {}
        average_dict = {"average_profit": None}
        average_salary = 0
        count_firm = 0

        for i in range(len(context)):
            word = context[i].split()
            diff = int(word[2]) - int(word[3])
            if diff > 0:
                average_salary += diff
                count_firm += 1
            firm_dict[word[0]] = diff
        average_dict["average_profit"] = average_salary / count_firm

    with open("task_7.json", "w", encoding='UTF-8') as file:
        print([firm_dict, average_dict], file=file)
    return f'Создан JSON-файл с содержимым:\n{[firm_dict, average_dict]}'


print(firm())
