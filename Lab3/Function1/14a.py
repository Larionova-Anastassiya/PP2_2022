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
    imp1 = __import__('1')

elif task == "Fahrenheit to Celsius":
    print("Enter Fahrenheit temperature:")
    imp2 = __import__('2')
    Fahrenheit = int(input())
    Celsia = centigrade(Fahrenheit)
    print(f"{Fahrenheit} fahrenheit is {Celsia} centigrade")

elif task == "reverse words in string":
    print("Enter string:")
    imp3 = __import__('6') # слова перевернет местами в предложении, если без сплита то буквы все.

elif task == "check if 007 contains":
    print("Enter list, example (1,2,3,4,...):")
    imp4 = __import__('8')

elif task == "check if 33 contains":
    print("Enter list, example (1 2 3 4 ...):")
    imp5 = __import__('7')

elif task == "find volume sphere":
    print("Enter radius:")
    imp6 = __import__('9')

elif task == "make a histogram":
    print("Enter list, example (1,2,3,4,...):")
    imp7 = __import__('12')

elif task == "check if the palindrome is a string":
    print("Enter string:")
    imp8 = __import__('11')