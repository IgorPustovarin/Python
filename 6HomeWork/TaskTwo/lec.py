# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# my_list = [2, 3, 5, 9, 3]
# result = 0
# for i in range(len(my_list)):
#     if (i % 2 != 0):
#         result = result + my_list[i]
#         print(my_list[i])
# print(result)

# Реализация с помощью новых операторов
# Формат: Объясняет преподаватель
# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
result = 0
my_list = [2, 3, 5, 9, 3]
my_list = [my_list[x] for x in range(len(my_list)) if x%2 ==1]
for i in range(len(my_list)):
    result = result + my_list[i]
print(result)