d = dict()
for i in range(int(input())): #введем данные до определенного размера
    s = input().split() # имя ученика и сумма по отдельности
    if s[0] not in d.keys(): # проверить есть ли такое уже имя
        d[s[0]] = 0
    d[s[0]] += int(s[1]) #сложить сумму у одинаковых имен
t = max(d.values()) #максимальная сумма из всех
d = sorted(d.items(), key = lambda x:x[0]) #
for i in d:
    if t - i[1] > 0:
        ans = t - i[1] # от максимума найдем остаток
        print(i[0], 'has to receive',ans, 'tenge') # выведем имя и остаток от максимумв
    if t - i[1] == 0: # если это сам максимум
        print(i[0], 'is lucky!')