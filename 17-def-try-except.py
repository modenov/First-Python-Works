# Вызов функции
# Обработка исключений

x = int(input('Введите делимое: '))
y = int(input('Введите делитель: '))


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print('Ты шо на ноль делишь, еблан! В школе не учился?')


print(divide(x, y))
