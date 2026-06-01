class Component:
    def __init__(self, title):
        self.title = title


class Reaction:
    def __init__(self, item1, item2, result):
        self.item1 = item1
        self.item2 = item2
        self.result = result

    def is_successful(self, ing1, ing2):
        return {self.item1, self.item2} == {ing1, ing2}


class Laboratory:
    def __init__(self):
        self.inventory = {"вода", "огонь", "воздух", "земля"}

        self.formulas = [
            Reaction("вода", "земля", "грязь"),
            Reaction("огонь", "земля", "камень"),
            Reaction("вода", "огонь", "пар"),
            Reaction("земля", "воздух", "пыль"),
            Reaction("вода", "воздух", "облако"),
            Reaction("огонь", "воздух", "энергия"),
            Reaction("облако", "вода", "дождь")
        ]

    def mix_items(self, ing1, ing2):
        if ing1 not in self.inventory or ing2 not in self.inventory:
            return "У тебя пока нет таких материалов для опытов."

        for formula in self.formulas:
            if formula.is_successful(ing1, ing2):
                new_item = formula.result

                if new_item in self.inventory:
                    return f"Ты уже открывал '{new_item}' раньше. Попробуй что-то другое."

                self.inventory.add(new_item)
                return f"Бинго! [{ing1}] + [{ing2}] = [{new_item}]!"

        return "Пшик... Из этой смеси ничего не вышло."

    def display_inventory(self):
        print("\nТвоя колба содержит:")
        for item in sorted(self.inventory):
            print(f" ~ {item}")
        print()

    def run(self):
        print("=== СИМУЛЯТОР АЛХИМИКА ===")
        print("Введи два элемента через пробел, чтобы смешать их.")
        print("Введи 'инвентарь', чтобы посмотреть свои элементы.")
        print("Введи 'стоп' для выхода.\n")

        while True:
            action = input("Что делаем? > ").strip().lower()

            if action == "инвентарь":
                self.display_inventory()
            elif action == "стоп":
                print("Лаборатория закрыта. До встречи!")
                break
            else:
                words = action.split()
                if len(words) == 2:
                    message = self.mix_items(words[0], words[1])
                    print(message + "\n")
                else:
                    print("Ошибка: нужно ввести ровно два слова через пробел (например: вода огонь).\n")


if __name__ == "__main__":
    game = Laboratory()
    game.run()