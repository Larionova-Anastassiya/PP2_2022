#для проверки доступа к указанному пути. Проверьте наличие, читаемость, записываемость и исполняемость указанного пути
import os
n = 'C:\\Users\\annalar\Documents\\Unik\Piton\PP2_2022\Lab6\\' #путь по которому проверять
#n = input()
# os.access() вернет True, если доступ разрешен, False, если нет.
print('\nExist:', os.access(n, os.F_OK)) #os.F_OK для проверки существования пути
print('\nReadable:', os.access(n, os.R_OK)) # os.R_OK - проверка возможности чтения,
print('\nWritable:', os.access(n, os.W_OK)) #os.W_OK - проверка возможности записи,
print('\nExecutable:', os.access('C:\\Users\\annalar\Documents\\Unik\Piton\Lab6\\', os.X_OK)) #--> False (нет пути такого)
#os.X_OK - проверка выполнения файла или открытия директории
#print('Executable:', os.access(n, os.X_OK))  --> True