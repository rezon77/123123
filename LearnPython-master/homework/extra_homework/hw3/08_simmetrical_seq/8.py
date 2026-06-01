numbers_count = int(input("Кол-во чисел: "))
numbers = []

for _ in range(numbers_count):
    numbers.append(int(input("Число: ")))

numbers_to_add = []

for index in range(len(numbers)):
    if numbers[index:] == numbers[index:][::-1]:
        numbers_to_add = numbers[:index][::-1]
        break

print(f"\nПоследовательность: {numbers}")
print(f"Нужно приписать чисел: {len(numbers_to_add)}")
print(f"Сами числа: {numbers_to_add}")
