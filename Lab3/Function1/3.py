def solve(heads, legs):
    ans = 'No solutions!'
    for x in range(heads + 1):
        y = heads - x
        if 2 * x + 4 * y == legs: #формула решения логической задачи
            return x, y
    return ans, ans

heads = 35 #int(input())
legs = 94 #int(input())
ans = solve(heads, legs)
print (*ans)