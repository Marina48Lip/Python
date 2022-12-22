# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Введите число n: '))
print('Для N=', n, ': {', end = '')
for i in range(1, n):
    print(' ', i, ':', round((1+1/i)**i, 2), end=',')
print(' ', n, ':', round((1+1/n)**n, 2), end='}')
sum = 0
for i in range(1, n+1):
    sum+=round((1+1/i)**i, 2)
print('\nСумма = ', sum)