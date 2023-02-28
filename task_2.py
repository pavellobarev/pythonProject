''' Задание 2. Создать текстовый файл (не программно),
сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.'''

lines=0
word=1
with open("text_1.txt", "r") as object:
    for line in object:
        print(line.replace("\n", ""))
        for n in line:
            if n == " ":
                word= word+1
            lines=lines+1
            print(f"Слов в строке {lines} = {word} \n")
            words=1
        print(f"Строк: {lines}")

