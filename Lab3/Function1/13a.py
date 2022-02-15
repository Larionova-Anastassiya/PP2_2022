def counter(num):
    def inner(inp, number):
        inner.count += 1
        return num(inp, number)
    inner.count = 0
    return inner
def num(inp,number):
    #c = 1  # начальный счетчик если угадаем сразу
    while inp != number:  # условия если не угадали и давать подсказки
        if inp < number:
            print("Your guess is too low.")
        elif inp > number:
            print("Your guess is too high.")
        print("Take a guess.")
        inp = input()
        inp = int(inp)  # вводим вновь число
        #c += 1  # счетчик добавляет попытки
import random
print("Hello! What is your name?")
name = input() #ввести свое имя для игры
print ("Well, "  + name + ", I am thinking of a number between 1 and 20." )
print("Take a guess.")
number = random.randint(1, 20) #компьютер загадает рандомное число от 1 до 20
inp = int(input()) #мы вводим число любое
#c = 1 #начальный счетчик если угадаем сразу
c = counter(num)
num(inp, number)
print (f'Good job, {name}! You guessed my number in {c} guesses!" ') #выведет имя и за сколько попыток

#не работает счетчик попыток (спросить)