n, f = map(int, input().split())  # ввести самим два числа в одну строку
k = 0
Prime = True
for i in range(2, n // 2 + 1):  # проверка на простое число
    if (n % i == 0):
        k = k + 1
        Prime = False
        break
    elif (k <= 0):
        Prime = True
    else:
        Prime = False
if (n <= 500 and Prime and f % 2 == 0):  # выполняемые условия в задаче
    print("Good job!")
else:
    print("Try next time!")
