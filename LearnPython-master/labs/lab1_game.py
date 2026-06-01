import os


class Gesture:
    def __init__(self, name):
        self.name = name

    def __gt__(self, other):
        return False

    def __str__(self):
        return self.name.capitalize()


class Rock(Gesture):
    def __init__(self):
        super().__init__("камень")

    def __gt__(self, other):
        return isinstance(other, Scissors)


class Paper(Gesture):
    def __init__(self):
        super().__init__("бумага")

    def __gt__(self, other):
        return isinstance(other, Rock)


class Scissors(Gesture):
    def __init__(self):
        super().__init__("ножницы")

    def __gt__(self, other):
        return isinstance(other, Paper)


class Participant:
    def __init__(self, nickname):
        self.nickname = nickname
        self.points = 0
        self.current_choice = None

    def choose(self):
        print(f"\n--- Ход игрока {self.nickname} ---")
        options = {"1": Rock(), "2": Scissors(), "3": Paper()}

        while True:
            move = input("Выберите (1 - Камень, 2 - Ножницы, 3 - Бумага): ").strip()
            if move in options:
                self.current_choice = options[move]
                break
            print("Ошибка! Введите число от 1 до 3.")


class GameEngine:
    def __init__(self):
        self.players = []
        self.total_rounds = 0

    @staticmethod
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def setup(self):
        self.clear()
        print("=== Лабораторная работа: Камень-Ножницы-Бумага ===")
        try:
            count = int(input("Введите количество участников: "))
            for i in range(count):
                name = input(f"Имя {i + 1}-го игрока: ")
                self.players.append(Participant(name))

            self.total_rounds = int(input("Сколько раундов играем? "))
        except ValueError:
            print("Нужно вводить числа! Перезапустите игру.")
            exit()

    def find_round_winners(self):
        winners = []
        for p1 in self.players:
            is_winner = True
            for p2 in self.players:
                if p1 == p2: continue
                if p2.current_choice > p1.current_choice:
                    is_winner = False
                    break

            if is_winner:
                can_beat_someone = any(p1.current_choice > other.current_choice for other in self.players)
                if can_beat_someone:
                    winners.append(p1)

        return winners

    def run(self):
        self.setup()

        for r in range(1, self.total_rounds + 1):
            self.clear()
            print(f"РАУНД №{r}")

            for p in self.players:
                p.choose()
                self.clear()

            print("\nРезультаты раунда:")
            for p in self.players:
                print(f"{p.nickname} выбрал: {p.current_choice}")

            round_winners = self.find_round_winners()

            if not round_winners:
                print("\nрезультат: НИЧЬЯ")
            else:
                print("\nПобедители раунда:")
                for w in round_winners:
                    w.points += 1
                    print(f" - {w.nickname}")

            input("\nНажмите Enter, чтобы продолжить...")

        self.show_final_stats()

    def show_final_stats(self):
        self.clear()
        print("=== ИТОГИ ИГРЫ ===")
        sorted_players = sorted(self.players, key=lambda x: x.points, reverse=True)

        for p in sorted_players:
            print(f"{p.nickname}: {p.points} очк.")

        print("\nИгра окончена. Спасибо!")


if __name__ == "__main__":
    game = GameEngine()
    game.run()