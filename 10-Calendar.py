# Показываем календарь!

import calendar

year_var = input('Какой год показать? Введите в формате ХХХХ: ')
month_var = input('А месяц? Введите в формате Х или ХХ: ')

print(calendar.month(int(year_var), int(month_var)))
