def to_ounces(grams):
    return 28.3495231 * grams


grams = int(input())
ans = to_ounces(grams)
print(ans)
