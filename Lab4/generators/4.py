def squares(a, b):
    while a <= b: #пока не превысит наш лимит б
        yield a * a #запоминает значение квадрата
        a += 1 #будет увеличивать каждый раз на один пока верно решение

a = int(input())
b = int(input())
for i in squares(a, b): # на каком промежутке выполнить. от а до б. например 1, 10
    print(i)