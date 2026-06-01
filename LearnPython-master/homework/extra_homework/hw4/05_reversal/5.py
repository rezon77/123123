text = input("Введите строку: ")
first_h_index = text.find('h')
last_h_index = text.rfind('h')
reversed_part = text[first_h_index + 1:last_h_index][::-1]

print(f"Развёрнутая последовательность между первым и последним h: {reversed_part}")
