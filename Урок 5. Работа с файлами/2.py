# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

with open('task_2.txt', 'r', encoding='UTF-8') as file:
    content = file.readlines()
    count = 0
    count_word = 0
    for i in range(len(content)):
        count_word += len(content[i])
        print(f'Номер строки: {i + 1} - количество слов в строке: {len(content[i])}')
    print(f'Итого строк: {i + 1} \nИтого слов: {count_word}')
