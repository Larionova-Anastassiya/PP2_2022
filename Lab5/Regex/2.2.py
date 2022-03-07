import re
m = input()
ans = 'ab{2,3}' #'a' followed by two to three 'b'
if re.search(ans, m): #применит к нашему тексту функцию регекса
    print('Yes!')
else:
    print('No!')
"""
    Example:

    ab -> No!
    aabbbbbc -> Yes!
"""