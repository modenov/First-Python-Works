# Calculating of credit final sum

print('Сейчас расчитаем ваш кредит')
need_sum = int(input('Введите желаемую сумму: '))
numbers_of_years = int(input('На сколько лет хотите взять кредит? '))
credit_rate = int(input('Введите процентную ставку банка: '))
final_sum = need_sum + need_sum / 100 * credit_rate * numbers_of_years

print(f'Платить придётся {final_sum} рублей!')
