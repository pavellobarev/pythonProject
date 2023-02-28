''' Задание 1. Создать программный файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.'''

object= open("text.txt", "w")
list = []
while True:
    line = input("Введите данные. Если хотите завершить, введите Enter: ")
    if line != '':
        list.append(line + "\n")
    else:
        break
object.writelines(list)
with open("text.txt","r") as object:
    for line in object:
        print(line)

