n = int(input()) #если он содержит прописные, строчные буквы и цифры
ans = []
for i in range(n):
    l = str(input())
    s1, s2, s3 = 0, 0, 0
    for j in l:
        if j >= 'A' and j <= 'Z':
            s1 += 1
        if j >= 'a' and j <= 'z':
            s2 += 1
        if j >= '0' and j <= '9':
            s3 += 1
    if s1 >= 1 and s2 >= 1 and s3 >= 1:
        if l not in ans:
            ans.append(l)
print(len(ans))
for i in sorted(ans):
    print(i)