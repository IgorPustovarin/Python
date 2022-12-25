# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование библиотеки Random для получения случайного int
import random

my_list =[]
for i in range(10):
    my_list.append(random.randint(0,100))
print(my_list)
count = 10
my_listResult = []
for i in range(10):
    numberRandom = random.randint(0,count)
    my_listResult.append(my_list [numberRandom])
    count = count - 1
    my_list.pop(numberRandom)
print(my_listResult)