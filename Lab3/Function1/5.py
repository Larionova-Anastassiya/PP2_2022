#Write a function that accepts string from user and print all permutations of that string
def permute(str, ans):
    if (len(str) == 0):
        #print(ans, end="  ")
        print(ans) #выведет сразу ответ когда размер строки 0
        return
    for i in range(len(str)): #для каждого элемента в строке
        k = str[i] #значение каждой буквы циклом
        left = str[0:i] #влево элемент слова до буквы
        right = str[i + 1:] #вправо элемент слова от буквы и до конца
        n = left + right #сложит результат сдвигов
        permute(n, ans + k) #пройдет по функции для проверки
ans = ""
str = input("String: ")
print("All possible: ")
permute(str, ans) #выведет все перестановки слова как на английском, так и на русском