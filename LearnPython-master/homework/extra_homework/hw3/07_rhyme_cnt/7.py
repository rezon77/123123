people_count = int(input("Кол-во человек: "))
rhyme_number = int(input("Какое число в считалке? "))

people = list(range(1, people_count + 1))
current_index = 0

print(f"Значит, выбывает каждый {rhyme_number}-й человек")

while len(people) > 1:
    print(f"\nТекущий круг людей: {people}")
    print(f"Начало счёта с номера {people[current_index]}")

    current_index = (current_index + rhyme_number - 1) % len(people)
    removed_person = people.pop(current_index)

    print(f"Выбывает человек под номером {removed_person}")

    if current_index == len(people):
        current_index = 0

print(f"\nОстался человек под номером {people[0]}")
