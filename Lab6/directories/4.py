# для подсчета количества строк в текстовом файле
print("Number of lines: ")
with open('example.txt') as f: #откроет наш текстовый файл и переименует его в f
    for i, l in enumerate(f): #enumerate() применяется в случаях, когда необходим счётчик количества
        pass #пропуск
print(i + 1) #выведет количество строк написанных текстом

"""
2 вариант

def file_lengthy(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
print("Number of lines: ", file_lengthy("example.txt"))

3 вариант

print("Number of lines: ")
#откроет наш текстовый файл и переименует его в f
for i, l in enumerate(open('example.txt')): #enumerate() применяется в случаях, когда необходим счётчик количества
    pass #пропуск
print(i + 1) #выведет количество строк написанных текстом

"""