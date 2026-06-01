import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [max(first_result, second_result) for first_result, second_result in zip(first_team, second_team)]

print(f"Первая команда: {first_team}")
print(f"Вторая команда: {second_team}")
print(f"Победители тура: {winners}")
