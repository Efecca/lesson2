import locale
locale.setlocale(locale.LC_ALL, "russian")
from datetime import date, timedelta,datetime
#Напечатайте в консоль даты: вчера, сегодня, месяц назад
now=datetime.today()
print('Вчера: {}'.format((now-timedelta(1)).strftime('%d %B %Y')))
print('Сегодня: {}'.format(now.strftime('%d %B %Y')))
print('Месяц назад: {}'.format((now-timedelta(365/12)).strftime('%d %B %Y')))
#Превратите строку "01/01/17 12:10:03.234567" в объект datetime
new_date = datetime.strptime("01/01/17 12:10:03.234567","%d/%m/%y %H:%M:%S.%f")
print(new_date)