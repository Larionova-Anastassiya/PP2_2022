import math #библиотека для квадрата
n, m = list(map(int, input().split())) #вводим первую точку по которой ориентир
r = int(input()) # вводим размер сколько будет точек
k = {}
for i in range(r):
    a, b = list(map(int, input().split())) # вводим точки и разделит через пробел
    ans = math.sqrt((a - n) ** 2 + (b - m) ** 2) #используем формулу по нахождению расстояния
    if (ans not in k):
        k[ans] = str(a) + " " + str(b) #добавляем если нет
    else:
        k[ans] = k[ans] + "\n" + str(a) + " " + str(b) #добавляем если уже есть с новой строки
j = list(k.keys())
j.sort() #сортируем лист ключей
for i in j:
    print(k[i]) #выводим элементы в отсортированном листе
