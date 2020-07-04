import random

tries = 0

number = random.randint(1,50)

print('Хмм... А угадаешь число от 1 до 50, которое я загадал?')

while tries < 6:
    guess = int(input('Попробуй угадать: '))

    tries += 1

    if guess < number:
        print('Нет! Этого мало!')

    if guess > number:
        print('Неа, в этот раз много!')

    if guess == number:
        print(f'Поздравляю! Тебе удалось угадать моё число "{number}" за {tries} попытки(ок).')
        break

    if guess != number and tries == 6:
        print(f'Прости, но тебе не удалось угадать моё число. Я загадывал "{number}".')
        break
