#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

a = input('Введите число: ')
sum = 0
for i in a:
    if i !='.':
        sum+=int(i)
print(sum) 
