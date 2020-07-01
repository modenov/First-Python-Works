# Разделяем строку по определённому символу

import sys
sys.getfilesystemencoding()

data = "12;10;8;10"
separated_data = data.split(';')
print(separated_data)
print('И класс у нас ' + str(type(separated_data)) + ' получается!')

# Также можно ФИО разделять по пробелу!
my_name = "Владимир Романович Моденов"
separated_my_name = my_name.split(' ')
print(separated_my_name)
