# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# my_list = [2, 3, 4, 5, 6]
# a = 0
# if (len(my_list)%2 !=0):
#     l = len(my_list)//2 + 1
# if (len(my_list)%2 ==0):
#     l = len(my_list)//2
# countRevers = len(my_list) - 1
# for i in range(l):
#     a = 0
#     a = my_list[i] * my_list[countRevers]
#     countRevers = countRevers - 1 
#     print(a)
# Реализация с помощью новых операторов
# Формат: Объясняет преподаватель
# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
my_list = [2, 3, 4, 5, 6, 7]
countRevers = len(my_list)-1
if (len(my_list)%2 !=0):
    my_list = [my_list[x] * my_list[countRevers - x]  for x in range(len(my_list)//2+1)]
if (len(my_list)%2 ==0):
    my_list = [my_list[x] * my_list[countRevers - x]  for x in range(len(my_list)//2)]
print(my_list)