#которая возвращает True, если все элементы кортежа истинны
def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

text = tuple((input().split()))
"""
Input: [3, 0, 2, []]
Output: False

Input:
Output:
"""
print("If tuple this is my text or empty:")
print(all(text))

print("\nIf tuple = [3, 0, 2, []] : ")
print(all([3, 0, 2, []]))

#Если передаваемая последовательность пуста, то функция all() также возвращает True.
#Функция all() возвращает значение True , если все элементы в итерируемом объекте - истинны, в противном случае она возвращает значение False.