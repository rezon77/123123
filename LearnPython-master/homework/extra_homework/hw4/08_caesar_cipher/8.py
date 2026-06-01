def encrypt_message(message, shift):
    lower_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    upper_alphabet = lower_alphabet.upper()
    encrypted_text = []

    for symbol in message:
        if symbol in lower_alphabet:
            new_index = (lower_alphabet.index(symbol) + shift) % len(lower_alphabet)
            encrypted_text.append(lower_alphabet[new_index])
        elif symbol in upper_alphabet:
            new_index = (upper_alphabet.index(symbol) + shift) % len(upper_alphabet)
            encrypted_text.append(upper_alphabet[new_index])
        else:
            encrypted_text.append(symbol)

    return ''.join(encrypted_text)


message = input("Введите сообщение: ")
shift = int(input("Введите сдвиг: "))

print(f"Зашифрованное сообщение: {encrypt_message(message, shift)}")
