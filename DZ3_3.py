# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов.

a = list(map(float, input('Введите список из вещественных чисел: ').split()))
sum = 0
b = []
for i in a:
    if i%1 != 0:
        b.append(round((i % 1), 2))
print('Разница между максимальным и минимальным значением дробной части элементов = ', end='')         
print(round(max(b) - min(b), 2))