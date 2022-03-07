#to convert a given string to snake case.
import re


def match(n): #функция выполняющая условия
    return '_'.join(re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', n.replace('-', ' '))).split()).lower()
    #re.sub() для замены любых символов пробелами, str.lower() для их нижнего регистра, join (), чтобы объединить все слова

m = input()
print(match(m)) #выведет функцию с нашим значением

"""
Example:

AnnaMotherIsThebest -> anna_mother_is_thebest
"""