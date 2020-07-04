# Цикл for
# Функция range

# Вычислим чётные и нечётные числа
a = int(input('Введите число, до которого будем считать: '))

for i in range(1, a+1):
    if i % 2 == 0:
        print(f'{i} — чётное число')
    else:
        print(f'{i} — нечётное число')

print('')

# Лист тьюплов и его вызов
persons = [('John', 22), ('Vova', 31), ('Andrey', 24)]

for (name, age) in persons:
    print(f'{name} is {age} years old.')
