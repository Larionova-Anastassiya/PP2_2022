# возвращает все числа от (n) до 0.

def all(n):
    while n >= 0: #пока не равно 0 будет выполнять
        yield n #запоминает наши значения и выводит
        n -= 1 #уменьшает на 1 наше значение


start = int(input()) #вводим с какого начать
for i in all(start): #пройдет по элементам в функции
    print(i)