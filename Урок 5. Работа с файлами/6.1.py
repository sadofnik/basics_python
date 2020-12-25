# Получилось также, но немного изменил прохождение цикла из-за наличия в часах доп.символов

with open('task_6.1.txt', 'r', encoding='UTF-8') as file_r:
    context = file_r.readlines()
    subj = {}
    for i in range(len(context)):
        hours = 0
        word = context[i].split()
        for les in word:
            print(les)
            if les.find('(') >= 0:
                temp_les = int(les[:les.index('(')])
                hours += temp_les
            else:
                continue
        subj[word[0]] = hours

print(subj)
