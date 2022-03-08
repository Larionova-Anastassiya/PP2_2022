#которая принимает строку и вычисляет количество прописных и строчных букв
s = input() #вводим самим строку
U = sum(map(str.isupper, s)) #количество заглавных (больших) букв
l = sum(map(str.islower, s)) #количество строчных (маленьких) букв
print(f'Заглавных букв: {U}'
      f'\nCтрочных: {l}')
"""
sum --> вычислит общее количество данных

map(str.isupper, s) --> в строке найдет именно заглавные буквы, так же и строчные

str.isupper --> str.isupper() возвращает True, если все символы в строке str прописные (имеют верхний регистр), 
при этом строка не должна быть пустой, то есть должна иметь хотя бы один символ в верхнем регистре

str.islower --> str.islower() возвращает True, если все символы в строке имеют нижний регистр и есть хотя бы один символ
"""