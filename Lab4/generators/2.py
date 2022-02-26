#для печати четных чисел от 0 до n в форме, разделенной запятыми, где n ввод с консоли.
def even(x):
    for x in range(0,x+1):
        if x%2==0:
            yield x #запомнит и выведет х

limit=int(input()) #лимит до какого числа
ans = [] #пустое куда сохранять
for i in even(limit):
    ans.append(str(i)) #добавит
print(",".join(ans)) #выведет через запятую

"""
example:
11
0,2,4,6,8,10
"""