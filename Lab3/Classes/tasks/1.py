#Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
class func(object): #возьмет обьект (строку) для работы
    def getString(self):
        self.i = input("String: ") #вводить самим строку
    def printString(self):
        print(self.i.upper()) #выведет строку преобразовав в большие буквы
ans = func() #присваивание класса
ans.getString() #вызов функции из класса ввода
ans.printString() #вызов функции из класса вывода