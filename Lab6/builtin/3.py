# проверяет, является ли переданная строка палиндромом или нет.
def palindrome(data):
    data = data.replace(' ', '').lower()  # он заменит все пробелы на пустоту и уменьшит все буквы (для проверки)
    return 'Palindrome' if data == data[::-1] else 'Not palindrome'  # если строка одинакова со строкой наоборот (data[::-1]) то палиндром


n = input()
print(palindrome(n)) #вызовет функцию проверки

"""
Example:

Input: 123anna321
Output: Palindrome

Input: Afa Ag gA afA
Output: Palindrome

"""
