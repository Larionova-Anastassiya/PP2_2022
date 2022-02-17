def unique(num):
    unique = []
    for elem in num:
        if elem not in unique:
            unique.append(elem)
    return unique
list = list(map(int, input().split(",")))
ans = unique(list)
print(*ans)
"""
input: 1,2,3,4,5,6,1,2,3,4,9
output: 1 2 3 4 5 6 9
"""