''' Задание 5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw.
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.'''


class Stationary:
    def __init__(self, title):
        self.title = title
    @staticmethod
    def draw():
        print("Запуск отрисовки")

class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f"Отрисовка {self.title} Класс Pen")

class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f" Отрисовка {self.title} Класс Pencil")

class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f" Отрисовка {self.title} Класс Handle")

p_obj=Pen("ручкой - ")
p_obj.draw()
p_obj=Pencil("карандашом - ")
p_obj.draw()
p_obj=Handle("маркером - ")
p_obj.draw()


