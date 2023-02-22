''' Задание 6 Реализовать два небольших скрипта:'''
#итератор, генерирующий целые числа, начиная с указанного;
def function():
    a = int(input('Введите стартовое число: '))
    from itertools import islice
    from itertools import count
    for i in islice(count(a), 20):
        print(i)
function()

#итератор, повторяющий элементы некоторого списка, определённого заранее.
def function_2():
    list = [1, 2, "number", 3]
    from itertools import islice
    from itertools import cycle
    for el in islice(cycle(list), 100):
        print(el)
function_2()
