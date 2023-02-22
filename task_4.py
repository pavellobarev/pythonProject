'''Задание 4 Представлен список чисел.
Определите элементы списка, не имеющие повторений.
Сформируйте итоговый массив чисел, соответствующих требованию.
Элементы выведите в порядке их следования в исходном списке.
Для выполнения задания обязательно используйте генератор.'''

def function(lst:list) -> None:
    result = {}
    for key, num in enumerate(lst):
        if result.get(num) is None:
            result[num] = 1
        else:
            result[num] += 1
    return result
list_src = [1, 2, 3, 23, 54, 23, 7, 65, 78, 78, 97, 2]
counter = function(list_src)
list_res = [x for x, n in counter.items() if n == 1]
print(list_res)
