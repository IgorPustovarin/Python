# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
numberPlace = int(input('Введите номер плоскости от 1 до 4 и увидите предположительные координаты X и Y '))
if(numberPlace == 1):
    print('Возможны координаты при X > 0 и Y > 0 ')
if(numberPlace == 2):
    print('Возможны координаты при X > 0 и Y < 0 ')
if(numberPlace == 3):
    print('Возможны координаты при X < 0 и Y < 0 ')
if(numberPlace == 4):
    print('Возможны координаты при X < 0 и Y > 0 ')