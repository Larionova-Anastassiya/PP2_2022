#to find sequences of lowercase letters joined with a underscore.
import re


def match(n): #функция выполняющая условия
    ans = '^[a-z]+_[a-z]+$' #lowercase letters joined with a underscore (aab_abbbc)
    if re.search(ans, n): #применит к нашему тексту функцию регекса
        return 'Yes!'
    else:
        return ('No!')


m = input()
print(match(m)) #выведет функцию с нашим значением

"""
Example:

aab_Abbbc -> No!
Aaab_abbbc -> No!
aab_cbbbc -> Yes!
"""