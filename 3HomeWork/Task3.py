# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_list = [1.1, 1.2, 3.1, 5, 10.01]
# i = 0
# temp = 0
# min = my_list[i]
# max = temp
# for i in range(len(my_list)):
#     temp = round(my_list[i] - (my_list[i]//1), 2)
#     if (temp != 0):
#         if (min >temp):
#             min = temp
#         elif (max < temp):
#             max = temp
# print(max - min)