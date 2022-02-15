n = int(input()) #количество демонов()
di = dict()
demon = 0 #first counter
for i in range(n):
    l = input().split()
    if l[1] not in di.keys(): #если нет в нашем дикшионари такая слабость
        di[l[1]] = 1
    else: di[l[1]] += 1 #сложить слабости
m = int(input()) #количество охотников()
k = dict()
for i in range(m):
    l = input().split() #имя охотника, способность, количество демонов
    if l[1] not in k.keys(): #если нет в нашем дикшионари такая слабость демонов
        k[l[1]] = int(l[2])
    else: k[l[1]] += int(l[2]) #сложить слабости
#подсчет демонов ->
for key, value in sorted(di.items()):
    if key not in k.keys():
        demon += value
for key, value in sorted(di.items()):
    for key1, value1 in sorted(k.items()):
        if key1 == key:
            sum = value - value1 #слабости будут отниматься сколько сможет убить, чтобы знать сколько осталось
            if sum > 0:
                demon += sum
            break
print('Demons left:', demon) #выведет сколько демонов осталось
"""
Целое число в первой строке = n  - количество демонов().
Далее  строки состоят из строк l (l[0] name, l[1] need name слабость) - имя демона и слабость демона.
Целое число в следующей строке = m  - количество охотников().
Далее  строки состоят из строк ,  и целое число  - имя охотника (l[0]), способность (l[1]), количество демонов (l[2]), которых охотник может убить

Печать - Demons left: и количество оставшихся демонов
"""