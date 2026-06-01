n = int(input("Количество контейнеров: "))
containers = []

for _ in range(n):
    weight = int(input("Введите вес контейнера: "))
    if weight <= 200:
        containers.append(weight)

new_weight = int(input("\nВведите вес нового контейнера: "))

position = len(containers) + 1

for i in range(len(containers)):
    if containers[i] < new_weight:
        position = i + 1
        break

print(f"\nНомер, который получит новый контейнер: {position}")