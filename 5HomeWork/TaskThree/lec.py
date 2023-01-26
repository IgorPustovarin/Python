# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

# count = 0
# text = '5a4b3c'
# result = ''
# my_list = []
# for i in text:
#     my_list.append(i)
# for i in range(len(my_list)):
#     if (my_list[i].isdigit()):
#         count = my_list[i]
#         result = result + my_list[i+1] * int(count)
# print(result) #Реализовал механизм разжатия архива

count = 0
text2 = 'fffggWWWWWt'
result2 = ''
for i in range(len(text2)):
        if text2[i-1] != text2[i]:
            count = text2.count(text2[i])
            result2 = result2 + str(count) + text2[i]
            print(count)
print(result2)#Реализовал алгоритм сжатия
    




# range(len(my_list))
# for i in text:
#     # last = i
#     print(text[i+1])
#     if (i.isdigit()):#Нашел интересную проверку на то, является ли символ числом или нет, от этого сейчас и буду плясать
#         count = int(i)
#         print(count)
#         print('работает')
    # else:
    #     last = i
    
# my_list = list(map(int, my_list.split())) #Перевод из строки в интеджер
# print(my_list)

# for i, item in enumerate(my_list):# Нумерует каждый элемент списка
#     print(i, item)
# b = last*count
# b = b + c*count2
# print(b)