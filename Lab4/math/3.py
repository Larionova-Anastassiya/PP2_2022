import math
print("Input number of sides:")
n = int(input())
print("Input the length of a side:")
s = int(input())

ans = (1/2) * (s/2) * (s * n) #this formula
print("The area of the polygon is:")
ans = math.ceil(ans) #округляем
print(ans)