text = input("Введите текст: ")
vowels = [letter for letter in text.lower() if letter in 'аеёиоуыэюя']

print(f"\nСписок гласных букв: {vowels}")
print(f"Длина списка: {len(vowels)}")
