# Задание 2
import time
n = int(input("Введите время в секундах"))
time_format = time.strftime("%H:%M:%S", time.gmtime(n))
print("Time in preferred format :-", time_format)

