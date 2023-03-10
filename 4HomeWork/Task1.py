# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k = int(input('Введите натуральную степень k = '))
lst = []
for i in range(k+1):
    lst.append(randint(0, 100))
result = []
for i in range(k,-1,-1):
    if lst[i] != 0:
        if i == 0:
            result.append(f'{lst[i]}')
        elif i == 1:
            result.append(f'{lst[i]}*x')
        else:
            result.append(f'{lst[i]}*x^{i}')
print(" + ".join(result) + " = 0")
with open ('file.txt', 'w') as data:
    data.write(" + ".join(result) + " = 0")
