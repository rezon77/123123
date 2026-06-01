skates_count = int(input("Кол-во коньков: "))
skates_sizes = []

for skate_number in range(1, skates_count + 1):
    skate_size = int(input(f"Размер {skate_number}-й пары: "))
    skates_sizes.append(skate_size)

people_count = int(input("\nКол-во людей: "))
foot_sizes = []

for person_number in range(1, people_count + 1):
    foot_size = int(input(f"Размер ноги {person_number}-го человека: "))
    foot_sizes.append(foot_size)

skates_sizes.sort()
foot_sizes.sort()

skate_index = 0
foot_index = 0
matched_people = 0

while skate_index < len(skates_sizes) and foot_index < len(foot_sizes):
    if skates_sizes[skate_index] == foot_sizes[foot_index]:
        matched_people += 1
        skate_index += 1
        foot_index += 1
    elif skates_sizes[skate_index] < foot_sizes[foot_index]:
        skate_index += 1
    else:
        foot_index += 1

print(f"\nНаибольшее кол-во людей, которые могут взять ролики: {matched_people}")
