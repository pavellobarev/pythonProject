''' Задание 5.  Создать (программно) текстовый файл, записать в него программно набор чисел,
разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.'''

object = open("text_4.txt", "w")
print("Введите набор чисел, разделенных пробелами: ")
while True:
    line = input()
    object.write(line + '\n')
    if line == "":
        break
object = open('text_4.txt', 'r')
list = object.read().split()
total = 0
for elem in list:
    total += float(elem)
print("Сумма чисел в файле: ", total)


