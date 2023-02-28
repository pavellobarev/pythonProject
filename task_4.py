''' Задание 4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.'''

word={"one": "один", "two": "два", "three": "три"}
with open("text_2.txt") as object:
    for line in object:
        for key in word.keys():
            line=line.replace(key, word[key])
        print(line)
        with open("text_3.txt", "a") as object_rus:
            object_rus.write(f"\n {line}")


