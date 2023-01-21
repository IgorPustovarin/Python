# Создайте программу для игры в 'Крестики-нолики'
import random
# from random import randint
numberGamer = random.randint(1,2)
name = input('Введи своё имя уважаемый игрок ')
print(name + " давай сыграем в крестики-нолики, компьютер будет ходить всегда ноликами")
if numberGamer == 1:
    print('Первым ходит ' + name)
elif numberGamer == 2:
    print('Первым ходит компьютер')
my_listGame = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list = ['1', '2', '3']
my_list2 = ['4', '5', '6']
my_list3 = ['7', '8', '9']
playComp = 0
count = 8
temp = 0
#my_listResult = []
for i in range(6):
    numberRandom = random.randint(0,count)
    temp = numberRandom
    print(numberRandom)
    print(my_listGame)
    numberRandom = my_listGame[numberRandom]
    print(f"Компьютер закрывает ячейку {numberRandom}")
    if numberRandom >= 0 and numberRandom < 4:
        if numberRandom != 0:
            numberRandom = numberRandom -1
        my_list[numberRandom] = '0'
    elif numberRandom > 3 and numberRandom < 7:
        numberRandom = numberRandom - 4
        my_list2[numberRandom] = '0'
    elif numberRandom > 6 and numberRandom < 10:
        numberRandom = numberRandom - 7
        my_list3[numberRandom] = '0'
    my_listGame.pop(temp)
    count = count - 1
    print(my_list)
    print(my_list2)
    print(my_list3)
    number = int(input("Какую ячейку закроешь ты "))
    #number2 = number
    for i in range(9):
        # print(i)
        # print(my_listGame[i])
        # print(number)
        if my_listGame[i] == number:
            temp = i
            print(i)
        break
        
    if number >= 0 and number < 4:
        if numberRandom != 0:
            numberRandom = numberRandom -1
        my_list[i] = 'X'
        for i in range(2):
            if my_list[i] == number:
                my_list[i] = 'X'
        my_listGame.pop(temp)
    # elif number2 > 3 and number2 < 7:
    #     for i in my_list2:
    #         if i == number2:
    #             my_list2[i] = 'X'
    #         #continue
    #     #number = number - 4
        
    #     my_listGame.pop(temp)
    # elif numberRandom > 6 and numberRandom < 10:
    #     number = number - 7
    #     my_list3[number] = 'X'
    #     my_listGame.pop(temp)
    # count = count - 1
    print(my_list)
    print(my_list2)
    print(my_list3)



# import random

# my_list =[]
# for i in range(10):
#     my_list.append(random.randint(0,100))
# print(my_list)
# count = 10
# my_listResult = []
# for i in range(10):
#     numberRandom = random.randint(0,count)
#     my_listResult.append(my_list [numberRandom])
#     count = count - 1
#     my_list.pop(numberRandom)
# print(my_listResult)