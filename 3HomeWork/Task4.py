# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

# number = int(input('Введите десятичное число и переведем его в двоичное ')) 
# temp = 0
# result = 0
# my_list = []
# while (number >= 1):
#     if (number / 2 == number // 2):
#         temp = 0 
#         number = number / 2
#         my_list.append(temp)
#         # print(my_list)
#     elif (number//2 != number/2):
#         temp = 1
#         number = number // 2
#         my_list.append(temp)
#         # print(my_list)
#         # print(number)
# # print(my_list)
# count = len(my_list) - 1
# for i in range(len(my_list)):
#     result = result + my_list[count]
#     count = count - 1
#     result = result * 10
# print(int(result/10))