'''Задание 3. Реализовать программу работы с органическими клетками'''

class cell:
    def __init__(self, quantity):
        self.quantity=int(quantity)
    def __str__(self):
        return f'({self.quantity}'
    def __add__(self, other):
        return f'Сумма клеток={str(cell(self.quantity+other.quantity))}'
    def __sub__(self, other):
        if(self.quantity-other.quantity)>0:
            return f'Разность клеток={cell(int(self.quantity-other.quantity))}'
        return f'Разность отрицательна'
    def __mul__(self, other):
        return cell(int(self.quantity * other.quantity))
    def __truediv__(self, other):
        return cell(round(self.quantity // other.quantity))
    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
            row += f'{"*" * (self.quantity % cells_in_row)}'
        return row

cells1 = cell(5)
cells2 = cell(10)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(5))
print(cells1.make_order(10))
print(cells1 / cells2)






