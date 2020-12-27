# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в
# новый текстовый файл.

def search_dict(word: str):
    dictionary = {
        "one": "Один - 1",
        "two": "Два - 2",
        "three": "Три - 3",
        "four": "Четыри - 4"
    }
    return dictionary.get(word.lower())


def salary_list():
    with open('task_4_eng.txt', 'r', encoding='UTF-8') as file_r:
        context = file_r.readlines()
        for i in range(len(context)):
            word = context[i].split()
            with open('task_4_ru.txt', 'a', encoding='UTF-8') as file_a:
                file_a.write(f'{search_dict(word[0])}\n')


salary_list()
