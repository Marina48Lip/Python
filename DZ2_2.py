# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

N = int(input('Введите число: '))
n_pr = 1
print('N = ', N, 'тогда [', end='')
for i in range(1, N):
    n_pr = n_pr*i
    print(n_pr, end=',')
print(n_pr*N, end=']')
