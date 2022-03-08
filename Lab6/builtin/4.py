# функцию квадратного корня через определенные миллисекунды

from time import sleep #выполнит код с задержкой
import math

def func(fn, ms, *args):
  sleep(ms / 1000) #задержка в милисекундах
  return fn(*args)

n = int(input()) #25100  значения для корня
m = int(input()) #2123  задержка
ans = func(lambda x: math.sqrt(x), m, n)
print(f"Square root of {n} after {m} miliseconds is {ans}")
#Square root of 25100 after 2123 miliseconds is 158.42979517754858

"""
lambda x: math.sqrt(x) --> лямбда функция выполняющая корень значения
sleep(ms / 1000) --> вызов задержки после определенного момента
*args - произвольное число позиционных аргументов, передается список аргументов, заключенных в кортеж
"""