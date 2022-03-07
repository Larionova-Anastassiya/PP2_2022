#чтобы перечислить только каталоги, файлы и все каталоги, файлы по указанному пути.
import os
path = 'C:\\Users\\annalar\Documents\\Unik\Piton\PP2_2022\Lab6\\' #путь по которому проверять
i, x, y = 0, 0, 0
print("\nAll directories and files :") #выведет все файлы и папки
for name in os.listdir(path): #элементы в пути (папке)
    i += 1
    print(i, name) #выведем элементы (наши папки, файлы)

print("\nOnly directories:") #выведет только папки
for name in os.listdir(path): #элементы в пути (папке)
    if os.path.isdir(os.path.join(path, name)): #если есть в папке то вывести
        x += 1
        print(x, name) #выведем элементы (наши папки)

print("\nOnly files:") #выведет только файлы
for name in os.listdir(path): #элементы в пути (папке)
    if not os.path.isdir(os.path.join(path, name)): #если not в папке то вывести не папки
        y += 1
        print(y, name) #выведем элементы (наши файлы)
