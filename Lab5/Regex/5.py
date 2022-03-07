#that matches a string that has an 'a' followed by anything, ending in 'b'.
import re


def match(n): #функция выполняющая условия
    ans = 'a.*?b$' #that matches a string that has an 'a' followed by anything, ending in 'b'.
    if re.search(ans, n): #применит к нашему тексту функцию регекса
        return 'Yes!'
    else:
        return ('No!')


m = input()
print(match(m)) #выведет функцию с нашим значением

"""
Example:

aabAbbbc -> No!
accddb -> Yes!
"""