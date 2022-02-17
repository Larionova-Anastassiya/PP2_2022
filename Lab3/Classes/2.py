class Shape(object): #класс для подкласса
    def __init__(self):
        pass
    def area(self):
        return 0 #по умолчанию площадь фигуры равна 0

class Square(Shape): #подкласс для вычисления площади
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length #принимает длину и определяет ее как нашу вводимую
    def area(self):
        return self.length * self.length #находит площадь квадрата

print("Input length:")
n = int(input()) #вводим длину стороны квадрата
ans= Square(n) #в подклассе инициализация и принимает значения
print("Area:")
print (ans.area()) #использует функцию для нахождения