n, m = input().replace('+', ' ').split() #ввод в виде ONETWOTHR+FOUFIVSIX и разделить его
t = { "ZER" : 0, "ONE" : 1 , "TWO" : 2, "THR" : 3, "FOU" : 4, "FIV" : 5, "SIX" : 6, "SEV" : 7, "EIG" : 8, "NIN" : 9} #
def fun(s): # функция которая буквы сделает цифрами
    ans = 0
    for i in range(0, len(s), 3):
        b = s[i:i+3]
        ans = ans*10 + t[b]
    return ans
summ = str(fun(n) + fun(m)) #сложит и получим результат по в цифрах
summ = summ.replace('1', 'ONE').replace('2', 'TWO').replace('3', 'THR').replace('4', 'FOU').replace('5', 'FIV').replace('6', 'SIX').replace('7', 'SEV').replace('8', 'EIG').replace('9', 'NIN').replace('0', 'ZER')
print(summ) #результат так же буквами сделает ONEZERZERFIVFIV
