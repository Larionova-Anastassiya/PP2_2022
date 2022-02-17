def Palindrome(word):
    left = 0
    right = len(word) - 1
    while right >= left: #будет проверять каждого элемента
        if word[left] != word[right]: #если же первый и последний элемент не совпадают
            return False
        left += 1
        right -= 1
    return True

word = input()
print(Palindrome(word))
