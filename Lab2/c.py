n = int(input()) #размер матрицы
arr = [[0] * n for i in range(n)] # создание нулевой матрицы
a = 0 # числа дальнейшие для заполнения
for i in range(n):
    for j in range(n):
        if i == j:
            arr[i][j] = a * a #диагональ это квадраты чисел
            a += 1
i, j, a = 0, 0, 0 # измененные для других линий
while j < n: #первая линия подряд чисел
    arr[i][j] = a
    a += 1
    j += 1
j, a = 0, 0
while i < n: #вторая линия подряд чисел
    arr[i][j] = a
    a += 1
    i += 1
for ans in arr:
    print(' '.join([str(s) for s in ans])) #ответ матрица умножения только с квадратами чисел
"""
input: 5
output: 
0 1 2 3 4
1 1 0 0 0
2 0 4 0 0
3 0 0 9 0
4 0 0 0 16

"""