# Вычисляем длину строки
greeting = 'Hello Python!'
greeting_length = len(greeting)
print(len(greeting))

# А сейчас получаем элемент строки по его номеру в строке
# Indexing
print(greeting[6])
print(greeting[-1])

# Вырезание кусочков
# Slicing
print(greeting[0:5])
print(greeting[-7:-1])
print(greeting[6:])
print(greeting[::2])
print(greeting[2::3])
print(greeting[1:9:3])

print(greeting[::-1])  # Обратный порядок символов в строке

# Multiplication
yummy = "Yum"
print(yummy * 2)

my_name = "Вова! "
print(my_name * 3)

# Methods
my_full_name = 'владимир РОМАНОВИЧ МоДеНоВ'
print(my_full_name.upper())
print(my_full_name.lower())

very_long_string = "This is the very very very long string"
print(very_long_string.split())

# Concatenate
age = 23
print('Валере ' + str(age) + ' года.')
print('А Анне ' + str(27) + ' лет.')

# Placeholders - Заполнители
name = "Jack"
name_and_age = "My name is {0} and I am {1} years old.".format(name, age)
print(name_and_age)
name_and_age = "My name is {0} and I am {1} years old.".format("Jack", 23)
print(name_and_age)
name_and_age = "My name is {nm} and I am {ag} years old.".format(nm="Jack", ag=23)
print(name_and_age)

# Float in String
float_result = 1000 / 7
print(float_result)
print('The result of division is {0:1.3f}'.format(float_result))
