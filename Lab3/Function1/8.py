def spy_game(nums):
    for i in range(len(nums)):
        if nums[i:i+3] == [0,0,7]: #содержит последовательных 0 0 7 ([i:i+3] в каких местах проверять (везде) чтобы было [0,0,7])
            return True
    return False
list = list(map(int, input().split(","))) #вводим лист цифр и делим через пробел
ans = spy_game(list) #присваиваем для работы функции
if ans == True:
    print("True")
else:
    print("False")