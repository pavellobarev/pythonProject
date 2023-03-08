'''Задание 1. 1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.'''

class matrix:
    def __init__(self, *args):
        self.new_lst=list(args)
    def __str__(self):
        result= '\n'.join(map(str, self.new_lst))
        result= result.replace(',','').replace('[', '').replace(']', '')
        return result
    def __add__(self, other):
        new_sum=[]
        line_sum=[]
        for x in range(len(self.new_lst)):
            for y in range(len(self.new_lst[x])):
                line_sum.append(self.new_lst[x][y]+other.new_lst[x][y])
            new_sum.append(line_sum)
            line_sum=[]
        return matrix('\n'.join(map(str, new_sum)))

m_obj_1=matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(m_obj_1)
print()

m_obj_2=matrix([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(m_obj_2)
print()

print(f'Сумма матриц:\n(m_obj_1=m_obj_2)')
print()
print(m_obj_1)
print()
print(m_obj_2)
