n = int(input())  # сколько операций будет
l = []  # input books
k = []  # output books
for i in range(n):
    o = input()  # вводим число и книгу
    if int(o[0]) == 1:  # чтобы добавить
        l.append(o[2:len(o)])
    if int(o[0]) == 2:  # чтобы удалить (взять)
        k.append(l[0])
        l.remove(l[0])
for i in k:
    print(i, end=" ")  # вывести в одну строку ответ
