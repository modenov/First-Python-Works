# Отработка if и else

# Сравнение двух чисел
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

if a > b:
    print(f'{a} больше {b}!')
elif a < b:
    print(f'{b} больше {a}!')
elif a == b:
    print('Эти числа равны!')
else:
    print('Чёт какая-то ерунда, я не смог узнать результат!')
