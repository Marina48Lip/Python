# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# Входные и выходные данные хранятся в отдельных текстовых файлах.



with open('text1.txt', 'r', encoding='utf-8') as data:  
    old_text = data.read().split()
print(old_text)
new_text = list(filter(lambda word: 'а' not in word and 'б' not in word and 'в' not in word, old_text))
print(new_text)
data = open('text2.txt', 'a', encoding='utf-8')
data.writelines(''.join(str(new_text)))
data.close()
