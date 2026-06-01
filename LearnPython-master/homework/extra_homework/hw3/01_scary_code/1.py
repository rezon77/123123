a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
count_fives = a.count(5)
print(f"Кол-во цифр 5 при первом объединении: {count_fives}")

while 5 in a:
    a.remove(5)

a.extend(c)
count_threes = a.count(3)
print(f"Кол-во цифр 3 при втором объединении: {count_threes}")
print(f"Итоговый список: {a}")
