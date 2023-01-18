# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def coding(text):
    count = 1
    res = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            res = res + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        res = res + str(count) + text[-1]
    return res


def decoding(text):
    number = ''
    res = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            res = res + text[i] * int(number)
            number = ''
    return res


s = input("Введите текст: ")
print('Текст после сжатия:', coding(s))
print('Текст после восстановления:', decoding(coding(s)))