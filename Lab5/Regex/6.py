#to replace all occurrences of space, comma, or dot with a colon.
import re


def match(n): #функция выполняющая условия
    #to replace all occurrences of space, comma, or dot with a colon.
    #применит к нашему тексту функцию регекса re.sub замена на :
    return re.sub("[ ,.]", ":", n)


m = input()
print(match(m)) #выведет функцию с нашим значением

"""
Example:

Anna, Mother: is the best. -> Anna::Mother::is:the:best:
"""