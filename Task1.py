#В задании дана цель создать простой шифр Цезаря, а также второй функцией дешифратор к нему
#Дешифратор работает только на латиницу, для кириллицы нужна функция, в которой будет прописан кириллический алфавит
def caesar_cipher():
    entered_text = str(input("Введите текст для шифровки: "))
    if not entered_text:
        return
    try:
        key_cipher = int(input("Количество элементов для шифрования: "))
    except ValueError:
        return entered_text
    if key_cipher <= 0:
        return entered_text

    ciphered_text = ""
    for ch in entered_text:
        if ch.isalpha():
            alph_stay = ord(ch) + key_cipher
            if alph_stay > ord('z'):
                alph_stay -= 26
            final_letter = chr(alph_stay)
            ciphered_text += final_letter
    print("Ваш зашифрованный текст: ", ciphered_text)
    return ciphered_text


ciphered_text = caesar_cipher()


# Функция дешифровки будет отличаться, потому что в прошлой отсутсвовала возможность отбросить символы, которые были
# за буквой "a"
def caesar_decipher():
    decipher_text = ciphered_text
    if not decipher_text:
        return
    try:
        key_decipher = int(input("Количество элементов для дешифрования: "))
    except ValueError:
        return decipher_text
    if key_decipher <= 0:
        return decipher_text
    eng_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted_alphabet = eng_alphabet[26 - key_decipher:] + eng_alphabet[0:(26 - key_decipher)]
    cipher_text = ""

    for i in range(len(decipher_text)):
        char = decipher_text[i]
        idx = eng_alphabet.find(char.upper())
        if idx == -1:
            cipher_text = cipher_text + char
        elif char.islower():
            cipher_text = cipher_text + shifted_alphabet[idx].lower()
        else:
            cipher_text = cipher_text + shifted_alphabet[idx]
    print("Дешифровка вашего текста: ", cipher_text)
    return cipher_text


caesar_decipher()
