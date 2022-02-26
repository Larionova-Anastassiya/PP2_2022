import datetime
ans = datetime.datetime.today().replace(microsecond=0) #без милисекунд вызов из библиотеки (сегодня полное)
#replace --> заменяет микросекунды убирая их
#dt = datetime.datetime.today()    с милисекундами
print(ans)