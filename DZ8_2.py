'''Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром Цезаря и возвращает его. 
Шифр Цезаря заменяет каждую букву в тексте на букву, которая отстоит в алфавите на некоторое фиксированное число позиций.
В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша функция кодирует сдвиг алфавита на 3 позиции:
А→Г,А→Г,
Б→Д,Б→Д,
В→Е,В→Е,
...
Все символы, кроме русских букв должны остаться неизменными. Маленькие буквы должны
превращаться в маленькие, большие — в большие.
Напишите также функцию декодирования decrypt_caesar(msg, shift), также
использующую сдвиг по умолчанию. При написании функции декодирования используйте
вашу функцию кодирования.''' 

def encrypt_caesar(msg, shift):
    encrypted = ""
    for i in range(len(msg)):                                 
        index = msg[i]
        if 1040 <= ord(index) <= 1071 or 1072 <= ord(index) <= 1103:      
                number = ord(index) + shift
                if index == index.upper():
                    if number > 1071:
                        number -= 32
                if index == index.lower():
                    if number > 1103:
                        number -= 32
                encrypted = str(encrypted) + str(chr(number))
        else:
            encrypted = str(encrypted) + str(index)
    return encrypted
 
def decrypt_caesar(encrypted, shift):
    decrypted = ""
    for i in range(len(encrypted)):                                 
        index = encrypted[i]
        if 1040 <= ord(index) <= 1071 or 1072 <= ord(index) <= 1103:      
                number = ord(index) - shift
                if index == index.upper():
                    if number > 1071:
                        number -= 32
                if index == index.lower():
                    if number > 1103:
                        number -= 32
                decrypted = str(decrypted) + str(chr(number))
        else:
            decrypted = str(decrypted) + str(index)
    return decrypted
                                                                                                            
 
msg = input("Введите текст: ")
shift = int(input('Введите шаг: '))
 
encrypt_caesar(msg, shift)
encrypted = encrypt_caesar(msg, shift)
decrypt_caesar(encrypted, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)