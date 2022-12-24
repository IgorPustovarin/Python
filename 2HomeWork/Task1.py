# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
number = float(input('Введите вещественное число '))
result = 0
if number != int(number):
    number = round(number, 7)
    print(number)
    while (number != int(number)):
        number = number * 10
        print(int(number))
# if number == int(number):
while (1 <= number):
    result = result + number % 10
    number = number / 10
print(int(result))