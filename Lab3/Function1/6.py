"""
def reverseWords(s):
  return s[::-1]
s = input()
print(reverseWords(s))
"""
def reverseWords(s):
  return s[::-1]
s = input().split() #слова перевернет местами в предложении, если без сплита то буквы все. Если ввод We are ready
ans = reverseWords(s) #выведет ready are We
print(*ans)
