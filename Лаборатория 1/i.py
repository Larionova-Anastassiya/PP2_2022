l = int(input()) #сколько строк будет
# k = input()
s = [] #пустой лист для данных
m = "@gmail.com" #что искать будет
""" 
for i in range(n): #вводить самому почту
    s.append(input())
l = s.find(m)
if l != -1:
    print(i)
    #neverno
"""
for i in range(0, l): #вводить самому почту
    k = input()
    if m in k:
        #d = k.strip(m)
        s.append(k.strip(m))
print(*s, sep = "\n") #вывод ответа с новой строки