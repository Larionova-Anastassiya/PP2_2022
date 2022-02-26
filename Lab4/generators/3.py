# делящиеся на 3 и 4, между заданным диапазоном 0 и n

def devision(x):
    for x in range(0, x + 1): #начало с 0
        if x % 3 == 0 and x % 4 == 0: #условия деления на 3 и на 4
            yield x #запомнит и продолжит с запомнившимся элементом

limit = int(input())
resp = [str(i) for i in devision(limit)] #цикл пройдет по элементам в функции
print(",".join(resp)) #выведет через запятую
