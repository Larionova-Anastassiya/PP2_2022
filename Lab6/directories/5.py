# для записи списка в файл

# color = ['Красный', 'Оранжевый', 'Желтый', 'Зеленый', 'Голубой', 'Синий', 'Фиолетовый'] #готовый лист вставит

list = list(input().split())  # самим ввести лист и разделит через пробел
with open('mynewfile.txt',"w") as file:  # откроет новый файл или создаст и переименует его в file ("w" перезапишет данные)
    for word in list:  # for c in color: #пройдет по каждому элементу (word) в листе
        file.write("%s\n" % word)  # напишет слова (%word) в нашем файле с новой строки каждое ("%s\n")
"""
Данные, такие как строковые форматы (%s), и имеющие кортеж, состоящий из имени переменной и переменной.
\n-это символ новой строки, который используется, когда мы хотим отобразить новую строку.
"""

content = open('mynewfile.txt')  # откроет уже существующий файл
print(content.read())  # прочтет и выведет нам данные файла
