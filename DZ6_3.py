# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.

n = int(input('Введите количество друзей: '))
friends = {}
for i in range(n):
    name = input('Введите имя: ')
    age = int(input('Введите возраст:'))
    friends[name]= age

print(friends)
print('Самый младший из друзей: ', min(friends, key=friends.get))