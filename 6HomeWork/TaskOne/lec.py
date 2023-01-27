#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# number = float(input('Введите вещественное число '))
# result = 0
# if number != int(number):
#     number = round(number, 7)
#     print(number)
#     while (number != int(number)):
#         number = number * 10
#         print(int(number))
# # if number == int(number):
# while (1 <= number):
#     result = result + number % 10
#     number = number / 10
# print(int(result))

# Реализация с помощью новых операторов
# Формат: Объясняет преподаватель
# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

result = 0
number = str(input("Введите вещественное число "))
my_list = [number[i] for i in range(len(number))]
my_list = list(map(int, my_list))
for i in range(len(my_list)):
    result = result + my_list[i]
print(result)