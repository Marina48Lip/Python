# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random
n = int(input('Введите количество элементов:'))
list = []
for i in range(n):
    list.append(random.randint(1, 10))
print(list)

new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
#print(new_list)
print('Количество различных элементов =', len(new_list))
