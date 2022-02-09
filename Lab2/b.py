n = input()
mas1 = list(map(int, input().split()))
mas2 = sorted(mas1)
ans = mas2[-1] * mas2[-2]
print(ans)
#Максимальное произведение двух элементов.
