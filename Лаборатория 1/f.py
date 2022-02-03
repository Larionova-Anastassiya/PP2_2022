n = int(input()) #сколько строк будет
for i in range(n): #вводить самому
    k = int(input())
    if k <= 10:
        print("Go to work!")
    elif k > 10 and k <= 25:
        print("You are weak")
    elif k > 25 and k <= 45:
        print("Okay, fine")
    elif k > 45:
        print("Burn! Burn! Burn Young!")