#to find the sequences of one upper case letter followed by lower case letters.
import re


def match(n): #функция выполняющая условия
    ans = '[A-Z]+[a-z]+$' #one upper case letter followed by lower case letters.
    if re.search(ans, n): #применит к нашему тексту функцию регекса
        return 'Yes!'
    else:
        return ('No!')


m = input()
print(match(m)) #выведет функцию с нашим значением

"""
Example:

PYTHON -> No!
python -> No!
aA -> No!
Python -> Yes!
"""