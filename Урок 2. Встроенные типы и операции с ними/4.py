# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.

# a = "Пользователь вводит строку из нескольких слов разделённых пробелами."
a = input(f'Введите предложение: ').split()

for i in range(len(a)):
    print(f'{i + 1}. {a[i]:<.10}')


# Через enumerate
for ind, el in enumerate(a, 1):
    print(f'{ind}. {el:<.10}')


#  Новый способ с использованием среза
for i in range(len(a)):
    print(f'{i + 1}. {a[i][:10]}')
