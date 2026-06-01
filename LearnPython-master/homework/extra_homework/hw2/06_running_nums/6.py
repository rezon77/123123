lst = [1, 4, -3, 0, 10]
k = int(input("Сдвиг: "))

print(f"Изначальный список: {lst}")

k = k % len(lst)

shifted_lst = lst[-k:] + lst[:-k]

print(f"Сдвинутый список: {shifted_lst}")