def sort(w):  # Разделить строку n, пока не будет найдено место.
    words = w.split()
    words.sort()  # sort () будет сортировать строки.
    for i in words:
        print(i)

import re

s = input()
reg = re.compile('[^a-zA-Z ]')
w = reg.sub('', s)  # строка без специальных знаков будет
l = set(w.split())
print(len(l))
sort(w)  # Вызов функции
"""
1 variant
input: Hello, Boris! How are you?
output:
5
Boris
Hello
How
are
you
"""