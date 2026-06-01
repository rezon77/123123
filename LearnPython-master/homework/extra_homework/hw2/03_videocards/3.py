n = int(input("Количество видеокарт: "))
cards = []

for i in range(n):
    card = int(input(f"{i + 1} Видеокарта: "))
    cards.append(card)

print(f"\nСтарый список видеокарт: {cards}")

max_card = max(cards)

new_cards = [card for card in cards if card != max_card]

print(f"Новый список видеокарт: {new_cards}")