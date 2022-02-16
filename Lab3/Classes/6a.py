#with class
print("Input list: ")
class prime(object):
    def getList(self):
        self.my_list = list(map(int, input().split())) #вводить самим
    def prime_number(self):
        prime = list(filter(lambda i: all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)), self.my_list))
        p = sorted(prime)
        #можно не сортить и тогда сразу вывести прайм
        print(*p)
ans = prime()
ans.getList() #вызов функции из класса ввода
print("Prime this list:")
ans.prime_number() #вызов функции из класса вывода prime

"""
filter() отбирает/фильтрует элементы переданного объекта ри помощи функции.
Функция используется lambda для всех значений листа (i) (где j числа для проверки деления), для нашего листа разделенных чисел
int(i ** 0.5) + 1 используется вместо корня - это где остановится. 2 это начало для проверки
"""