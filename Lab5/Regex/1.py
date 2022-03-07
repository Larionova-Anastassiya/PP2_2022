# that matches a string that has an 'a' followed by zero or more 'b''s.
import re


def match(n): #функция выполняющая условия
    ans = '^a(b*)$' #'a' followed by zero or more 'b''s
    if re.search(ans, n): #применит к нашему тексту функцию регекса
        return 'Yes!'
    else:
        return ('No!')


m = input()
print(match(m)) #выведет функцию с нашим значением

"""
Example:

ac -> No!
abc -> No!
a -> Yes!
ab -> Yes!
abb -> Yes!
"""
