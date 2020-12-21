# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится
# специальный символ, выполнение программы завершается. Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_func():
    all_sum = 0
    while True:
        user_input = input(' Введите числа через пробел.\n Для выхода введите букву:\n').split()
        for i in range(len(user_input)):
            try:
                c = int(user_input[i])
                all_sum = all_sum + c
            except:
                return f'Общая сумма ввода {all_sum}'
        print(f'{all_sum}')


print(sum_func())
