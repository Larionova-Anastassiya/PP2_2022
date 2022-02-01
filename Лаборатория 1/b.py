text = str(input().strip()) #ввести самим слово и разделить его
summ = 0 #сумма начальная к которой будем прибабвлять
for char in text:
    summ += ord(char)
    """нашли по ASCII коду значения и прибавили их с помощью for"""
if summ > 300: #выполняемое условие
    print("It is tasty!")
else:
    print("Oh, no!")
