class Shape(object):  # класс для подкласса
    def __init__(self):
        pass

    def area(self):
        return 0  # по умолчанию площадь фигуры равна 0


class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)
        self.length = length  # принимает длину и определяет ее как нашу вводимую
        self.width = width  # принимает ширину и определяет ее как нашу вводимую

    def area(self):
        return self.length * self.width


print("Input length:")
n = int(input())  # вводим длину стороны
print("Input width:")
m = int(input())  # вводим ширину стороны

ans = Rectangle(n, m)  # в подклассе инициализация и принимает значения
print("Area:")
print(ans.area())  # использует функцию для нахождения
