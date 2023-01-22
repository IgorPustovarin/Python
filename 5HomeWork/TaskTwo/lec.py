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
my_listComp = []
my_listUser = []
playComp = 0
count = 8
temp = 0
countWinComp = 0
countWinUser = 0
#my_listResult = []
if (numberGamer == 2):
    for i in range(10):
        numberRandom = random.randint(0,count)
        #print(f'Индекс numberRandom {numberRandom}')
        temp = numberRandom
        playComp = my_listGame[numberRandom]
            
        #print(my_listGame)
        print(f"Компьютер закрывает ячейку {playComp}")
        if (playComp >= 0 and playComp < 4):
            #if (numberRandom != 0):
            playComp = playComp -1
            my_list[playComp] = '0'
        elif (playComp > 3 and playComp < 7):
            playComp = playComp - 4
            my_list2[playComp] = '0'
        elif (playComp > 6 and playComp < 10):
            playComp = playComp - 7
            my_list3[playComp] = '0'
        my_listComp.append(my_listGame[temp])
        my_listGame.pop(temp)
        count = count - 1
        print(my_list)
        print(my_list2)
        print(my_list3)
        if (len(my_listGame) == 0):
            print("Игра закончена")
            break

        #print(my_listGame)
        number = int(input("Какую ячейку закроешь ты "))
        for i in range(len(my_listGame)):
            if (number == my_listGame[i]):
                temp = i
                #print(f'Индекс удаляемого элемента + {temp}')
        if (number >= 0 and number < 4):
            number = number -1
            my_list[number] = 'X'
        elif (number > 3 and number < 7):
            my_list2[number - 4] = 'X'
        elif (number > 6 and number < 10):
            number = number - 7
            my_list3[number] = 'X'
        my_listUser.append(my_listGame[temp])
        my_listGame.pop(temp)
        count = count - 1
        print(my_list)
        print(my_list2)
        print(my_list3)
        print(f"Комбинация компьбтера {my_listComp}")
        print(f"Комбинация игрока {my_listUser}")
        print()
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==1 or my_listComp[i] == 2 or my_listComp[i] == 3):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==1 or my_listComp[i] == 4 or my_listComp[i] == 7):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==2 or my_listComp[i] == 5 or my_listComp[i] == 8):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==3 or my_listComp[i] == 6 or my_listComp[i] == 9):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==4 or my_listComp[i] == 5 or my_listComp[i] == 6):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==7 or my_listComp[i] == 8 or my_listComp[i] == 9):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==1 or my_listComp[i] == 5 or my_listComp[i] == 9):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==7 or my_listComp[i] == 5 or my_listComp[i] == 3):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
            
            
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==1 or my_listUser[i] == 2 or my_listUser[i] == 3):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==1 or my_listUser[i] == 4 or my_listUser[i] == 7):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==2 or my_listUser[i] == 5 or my_listUser[i] == 8):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==3 or my_listUser[i] == 6 or my_listUser[i] == 9):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==4 or my_listUser[i] == 5 or my_listUser[i] == 6):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==7 or my_listUser[i] == 8 or my_listUser[i] == 9):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==1 or my_listUser[i] == 5 or my_listUser[i] == 9):
                countWinUser = countWinUser +1
            if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==7 or my_listUser[i] == 5 or my_listUser[i] == 3):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        if (len(my_listGame) == 0):
            print("Игра закончена")
            break

if (numberGamer == 1):
    for i in range(10):
        number = int(input("Какую ячейку закроешь ты "))
        for i in range(len(my_listGame)):
            if (number == my_listGame[i]):
                temp = i
                #print(f'Индекс удаляемого элемента + {temp}')
        if (number >= 0 and number < 4):
            number = number -1
            my_list[number] = 'X'
        elif (number > 3 and number < 7):
            my_list2[number - 4] = 'X'
        elif (number > 6 and number < 10):
            number = number - 7
            my_list3[number] = 'X'
        my_listUser.append(my_listGame[temp])
        my_listGame.pop(temp)
        count = count - 1
        print(my_list)
        print(my_list2)
        print(my_list3)
        if (len(my_listGame) == 0):
            print("Игра закончена")
            break

        numberRandom = random.randint(0,count)
        #print(f'Индекс numberRandom {numberRandom}')
        temp = numberRandom
        playComp = my_listGame[numberRandom]
            
        #print(my_listGame)
        print(f"Компьютер закрывает ячейку {playComp}")
        if (playComp >= 0 and playComp < 4):
            #if (numberRandom != 0):
            playComp = playComp -1
            my_list[playComp] = '0'
        elif (playComp > 3 and playComp < 7):
            playComp = playComp - 4
            my_list2[playComp] = '0'
        elif (playComp > 6 and playComp < 10):
            playComp = playComp - 7
            my_list3[playComp] = '0'
        my_listComp.append(my_listGame[temp])
        my_listGame.pop(temp)
        count = count - 1
        print(my_list)
        print(my_list2)
        print(my_list3)
        if (len(my_listGame) == 0):
            print("Игра закончена")
            break
        print(f"Комбинация компьбтера {my_listComp}")
        print(f"Комбинация игрока {my_listUser}")
        print()
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==1 or my_listComp[i] == 2 or my_listComp[i] == 3):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==1 or my_listComp[i] == 4 or my_listComp[i] == 7):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==2 or my_listComp[i] == 5 or my_listComp[i] == 8):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==3 or my_listComp[i] == 6 or my_listComp[i] == 9):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==4 or my_listComp[i] == 5 or my_listComp[i] == 6):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==7 or my_listComp[i] == 8 or my_listComp[i] == 9):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==1 or my_listComp[i] == 5 or my_listComp[i] == 9):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
        countWinComp = 0
        for i in range(len(my_listComp)):
            if (my_listComp[i] ==7 or my_listComp[i] == 5 or my_listComp[i] == 3):
                countWinComp = countWinComp +1
                if (countWinComp == 3):
                    print("Компьютер выиграл")
            
            
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==1 or my_listUser[i] == 2 or my_listUser[i] == 3):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==1 or my_listUser[i] == 4 or my_listUser[i] == 7):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==2 or my_listUser[i] == 5 or my_listUser[i] == 8):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==3 or my_listUser[i] == 6 or my_listUser[i] == 9):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==4 or my_listUser[i] == 5 or my_listUser[i] == 6):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==7 or my_listUser[i] == 8 or my_listUser[i] == 9):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==1 or my_listUser[i] == 5 or my_listUser[i] == 9):
                countWinUser = countWinUser +1
            if (countWinUser == 3):
                    print("Игорок выиграл")
        countWinUser = 0
        for i in range(len(my_listUser)):
            if (my_listUser[i] ==7 or my_listUser[i] == 5 or my_listUser[i] == 3):
                countWinUser = countWinUser +1
                if (countWinUser == 3):
                    print("Игорок выиграл")
        if (len(my_listGame) == 0):
            print("Игра закончена")
            break