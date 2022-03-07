#для удаления файла по указанному пути. Перед удалением проверьте наличие доступа и наличие заданного пути.
import os

n = 'C:\\Users\\annalar\Documents\\Unik\Piton\PP2_2022\Lab6\\directories\\' #путь по которому проверка

print("\nTest exists or not:")
print(os.path.exists(n)) #проверит есть ли такой путь и возможен ли он

if not os.path.exists("Letters"): #если нет такой папки
   os.mkdir("Letters") #то он создаст папку

# потом он удалит файл сразу или сделать сначала первую функцию закомментив вторую и потом использовать вторую

if os.path.exists("Letters"): #если есть путь такой папки
   os.rmdir("Letters") #то он удалит папку
