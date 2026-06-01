n = int(input("Введите длину списка: "))
result = [1 if index % 2 == 0 else index % 5 for index in range(n)]

print(f"Результат: {result}")
