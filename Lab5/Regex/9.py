#to insert spaces between words starting with capital letters.
import re


def match(n): #функция выполняющая условия
    return re.sub(r"(\w)([A-Z])", r"\1 \2", n)
    #находя заглавные буквы он поставит пробел и продолжит дальше

m = input()
print(match(m)) #выведет функцию с нашим значением

"""
Example:

AnnaMotherIsThebest -> Anna Mother Is Thebest
"""