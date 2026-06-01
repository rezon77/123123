guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f"\nСейчас на вечеринке {len(guests)} человек: {guests}")
    status = input("Гость пришёл или ушёл? ")

    if status == 'Пора спать':
        break

    guest_name = input("Имя гостя: ")

    if status == 'пришёл':
        if len(guests) < 6:
            guests.append(guest_name)
            print(f"Привет, {guest_name}!")
        else:
            print(f"Прости, {guest_name}, но мест нет.")
    elif status == 'ушёл':
        guests.remove(guest_name)
        print(f"Пока, {guest_name}!")

print("\nВечеринка закончилась, все легли спать.")
