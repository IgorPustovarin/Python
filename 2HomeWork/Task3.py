# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int
import random

my_list =[]
for i in range(10):
    my_list.append(random.randint(0,100))
print(my_list)
count = 0
my_listResult = []
for count in range(40):
    numberRandom = random.randint(0,9)
    if my_list [numberRandom] != -1:
        my_listResult.append(my_list [numberRandom])
        count = count + 1
    my_list [numberRandom] = -1
print(my_listResult)