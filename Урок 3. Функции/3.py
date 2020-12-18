# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


#  Простым условием
def my_func(a, b, c):
    if a > b:
        if b > c:
            print(a + b)
        else:
            print(a + c)
    elif a > c:
        print(a + b)
    else:
        print(b + c)


my_func(6, 5, 7)


#  Через сортировку
def my_func_s(*args):
    a = sorted(args)
    print(a.pop(-1) + a.pop(-1))


my_func_s(6, 5, 7)
