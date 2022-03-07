#чтобы проверить, существует ли данный путь или нет. Если путь существует, найдите имя файла и часть каталога данного пути.
import os
path = r'C:\\Users\\annalar\Documents\\Unik\Piton\PP2_2022\Lab6\\directories\\1.py'

print("\nTest exists or not:")
print(os.path.exists(path)) #проверит есть ли такой путь и возможен ли он

print("\nFile name:")
print(os.path.basename(path)) #выведет название файла (указанный в пути)

print("\nDirectory name:")
print(os.path.dirname(path)) #выведет папку в которой находится данный файл, выведет путь до последней папки