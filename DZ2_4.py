# Реализуйте алгоритм перемешивания списка.

import random
text = 'В лесу родилась елочка в лесу она росла'
text2 = text.split(' ')
print(text2)
random.shuffle(text2)
print(text2)
