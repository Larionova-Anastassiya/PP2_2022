t = input()
l = input()
K = t.find(l)
N = t.rfind(l)
if K!=N:
    print(K, N)
else:
    print(K)
