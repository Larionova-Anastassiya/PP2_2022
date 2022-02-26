#чтобы вычесть пять дней из текущей даты.

from datetime import date
from datetime import timedelta

ans = date.today() - timedelta(days = 5)

#date.today() --> выведет дату сегодняшнюю
#timedelta() --> принимает определенное наше значение (5 дней)
#базовые операторы для получения прошлого или будущего времени

print('Date :',date.today())
print('5 days before:',ans)
