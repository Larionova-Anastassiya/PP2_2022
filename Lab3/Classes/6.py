print("Input list: ")
my_list = list(map(int, input().split()))

prime = list(filter(lambda i: all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)), my_list))
"""
filter() отбирает/фильтрует элементы переданного объекта ри помощи функции.
Функция используется lambda для всех значений листа (i) (где j числа для проверки деления), для нашего листа разделенных чисел
int(i ** 0.5) + 1 используется вместо корня - это где остановится. 2 это начало для проверки
"""
print("Prime this list:")
print(*prime)
