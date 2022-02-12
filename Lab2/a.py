def jump(n): # function
    maxi = 0 #maximum 0
    for i, j in enumerate(n):
        if i > maxi:
            return False
        maxi = max(i + j, maxi) #максимально достижимый индекс
    return True
n = list(map(int, input().split())) # input
ans = jump(n)
if ans == False: # output
    print('0')
else:
    print('1')