n = input()
print(int(n, 2)) #автоматический перевод в десятичную любое число, рекурсию не изучали и не поняла данную тему пока что
""" 
variant 2

summ = 0
f = len(n)
for i in range(0, len(n)):
    #num = int(n[i])*(2**(f - i))/2 перевод в десятичную
    summ + int(n[i]) * (2**(f - i))
print(summ)
"""
