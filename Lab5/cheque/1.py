import re, sys

txt = sys.stdin.read()

print('Компания:', re.search(r'Филиал (.+)', txt)[1])
print('БИН:', re.search(r'БИН (.+)', txt)[1])
print('Адресс:', re.search(r'г\..+', txt)[0])
print('Дата и время:', re.search(r'Время: (.+)', txt)[1])
items = re.findall(r'(\d{1,2})\.\n(.+)\n(\d).+x (.+),', txt)

for item in items:
    print(f"{item[0]}. {item[1]}\nКол-во: {item[2]} шт\nЦена: {item[3]}тг\nВ сумме: {int(item[2]) * int(''.join(item[3].split()))}тг\n")
