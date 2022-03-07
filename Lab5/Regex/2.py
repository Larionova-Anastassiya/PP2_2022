# that matches a string that has an 'a' followed by two to three 'b'.
import re


def match(n): #функция выполняющая условия
    ans = 'ab{2,3}' #'a' followed by two to three 'b'
    if re.search(ans, n): #применит к нашему тексту функцию регекса
        return 'Yes!'
    else:
        return ('No!')


m = input()
print(match(m)) #выведет функцию с нашим значением

"""
Example:

ab -> No!
aabbbbbc -> Yes!
"""
