n = int(input()) #конвертируемое число
z = str(input()) #что делать с числом
if z == 'k':
    c = int(input())  # сколько цифр после запятой
    ans = float(n / 1024)
    #f'{ans:.{c}f}' первый вид конвертирования после запятой
    #round(n, c) #второй вид конвертирования после запятой
    print(f"{ans:.{c}f}")  #byte to kilobyte
    #ans = round(ans, c)
elif z == 'b':
    ans = n * 1024 #kilobyte to byte
    print(ans)