def to_ounces(grams):
    return 28.3495231 * grams

def centigrade(Fahrenheit):
    return (5.0 / 9.0) * (Fahrenheit - 32)

def reverseWords(s):
  return s[::-1]

def spy_game(nums):
    for i in range(len(nums)):
        if nums[i:i+3] == [0,0,7]: #содержит последовательных 0 0 7 ([i:i+3] в каких местах проверять (везде) чтобы было [0,0,7])
            return True
    return False

def has_33(nums):
    for i in range(len(nums)):
        if nums[i:i+2] == [3,3]: #indices contain 2 consecutive 3 (содержит два последовательных 3)
            return True
    return False

from math import pi
def volume(radius):
    return 4 / 3 * pi * radius ** 3 #formula

def histogram(my_list):
  for n in my_list:
    print (n * "*")

def Palindrome(word):
    left = 0
    right = len(word) - 1
    while right >= left: #будет проверять каждого элемента
        if word[left] != word[right]: #если же первый и последний элемент не совпадают
            return False
        left += 1
        right -= 1
    return True

print("What function do you want to use?")
print("№ grams per ounce \n"
      "№ Fahrenheit to Celsius \n"
      "№ reverse words in string \n"
      "№ check if 007 contains \n"
      "№ check if 33 contains \n"
      "№ find volume sphere \n"
      "№ make a histogram \n"
      "№ check if the palindrome is a string \n")

task = input()
if task == "grams per ounce":
    print("Enter grams:")
    grams = int(input())
    ans = to_ounces(grams)
    print("Grams per ounces:")
    print(ans)

elif task == "Fahrenheit to Celsius":
    print("Enter Fahrenheit temperature:")
    Fahrenheit = int(input())
    Celsia = centigrade(Fahrenheit)
    print(f"{Fahrenheit} fahrenheit is {Celsia} centigrade")

elif task == "reverse words in string":
    print("Enter string:")
    s = input().split()  # слова перевернет местами в предложении, если без сплита то буквы все. Если ввод We are ready
    ans = reverseWords(s)  # выведет ready are We
    print("Reverse string:")
    print(*ans)

elif task == "check if 007 contains":
    print("Enter list, example (1,2,3,4,...):")
    list = list(map(int, input().split(",")))  # вводим лист цифр и делим через пробел
    ans = spy_game(list)  # присваиваем для работы функции
    if ans == True:
        print("True")
    else:
        print("False")

elif task == "check if 33 contains":
    print("Enter list, example (1 2 3 4 ...):")
    list = list(map(int, input().split()))  # вводим лист цифр и делим через пробел or .split(",")
    ans = has_33(list)  # присваиваем для работы функции
    if ans == True:
        print("True")
    else:
        print("False")

elif task == "find volume sphere":
    print("Enter radius:")
    radius = int(input())
    print("Volume this sphere:")
    print(volume(radius))

elif task == "make a histogram":
    print("Enter list, example (1,2,3,4,...):")
    my_list = list(map(int, input().split(",")))
    print("This histogram:")
    histogram(my_list)

elif task == "check if the palindrome is a string":
    print("Enter string:")
    word = input()
    print(Palindrome(word))