#для печати вчера, сегодня, завтра.

from datetime import date
from datetime import timedelta

yesterday = date.today() - timedelta(hours = 24) #отнимет один день. точнее 24 часа
tomorrow = date.today() + timedelta(hours = 24) #прибавит один день или 24 часа
#date.today() --> выведет дату сегодняшнюю
#timedelta() --> принимает определенное наше значение (5 дней)
#базовые операторы для получения прошлого или будущего времени
print('yesterday:', yesterday)
print('Date :',date.today())
print('5 days before:', tomorrow)