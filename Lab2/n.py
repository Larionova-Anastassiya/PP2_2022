ar = [] #сложить числа до середины по парам
while True:
    a = int(input())
    ar.append(a)
    if a == 0:
        break
ar.pop(len(ar) - 1)
pl = len(ar) // 2
for i in range(len(ar) // 2):
    if (len(ar) // 2) + (len(ar) // 2) == len(ar): #проверить если четное
        print(ar[i] + ar[len(ar) - 1 - i], end=' ')
    elif (len(ar) // 2) + (len(ar) // 2) != len(ar): #проверить если нечетное
        res = [a + b for a, b in zip(ar[:pl], reversed(ar[pl:]))]
        res.append(ar[pl])
        print(*res)
        break
