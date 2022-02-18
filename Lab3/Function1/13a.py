def counter(num, name):
    c = 0
    while True:
        a = int(input())
        if a == number:
            c += 1
            print (f'Good job, {name}! You guessed my number in {c} guesses! ')
            exit()
        if a < number:
            c += 1
            print('Your guess is too low.')
        if a > number:
            c += 1
            print('Your guess is too big.')
import random
print("Hello! What is your name?")
name = input() #ввести свое имя для игры
print ("Well, "  + name + ", I am thinking of a number between 1 and 20." )
print("Take a guess.")
number = random.randint(1, 20) #компьютер загадает рандомное число от 1 до 20
counter(number, name)
