#для генерации 26 текстовых файлов с именами A.txt, B.txt, и так далее вплоть до Z.txt
import os
import string

if not os.path.exists("Letters"): #если нет такой папки
   os.mkdir("Letters") #то он создаст папку

os.chdir('Letters')
#создаст отдельно все наши файлы
for letter in string.ascii_uppercase: #Константное перечисление букв из набора ASCII в верхнем регистре
    with open(letter + ".txt", "w") as f: #создаст файл для всех букв и перезаписывать данные будет
        f.writelines(letter) #f.writelines() записывает последовательность (список) строк в файл
