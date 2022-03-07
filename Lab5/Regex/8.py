#to split a string at uppercase letters.
import re


def match(n): #функция выполняющая условия
    return re.findall('[A-Z][^A-Z]*', n) #to split a string at uppercase letters.
    #findall - возвращает все неперекрывающиеся совпадения шаблона pattern в строке string в виде списка строк

m = input()
print(match(m)) #выведет функцию с нашим значением

"""
Example:

AnnaMotherIsThebest -> ['Anna', 'Mother', 'Is', 'Thebest']
"""