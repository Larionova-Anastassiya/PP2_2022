# разница в двух датах в секундах чтобы была
from datetime import datetime
from datetime import time


def dis(data2, data1):  # разница в двух датах в секундах
    ans = data2 - data1  # найдет разницу между датами
    return ans.days * 24 * 3600 + ans.seconds  # на 24 часа и 3600 секунд (в часе) умножаем на дни и прибавляем оставшиеся секунды ответа


# first date (my birthday)
date1 = datetime.strptime('2003-06-03 12:45:30', '%Y-%m-%d %H:%M:%S')
"""
%H — представляет «часы» в 24-часовом формате. 
%M — Представление минут в виде десятичного числа. 
%S — представляет часть метки времени, равную «секундам».
%Y-%m-%d — год, месяц, день
"""

# second date (now)
date2 = datetime.now()
ans = dis(date2, date1)  # выполняет функцию с нашими датами
print(f"{ans} seconds")
