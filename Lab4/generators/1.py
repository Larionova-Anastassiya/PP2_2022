#генерирует квадраты чисел до некоторого числа n
import math
class MyNumbers:
  def __init__(self, limit):
      self.limit = limit #примет ограничение значение

  def __iter__(self): #начальные значения возьмет
    self.x = 1
    self.cnt = 1
    return self

  def __next__(self):
    if self.cnt > self.limit:
      raise StopIteration # остановит если превысило количество итераций
    x = math.pow(self.x, 2) #введет квадраты значения
    self.x += 1 #увеличит на 1 х и в итоге следующее число в квадрате
    self.cnt += 1 #считает итерации для ограничения
    return x

print("Input limit:")
n = int(input())
power = MyNumbers(n) #выполняет функцию для ограничения
for item in power: #выведет элементы итерации в классе
  item = math.floor(item) #округлт значения, чтобы не было плавающей точки
  print(item)
