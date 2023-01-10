# Вычислить число c заданной точностью d

from math import pi
d = str(input("Задайте точность числа Пи:"))

d_num = abs(d.find('.') - len(d)) - 1

pi_d = round (pi, d_num)
print ('число Пи с точностью', d, '=', pi_d)