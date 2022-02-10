m = int(input()) #размер матрицы
ans = [[0] * m for i in range(m)] #создать матрицу по размеру
if m % 2 == 0: #если четное определенный рисунок
    for i in range(m):
        for j in range(m):
            if i < j:
                ans[i][j] = "."
            else:
                ans[i][j] = "#"
else: #если нечетный в обратную сторону рисунок
    for i in range(m):
        for j in range(m):
            if i+j == j+i and i+j >= m-1:
                ans[i][j] = "#"
            else:
                ans[i][j] = "."
for r in ans:
    print(''.join([str(e) for e in r])) #вывести рисунок (e -> element, r -> row)