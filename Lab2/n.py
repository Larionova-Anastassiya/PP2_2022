ar = [] #сложить числа до середины по парам
while True:
    a = int(input())
    ar.append(a)
    if a == 0:
        break
ar.pop(len(ar) - 1)
ans = []
while len(ar) != 0:
    ans.append(ar[0] + ar[len(ar) - 1])
    ar.pop(0)
    ar.pop(len(ar) - 1)

print(*ans)
#но не выводит если нечетные