# Задайте список из n чисел последовательности (1 + 1/n)**n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06
number = int(input('Введите число: ')) 

def funkciya(n):
    return [round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]

nums = funkciya(number)
print(nums)
print(round(sum(nums), 2))