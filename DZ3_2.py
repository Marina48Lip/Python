# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

a = input('Введите список из нескольких чисел: ').split()
n = len(a)
sp_pr = []
print(a, '=> ', end='')
for i in range((n+1)//2):
    sp_pr.append(int(a[i])*int(a[n-i-1]))
print(sp_pr)
