# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.

n = int(input('Введите количество друзей: '))
friends = {}
for i in range(n):
    name = input('Введите имя: ')
    age = int(input('Введите возраст:'))
    friends[name]= age

print()

ages = friends.values()
sum = 0
for i in ages:
    sum = sum+ i
print('Средний возраст всех друзей = ', int(sum/n))

names = friends.keys()
print('Самое длинное имя: ', max(names, key=len))
