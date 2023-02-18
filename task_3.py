''' Задание 3 Реализовать функцию my_func(),
которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.'''

def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c
print(my_func(a=int(input("введите первое чило: ")), b=int(input("введите второе число: ")), c=int(input("введите третье число: "))))
