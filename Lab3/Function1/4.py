print("Input list: ")
def filter_prime(my_list):
    prime = list(filter(lambda i: all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)), my_list)) #использовала код из 6 задания классов
    p = sorted(prime)
    # можно не сортить и тогда сразу вывести прайм
    print(*p)
my_list = list(map(int, input().split()))
print("Prime this list:")
filter_prime(my_list)
#result = [i for i in ans if i != [None]]
