n = input()
l = set(n.split()) #ввести предложение или значения
ans = [] # пустой лист куда вносить значения будем
t = ""
for i in l:
    for j in i:
        if j.isalpha():
            t += j
    ans.append(t) #добавит в лист только слова, пропустит обозначения
    t = ""
ans.sort() #отсортирует лист
print(len(ans))
for i in ans: #пробежится по всем элементам и выведет их
    print(i)

    """
    2 variant
    input: Hello, Boris! How are you?
    output:
    5
    Boris
    Hello
    How
    are
    you
    """
