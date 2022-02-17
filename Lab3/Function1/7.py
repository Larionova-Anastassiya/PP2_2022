def has_33(nums):
    for i in range(len(nums)):
        if nums[i:i+2] == [3,3]: #indices contain 2 consecutive 3 (содержит два последовательных 3)
            return True
    return False
list = list(map(int, input().split())) #вводим лист цифр и делим через пробел
ans = has_33(list) #присваиваем для работы функции
if ans == True:
    print("True")
else:
    print("False")

"""
1 3 1 3
False

1 3 3
True
"""